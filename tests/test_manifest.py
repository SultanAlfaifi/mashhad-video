import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent
SCRIPT = ROOT.parent / 'skills/mashhad-video/scripts/project_manifest.py'
spec = importlib.util.spec_from_file_location('manifest', SCRIPT)
module = importlib.util.module_from_spec(spec)
sys.dont_write_bytecode = True
spec.loader.exec_module(module)


class ManifestTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=ROOT)
        self.path = Path(self.temp.name)
        self.manifest = {'schema_version': '1.0', 'title': 'مَشْهَد', 'primary_engine': 'remotion',
                         'spec': {'width': 1080, 'height': 1920, 'fps': {'num': 30000, 'den': 1001}, 'duration_frames': 300},
                         'shots': [{'id': 'a', 'engine': 'blender', 'layer': 'base', 'start_frame': 0, 'duration_frames': 150, 'status': 'planned'},
                                   {'id': 'b', 'engine': 'remotion', 'layer': 'base', 'start_frame': 150, 'duration_frames': 150, 'status': 'planned'}],
                         'transitions': [], 'assets': [], 'versions': {}}
    def tearDown(self):
        self.temp.cleanup()
    def errors(self, data=None, files=False):
        return module.validate(self.manifest if data is None else data, self.path, files)
    def test_rational_fps_and_exact_coverage(self):
        self.assertEqual(self.errors(), [])
    def test_real_timeline_gap(self):
        self.manifest['shots'][1].update(start_frame=151, duration_frames=149)
        self.assertTrue(self.errors())
    def test_undeclared_overlap(self):
        self.manifest['shots'][1].update(start_frame=140, duration_frames=160)
        self.assertTrue(self.errors())
    def test_valid_transition(self):
        self.manifest['shots'][1].update(start_frame=140, duration_frames=160)
        self.manifest['transitions'] = [{'from': 'a', 'to': 'b', 'start_frame': 140, 'duration_frames': 10}]
        self.assertEqual(self.errors(), [])
    def test_transition_must_match_actual_overlap(self):
        self.manifest['shots'][1].update(start_frame=140, duration_frames=160)
        self.manifest['transitions'] = [{'from': 'a', 'to': 'b', 'start_frame': 140, 'duration_frames': 11}]
        self.assertTrue(self.errors())
    def test_overlay_within_film(self):
        self.manifest['shots'].append({'id': 'label', 'engine': 'remotion', 'layer': 'overlay', 'start_frame': 125, 'duration_frames': 100, 'status': 'planned'})
        self.assertEqual(self.errors(), [])
        self.manifest['shots'][-1]['duration_frames'] = 200
        self.assertTrue(self.errors())
    def test_duplicate_shot_ids(self):
        self.manifest['shots'][1]['id'] = 'a'
        self.assertTrue(self.errors())
    def test_boolean_fraction_and_negative_frames_rejected(self):
        for bad in (True, -1, 1.5, None):
            with self.subTest(bad=bad):
                current = copy.deepcopy(self.manifest)
                current['shots'][0]['duration_frames'] = bad
                self.assertTrue(self.errors(current))
    def test_invalid_fps(self):
        self.manifest['spec']['fps']['den'] = 0
        self.assertTrue(self.errors())
    def test_rendered_state_needs_evidence(self):
        self.manifest['shots'][0]['status'] = 'rendered'
        self.assertTrue(self.errors())
        self.manifest['shots'][0].update(source='scene.py', media='scene.mov')
        self.assertEqual(self.errors(), [])
        self.assertTrue(self.errors(files=True))
        for name in ('scene.py', 'scene.mov'):
            (self.path / name).write_text('fixture', encoding='utf-8')
        self.assertEqual(self.errors(files=True), [])  # Path evidence only, not media certification.
    def test_review_and_approval_are_distinct(self):
        self.manifest['shots'][0].update(status='reviewed', source='scene.py', media='scene.mov')
        self.assertTrue(self.errors())
        self.manifest['shots'][0]['review'] = 'review.json'
        self.assertEqual(self.errors(), [])
        self.manifest['shots'][0]['status'] = 'approved'
        self.assertTrue(self.errors())
    def test_corrupt_shapes_do_not_crash(self):
        for value in (None, [], {'spec': []}, {**self.manifest, 'shots': [None]}, {**self.manifest, 'transitions': [None]}, {**self.manifest, 'assets': [None]}):
            with self.subTest(value=value):
                self.assertTrue(module.validate(value, self.path))
    def test_asset_provenance(self):
        self.manifest['assets'] = [{'id': 'logo', 'path': 'logo.svg'}]
        self.assertTrue(self.errors())
        self.manifest['assets'][0]['provenance'] = 'user-supplied'
        self.assertEqual(self.errors(), [])
    def test_cli_create_validate_and_overwrite_protection(self):
        output = self.path / 'mashhad.json'
        command = [sys.executable, str(SCRIPT), 'new', str(output), '--title', 'مَشْهَد', '--engine', 'remotion', '--fps', '30000/1001']
        first = subprocess.run(command, capture_output=True)
        self.assertEqual(first.returncode, 0, first.stderr)
        before = output.read_bytes()
        second = subprocess.run(command, capture_output=True)
        self.assertEqual(second.returncode, 2)
        self.assertEqual(before, output.read_bytes())
        check = subprocess.run([sys.executable, str(SCRIPT), 'validate', str(output), '--check-files'], capture_output=True)
        self.assertEqual(check.returncode, 0, check.stderr)
    def test_cli_malformed_json_fails(self):
        output = self.path / 'bad.json'
        output.write_text('{', encoding='utf-8')
        result = subprocess.run([sys.executable, str(SCRIPT), 'validate', str(output)], capture_output=True)
        self.assertEqual(result.returncode, 2)


if __name__ == '__main__':
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ManifestTests))
    report = {'suite': 'frame manifest', 'tests_run': result.testsRun, 'failures': len(result.failures), 'errors': len(result.errors), 'passed': result.wasSuccessful()}
    (ROOT / 'manifest-results.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    sys.exit(0 if result.wasSuccessful() else 1)
