#!/usr/bin/env python3
"""Install this local skill for Codex and/or Claude Code. No network or app setup."""
import argparse
import json
from pathlib import Path
import shutil
import sys

SOURCE=Path(__file__).resolve().parents[1]/'skills/mashhad-video'

def destinations(agent,scope,project=None,home=None):
    home=Path(home) if home is not None else Path.home()
    base=Path(project).resolve() if scope=='project' else home
    clients=('codex','claude') if agent=='both' else (agent,)
    result={}
    for client in clients:
        if client=='codex':
            current=base/'.agents/skills/mashhad-video'
            legacy=base/'.codex/skills/mashhad-video'
            if scope=='user' and not current.exists() and legacy.exists():current=legacy
            result[client]=current
        else:result[client]=base/'.claude/skills/mashhad-video'
    return result

def install(source,targets,dry_run=False):
    if not (source/'SKILL.md').is_file():raise ValueError('Skill source is missing')
    files=[p for p in source.rglob('*') if p.is_file()
           and '__pycache__' not in p.parts and p.suffix not in ('.pyc','.pyo')]
    if any(p.is_symlink() for p in source.rglob('*')):raise ValueError('Symlinked sources are not supported')
    for dest in targets.values():
        if dest.exists():raise FileExistsError(str(dest)+' already exists; preserve or back it up before replacing it')
        if dest.is_symlink():raise ValueError('Symlink destination is not supported')
    if not dry_run:
        for dest in targets.values():
            dest.mkdir(parents=True,exist_ok=False)
            for original in files:
                target=dest/original.relative_to(source)
                target.parent.mkdir(parents=True,exist_ok=True)
                shutil.copy2(original,target)
    return {'dry_run':dry_run,'files_per_agent':len(files),'destinations':{k:str(v) for k,v in targets.items()},
            'runtime_installs':False,'application_launch':False}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--agent',choices=['codex','claude','both'],default='both')
    parser.add_argument('--scope',choices=['user','project'],default='user')
    parser.add_argument('--project',type=Path,default=Path.cwd())
    parser.add_argument('--dry-run',action='store_true')
    args=parser.parse_args()
    try:
        print(json.dumps(install(SOURCE,destinations(args.agent,args.scope,args.project),args.dry_run),ensure_ascii=False,indent=2))
        return 0
    except (OSError,ValueError) as exc:
        print(json.dumps({'error':str(exc)},ensure_ascii=False),file=sys.stderr);return 1

if __name__=='__main__':sys.exit(main())
