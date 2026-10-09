#!/usr/bin/env python3
"""Create or validate a frame-based production ledger; no engine execution.

Exit codes: 0 valid/created, 1 invalid manifest, 2 input/output or argument error.
Extra fields are retained for native-engine metadata, not interpreted as commands.
"""
import argparse
import json
from pathlib import Path
from fractions import Fraction
import sys


def integer(value, minimum=0):
    return type(value) is int and value >= minimum


def validate(data, directory, check_files=False):
    errors = []
    def require(ok, message):
        if not ok:
            errors.append(message)
        return ok

    def evidence(value, label):
        if not require(isinstance(value, str) and bool(value.strip()), label + ' must be a path'):
            return
        if check_files:
            try:
                path = Path(value)
                if not path.is_absolute():
                    path = directory / path
                require(path.is_file(), label + ' file does not exist: ' + value)
            except (OSError, ValueError):
                errors.append(label + ' is not a usable file path')

    if not require(isinstance(data, dict), 'Root must be an object'):
        return errors
    require(data.get('schema_version') == '1.0', 'schema_version must be "1.0"')
    for name in ('title', 'primary_engine'):
        require(isinstance(data.get(name), str) and bool(data[name].strip()), name + ' must be nonempty')
    spec = data.get('spec')
    if not require(isinstance(spec, dict), 'spec must be an object'):
        return errors
    for name in ('width', 'height', 'duration_frames'):
        require(integer(spec.get(name), 1), 'spec.' + name + ' must be a positive integer')
    fps = spec.get('fps')
    if require(isinstance(fps, dict), 'spec.fps must be {num, den}'):
        require(integer(fps.get('num'), 1) and integer(fps.get('den'), 1), 'FPS numerator and denominator must be positive integers')
    duration = spec.get('duration_frames')
    shots = data.get('shots')
    if not require(isinstance(shots, list) and bool(shots), 'shots must be a nonempty array'):
        return errors
    spans, ids = {}, set()
    states = ('planned', 'source_ready', 'rendered', 'reviewed', 'approved')
    for index, shot in enumerate(shots):
        label = 'shots[' + str(index) + ']'
        if not require(isinstance(shot, dict), label + ' must be an object'):
            continue
        shot_id = shot.get('id')
        valid_id = isinstance(shot_id, str) and bool(shot_id.strip())
        require(valid_id, label + '.id must be nonempty')
        if valid_id:
            require(shot_id not in ids, 'Duplicate shot id: ' + shot_id)
            ids.add(shot_id)
        layer, status = shot.get('layer'), shot.get('status')
        require(layer in ('base', 'overlay'), label + '.layer must be base or overlay')
        valid_state = require(status in states, label + '.status is invalid')
        require(isinstance(shot.get('engine'), str) and bool(shot['engine'].strip()), label + '.engine must be nonempty')
        start, length = shot.get('start_frame'), shot.get('duration_frames')
        valid_range = integer(start) and integer(length, 1)
        require(valid_range, label + ' requires a nonnegative integer start and positive integer duration')
        if valid_range and integer(duration, 1):
            require(start + length <= duration, label + ' extends beyond the film')
            if valid_id:
                spans[shot_id] = (start, start + length, layer)
        for field in ('source', 'media', 'review', 'approval'):
            if field in shot:
                evidence(shot[field], label + '.' + field)
        if valid_state:
            rank = states.index(status)
            for threshold, field in ((1, 'source'), (2, 'media'), (3, 'review'), (4, 'approval')):
                if rank >= threshold:
                    require(field in shot, label + '.' + field + ' evidence is required for ' + status)

    transitions = data.get('transitions', [])
    declared = set()
    if require(isinstance(transitions, list), 'transitions must be an array'):
        for index, transition in enumerate(transitions):
            label = 'transitions[' + str(index) + ']'
            if not require(isinstance(transition, dict), label + ' must be an object'):
                continue
            left, right = transition.get('from'), transition.get('to')
            if not require(isinstance(left, str) and isinstance(right, str) and left != right
                           and left in spans and right in spans, label + ' requires two distinct existing shots'):
                continue
            a, b = spans[left], spans[right]
            start, length = transition.get('start_frame'), transition.get('duration_frames')
            if not require(integer(start) and integer(length, 1), label + ' has invalid frame range'):
                continue
            overlap = (max(a[0], b[0]), min(a[1], b[1]))
            require(a[2] == b[2] == 'base', label + ' must join base shots')
            require(a[0] < b[0], label + '.from must precede .to')
            require(overlap[1] > overlap[0] and (start, start + length) == overlap,
                    label + ' must exactly describe the visible shot overlap')
            key = frozenset((left, right))
            require(key not in declared, label + ' duplicates a transition')
            declared.add(key)

    base = sorted((start, end, name) for name, (start, end, layer) in spans.items() if layer == 'base')
    cursor = 0
    require(bool(base), 'At least one base shot must cover the film')
    for index, (start, end, name) in enumerate(base):
        require(start <= cursor, 'Uncovered frames before ' + name + ': ' + str(cursor) + '..' + str(start))
        cursor = max(cursor, end)
        for other_start, other_end, other_name in base[:index]:
            if start < other_end and other_start < end:
                require(frozenset((other_name, name)) in declared,
                        'Undeclared base overlap: ' + other_name + ' / ' + name)
    if integer(duration, 1):
        require(cursor == duration, 'Base timeline coverage must end at duration_frames')
    assets = data.get('assets', [])
    asset_ids = set()
    if require(isinstance(assets, list), 'assets must be an array'):
        for index, asset in enumerate(assets):
            label = 'assets[' + str(index) + ']'
            if not require(isinstance(asset, dict), label + ' must be an object'):
                continue
            asset_id = asset.get('id')
            if require(isinstance(asset_id, str) and bool(asset_id.strip()), label + '.id must be nonempty'):
                require(asset_id not in asset_ids, 'Duplicate asset id: ' + asset_id)
                asset_ids.add(asset_id)
            require(isinstance(asset.get('provenance'), str) and bool(asset['provenance'].strip()), label + '.provenance is required')
            if 'path' in asset:
                evidence(asset['path'], label + '.path')
    if 'versions' in data:
        require(isinstance(data['versions'], dict), 'versions must be an object')
    return errors


def positive_integer(value):
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError('must be positive')
    return number


def frame_rate(value):
    try:
        fps = Fraction(value)
        if fps <= 0:
            raise ValueError()
        return fps
    except (ValueError, ZeroDivisionError):
        raise argparse.ArgumentTypeError('use a positive FPS, such as 30 or 30000/1001')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    new = commands.add_parser('new', help='Create a planned one-shot project, refusing overwrite')
    new.add_argument('file', type=Path)
    new.add_argument('--title', required=True)
    new.add_argument('--engine', required=True)
    new.add_argument('--width', type=positive_integer, default=1920)
    new.add_argument('--height', type=positive_integer, default=1080)
    new.add_argument('--fps', type=frame_rate, default=Fraction(30))
    new.add_argument('--frames', type=positive_integer, default=300)
    check = commands.add_parser('validate', help='Validate schema, timing and optional local evidence paths')
    check.add_argument('file', type=Path)
    check.add_argument('--check-files', action='store_true')
    args = parser.parse_args()
    try:
        if args.command == 'new':
            data = {'schema_version': '1.0', 'title': args.title, 'primary_engine': args.engine,
                    'spec': {'width': args.width, 'height': args.height,
                             'fps': {'num': args.fps.numerator, 'den': args.fps.denominator},
                             'duration_frames': args.frames, 'color_space': 'bt709'},
                    'shots': [{'id': 'shot-01', 'start_frame': 0, 'duration_frames': args.frames,
                               'layer': 'base', 'engine': args.engine, 'status': 'planned'}],
                    'transitions': [], 'assets': [], 'versions': {args.engine: 'unknown'}}
            errors = validate(data, args.file.parent)
            if errors:
                print(json.dumps({'valid': False, 'errors': errors}, ensure_ascii=False, indent=2))
                return 1
            args.file.parent.mkdir(parents=True, exist_ok=True)
            with args.file.open('x', encoding='utf-8') as handle:
                json.dump(data, handle, ensure_ascii=False, indent=2)
                handle.write('\n')
            print(json.dumps({'created': str(args.file.resolve()), 'status': 'planned'}, ensure_ascii=False))
            return 0
        with args.file.open(encoding='utf-8-sig') as handle:
            data = json.load(handle)
        errors = validate(data, args.file.parent.resolve(), args.check_files)
        print(json.dumps({'valid': not errors, 'errors': errors, 'files_checked': args.check_files,
                          'scope': 'structural/timing/path checks; no media or creative review'}, ensure_ascii=False, indent=2))
        return 1 if errors else 0
    except (OSError, ValueError) as exc:
        print(json.dumps({'valid': False, 'error': str(exc)}, ensure_ascii=False))
        return 2


if __name__ == '__main__':
    sys.exit(main())
