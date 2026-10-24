# .meta/scripts/tests/test_check_readme.py - Exercise offline validation boundaries.

import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location(
    "check_readme", Path(__file__).parents[1] / "check_readme.py"
)
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)

TITLE = '<h1 align="center">Profile</h1>'
CODE = '```python\nprint("protected verse")\n```'
TAIL = (
    '<details>\n<summary>def thoughts(self):</summary>\n'
    'A protected thought.\n</details>\n\n[EOF]: keep-me\n'
)
README = (
    TITLE + '\n\n' + CODE + '\n\n'
    'Editable prose.\n[Image](assets/picture.png)\n'
    '[Credits](assets/README.md#credits)\n'
    '<a name="projects"></a>\n[Projects](#projects)\n'
    '<details open>\n<summary>Projects</summary>\n'
    '<img src="assets/picture.png">\n</details>\n\n' + TAIL
)


class ReadmeTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        (self.root / ".meta/scripts").mkdir(parents=True)
        (self.root / "assets").mkdir()
        self.readme = self.root / "README.md"
        self.readme.write_text(README)
        (self.root / "assets/picture.png").write_bytes(b"synthetic asset")
        (self.root / "assets/README.md").write_text("# Credits\n")
        # Expected regions are explicit fixture constants, not validator output
        manifest = {
            "title": hashlib.sha256(TITLE.encode()).hexdigest(),
            "code_blocks": [hashlib.sha256(CODE.encode()).hexdigest()],
            "thoughts_and_after": hashlib.sha256(TAIL.encode()).hexdigest(),
            "files": {
                "assets/picture.png": hashlib.sha256(b"synthetic asset").hexdigest(),
                "assets/README.md": hashlib.sha256(b"# Credits\n").hexdigest(),
            },
        }
        self.manifest = self.root / ".meta/scripts/readme_invariants.json"
        self.manifest.write_text(json.dumps(manifest))

    def test_valid_documents_and_prose_edits_pass(self):
        self.assertEqual(validator.check(self.root), [])
        self.readme.write_text(README.replace("Editable prose.", "Clearer prose."))
        self.assertEqual(validator.check(self.root), [])

    def test_protected_title_code_and_tail_fail_independently(self):
        for before, after in [
            (TITLE, "<h1>Changed title</h1>"),
            ('print("protected verse")', 'print("rewritten verse")'),
            ("A protected thought.", "An edited thought."),
            ("[EOF]: keep-me", "[EOF]: changed"),
        ]:
            with self.subTest(region=before):
                self.readme.write_text(README.replace(before, after))
                self.assertTrue(validator.check(self.root))

    def test_missing_and_changed_assets_fail(self):
        image = self.root / "assets/picture.png"
        image.write_bytes(b"different image")
        self.assertTrue(validator.check(self.root))
        image.unlink()
        self.assertTrue(validator.check(self.root))

    def test_malformed_disclosures_fail(self):
        for before, after in [
            ("<summary>Projects</summary>", "Projects"),
            ("<summary>Projects</summary>", "<summary>Projects</details>"),
            ("<details open>", "<details open><summary>Extra</summary>"),
        ]:
            with self.subTest(markup=after):
                self.readme.write_text(README.replace(before, after))
                self.assertTrue(validator.check(self.root))

    def test_missing_local_links_and_anchors_fail(self):
        for target in ("missing.md", "#absent", "assets/README.md#absent"):
            with self.subTest(target=target):
                self.readme.write_text(README.replace("#projects)", target + ")"))
                self.assertTrue(validator.check(self.root))

    def test_external_links_and_code_examples_need_no_network(self):
        prose = (
            '[Remote](https://invalid.example/not-fetched)\n'
            '[Mail](mailto:person@example.invalid)\n'
            '`[Example](missing.md)`\n'
            '```html\n<details><img src="missing.png">\n```\n'
        )
        parsed = validator.document(prose)
        self.assertEqual(parsed.errors, [])
        self.assertEqual(len(parsed.links), 2)
        self.readme.write_text(
            README.replace("Editable prose.", prose.splitlines()[0])
        )
        self.assertEqual(validator.check(self.root), [])

    def test_heading_code_labels_keep_their_anchor(self):
        parsed = validator.document("## Run `checks`\n## Run `checks`\n")
        self.assertEqual(parsed.anchors, {"run-checks", "run-checks-1"})

    def test_local_references_cannot_leave_the_checkout(self):
        with tempfile.TemporaryDirectory() as outside:
            target = Path(outside) / "private.md"
            target.write_text("Must not be read")
            link = self.root / "outside.md"
            link.symlink_to(target)
            with self.assertRaisesRegex(ValueError, "leaves the repository"):
                validator.local_path(self.root.resolve(), self.readme, "outside.md")

    def test_missing_baseline_is_a_reported_failure(self):
        self.manifest.unlink()
        self.assertTrue(validator.check(self.root))


if __name__ == "__main__":
    unittest.main()
