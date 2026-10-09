import importlib.util
from pathlib import Path
import tempfile
import unittest

spec=importlib.util.spec_from_file_location('install',Path(__file__).resolve().parents[1]/'tools/install.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)

class InstallTests(unittest.TestCase):
    def test_both_clients_receive_complete_local_skill(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);source=root/'source';source.mkdir()
            (source/'SKILL.md').write_text('name: mashhad-video',encoding='utf-8')
            (source/'LICENSE').write_text('license evidence',encoding='utf-8')
            targets=module.destinations('both','user',home=root/'home')
            result=module.install(source,targets)
            self.assertEqual(result['files_per_agent'],2)
            for client,path in targets.items():
                self.assertEqual((path/'SKILL.md').read_bytes(),(source/'SKILL.md').read_bytes())
                self.assertTrue((path/'LICENSE').is_file())
    def test_existing_work_refused_before_any_writes(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);source=root/'source';source.mkdir();(source/'SKILL.md').write_text('source')
            targets=module.destinations('both','user',home=root/'home');targets['claude'].mkdir(parents=True)
            with self.assertRaises(FileExistsError):module.install(source,targets)
            self.assertFalse(targets['codex'].exists())
    def test_dry_run_and_project_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);source=root/'source';source.mkdir();(source/'SKILL.md').write_text('source')
            targets=module.destinations('both','project',project=root/'project')
            module.install(source,targets,True)
            self.assertFalse(any(p.exists() for p in targets.values()))
            self.assertEqual(targets['claude'],root/'project/.claude/skills/mashhad-video')
    def test_existing_codex_location_is_identified(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);legacy=root/'.codex/skills/mashhad-video';legacy.mkdir(parents=True)
            self.assertEqual(module.destinations('codex','user',home=root)['codex'],legacy)
    def test_local_bytecode_is_not_distributed(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);source=root/'source';source.mkdir()
            (source/'SKILL.md').write_text('source')
            cache=source/'scripts/__pycache__';cache.mkdir(parents=True)
            (cache/'helper.cpython-311.pyc').write_bytes(b'local build cache')
            target=root/'installed'
            result=module.install(source,{'claude':target})
            self.assertEqual(result['files_per_agent'],1)
            self.assertFalse((target/'scripts/__pycache__').exists())

if __name__=='__main__':unittest.main()
