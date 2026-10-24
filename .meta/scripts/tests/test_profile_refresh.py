# .meta/scripts/tests/test_profile_refresh.py - Check identity and publishing gates.

import contextlib
from datetime import date
import io
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import textwrap
import unittest
from unittest.mock import patch

from test_project_metadata import metadata

ROOT = Path(__file__).resolve().parents[3]
WORKFLOW = ROOT / '.github/workflows/profile-refresh.yml'


def card(repository='owner/public', private=False, activity='Old.'):
    title = '<strong>Project</strong>'
    if private:
        title = '🔒 ' + title
    else:
        title = f'<a href="https://github.com/{repository}">{title}</a>'
    return (
        f'<details data-repo="{repository}">\n<summary>{title} — Purpose.</summary>\n'
        '| **Flow** | _input → review_ |\n'
        '| **Maturity** | `Experimental` · `v0.3.0` · TRL 3 |\n'
        '| **Status** | Only a controlled demonstration. |\n'
        f'| **Activity** | {activity} |\n'
        '| **Tags** | `python` |\n</details>\n'
    )


def fact(repository='owner/public', private=False):
    return {
        'repository': repository,
        'visibility': 'Private' if private else 'Public',
        'updated': '2026-10-23',
        'activity': 'Recent',
    }


def step(name):
    section = WORKFLOW.read_text().split(f'      - name: {name}\n', 1)[1]
    section = section.split('      - name:', 1)[0]
    return textwrap.dedent(section.split('        run: |\n', 1)[1])


class IdentityTests(unittest.TestCase):
    def test_public_and_unlinked_private_cards_preserve_authored_fields(self):
        before = card() + card('owner/private', True)
        rows = [fact(), fact('owner/private', True)]
        after, count = metadata.reconcile(before, rows, date(2026, 10, 24))
        self.assertEqual(count, 2)
        self.assertEqual(after, before.replace('Old.', 'Updated 2026-10-23 · `Recent`'))
        self.assertEqual(
            metadata.reconcile(after, rows, date(2026, 10, 25)), (after, 0)
        )

    def test_arbitrary_urls_are_not_projects(self):
        text = card() + '\n[Reference](https://github.com/other/reference)\n'
        self.assertEqual(
            [c['repository'] for c in metadata.projects(text)], ['owner/public']
        )

    def test_missing_duplicate_invalid_or_mismatched_ids_fail(self):
        examples = [
            card().replace(' data-repo="owner/public"', ''),
            card() + card(),
            card('../owner/public'),
            card('owner/..'),
            card('./public'),
            card().replace('data-repo="owner/public"', 'data-repo="owner/other"'),
        ]
        for text in examples:
            with self.subTest(text=text), self.assertRaises(ValueError):
                metadata.projects(text)

    def test_private_title_and_version_links_are_rejected(self):
        private = card('owner/private', True)
        examples = [
            private.replace(
                '<strong>Project</strong>',
                '<a href="https://example.invalid"><strong>Project</strong></a>',
            ),
            private.replace(
                '`v0.3.0`', '[`v0.3.0`](https://example.invalid/release)'
            ),
        ]
        for text in examples:
            with self.subTest(text=text), self.assertRaises(ValueError):
                metadata.projects(text)

    def test_private_opt_in_precedes_all_api_calls(self):
        with patch.object(metadata, 'github') as api:
            row = metadata.collect('owner/private', date(2026, 10, 24), 30, [], True)
        api.assert_not_called()
        self.assertIn('error', row)

    def test_visibility_drift_stops_before_commit_and_release_queries(self):
        with patch.object(
            metadata, 'github',
            return_value={'private': False, 'full_name': 'owner/private'},
        ) as api:
            row = metadata.collect(
                'owner/private', date(2026, 10, 24), 30, ['owner/private'], True
            )
        self.assertEqual(api.call_count, 1)
        self.assertIn('error', row)

    def test_failed_access_does_not_expose_api_stderr(self):
        error = subprocess.CalledProcessError(
            1, ['gh'], stderr='private response and credential must stay hidden'
        )
        with patch.object(metadata, 'github', side_effect=error):
            row = metadata.collect('owner/public', date(2026, 10, 24), 30, [])
        self.assertEqual(row, {
            'repository': 'owner/public', 'error': 'CalledProcessError',
        })

    def test_malformed_api_payload_is_reported_without_its_contents(self):
        with patch.object(metadata, 'github', return_value=None):
            row = metadata.collect('owner/public', date(2026, 10, 24), 30, [])
        self.assertEqual(row, {'repository': 'owner/public', 'error': 'TypeError'})

    def test_unlisted_private_opt_in_never_starts_collection(self):
        with tempfile.TemporaryDirectory() as directory:
            readme = Path(directory) / 'README.md'
            readme.write_text(card())
            with (
                patch.object(sys, 'argv', [
                    'metadata', '--readme', str(readme),
                    '--include-private', 'owner/unknown',
                ]),
                patch.object(metadata, 'collect') as collect,
                contextlib.redirect_stderr(io.StringIO()),
                self.assertRaises(SystemExit),
            ):
                metadata.main()
            collect.assert_not_called()

    def test_unknown_duplicate_redirected_and_incomplete_facts_refuse(self):
        for rows in [
            [], [fact('owner/unknown')], [fact(), fact()],
            [{'repository': 'owner/public', 'redirects_to': 'owner/new'}],
            [{'repository': 'owner/public', 'error': 'Unavailable'}],
        ]:
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                metadata.reconcile(card(), rows, date(2026, 10, 24))

    def test_quiet_failure_preserves_readme_and_hides_repository_facts(self):
        with tempfile.TemporaryDirectory() as directory:
            readme = Path(directory) / 'README.md'
            source = card()
            readme.write_text(source)
            stdout, stderr = io.StringIO(), io.StringIO()
            with (
                patch.object(sys, 'argv', [
                    'metadata', '--readme', str(readme), '--write', '--quiet',
                ]),
                patch.object(metadata, 'collect', return_value={
                    'repository': 'owner/public', 'error': 'Private failure body',
                }),
                contextlib.redirect_stdout(stdout),
                contextlib.redirect_stderr(stderr),
            ):
                self.assertEqual(metadata.main(), 1)
            self.assertEqual(readme.read_text(), source)
            self.assertNotIn(
                'Private failure body', stdout.getvalue() + stderr.getvalue()
            )

    def test_unchanged_facts_do_not_write_or_touch_padding(self):
        with tempfile.TemporaryDirectory() as directory:
            readme = Path(directory) / 'README.md'
            source = card(activity='Updated 2026-10-23 · `Recent`      ')
            readme.write_text(source)
            with (
                patch.object(sys, 'argv', [
                    'metadata', '--readme', str(readme), '--write', '--quiet',
                    '--as-of', '2026-10-24',
                ]),
                patch.object(metadata, 'collect', return_value=fact()),
                patch.object(Path, 'write_text') as write,
                contextlib.redirect_stdout(io.StringIO()),
            ):
                self.assertEqual(metadata.main(), 0)
                write.assert_not_called()
            self.assertEqual(readme.read_text(), source)

    def test_public_readme_and_workflow_agree_on_private_allowlist(self):
        text = (ROOT / 'README.md').read_text()
        cards = metadata.projects(text)
        private = {c['repository'] for c in cards if c['private']}
        allowed = set(re.findall(r'--include-private ([\w./-]+)', WORKFLOW.read_text()))
        self.assertEqual(private, allowed)
        self.assertTrue(private)
        for entry in cards:
            with self.subTest(repository=entry['repository']):
                if entry['private']:
                    self.assertNotIn('<a ', entry['match']['summary'])
                    self.assertNotIn(
                        'https://github.com/' + entry['repository'], entry['match'][0]
                    )
                else:
                    self.assertIn(
                        'https://github.com/' + entry['repository'],
                        entry['match']['summary'],
                    )


class PublishTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.origin = self.root / 'origin.git'
        self.seed = self.root / 'seed'
        self.runner = self.root / 'runner'
        self.git('init', '--quiet', '--bare', '--initial-branch=main', str(self.origin))
        self.git('init', '--quiet', '-b', 'main', str(self.seed))
        self.git('config', 'user.name', 'Fixture', cwd=self.seed)
        self.git('config', 'user.email', 'fixture@example.invalid', cwd=self.seed)
        self.git('config', 'commit.gpgsign', 'false', cwd=self.seed)
        (self.seed / 'README.md').write_text('original\n')
        (self.seed / 'other.txt').write_text('unrelated\n')
        self.git('add', '.', cwd=self.seed)
        self.git('commit', '--quiet', '-m', 'Fixture', cwd=self.seed)
        self.git('remote', 'add', 'origin', str(self.origin), cwd=self.seed)
        self.git('push', '--quiet', 'origin', 'main', cwd=self.seed)
        self.git('clone', '--quiet', str(self.origin), str(self.runner))
        self.git('config', 'commit.gpgsign', 'false', cwd=self.runner)
        (self.root / 'bin').mkdir()
        gh = self.root / 'bin/gh'
        gh.write_text('#!/bin/sh\nexit 0\n')
        gh.chmod(0o755)
        self.env = dict(
            os.environ,
            PATH=str(self.root / 'bin') + os.pathsep + os.environ['PATH'],
            GH_TOKEN='synthetic',
        )

    def git(self, *args, cwd=None):
        return subprocess.check_output(
            ['git', *args], cwd=cwd or self.root, text=True,
            stderr=subprocess.DEVNULL,
        ).strip()

    def publish(self):
        return subprocess.run(
            ['bash', '-e', '-o', 'pipefail', '-c',
             step('Commit and push changed activity')],
            cwd=self.runner, env=self.env, capture_output=True, text=True,
        )

    def test_unchanged_readme_exits_without_commit(self):
        self.assertEqual(self.publish().returncode, 0)
        self.assertEqual(self.git('rev-list', '--count', 'main', cwd=self.origin), '1')

    def test_only_readme_is_committed_by_the_bot(self):
        (self.runner / 'README.md').write_text('new activity\n')
        result = self.publish()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.git('rev-list', '--count', 'main', cwd=self.origin), '2')
        self.assertEqual(
            self.git('show', '--format=', '--name-only', 'HEAD', cwd=self.runner),
            'README.md',
        )
        self.assertEqual(
            self.git('show', '-s', '--format=%an|%s', cwd=self.runner),
            'github-actions[bot]|chore(profile): refresh project activity',
        )

    def test_concurrent_remote_update_refuses_to_commit_or_push(self):
        (self.seed / 'other.txt').write_text('concurrent update\n')
        self.git('add', '.', cwd=self.seed)
        self.git('commit', '--quiet', '-m', 'Concurrent', cwd=self.seed)
        self.git('push', '--quiet', 'origin', 'main', cwd=self.seed)
        expected = self.git('rev-parse', 'main', cwd=self.origin)
        (self.runner / 'README.md').write_text('new activity\n')
        self.assertNotEqual(self.publish().returncode, 0)
        self.assertEqual(self.git('rev-parse', 'main', cwd=self.origin), expected)
        self.assertEqual(self.git('rev-list', '--count', 'HEAD', cwd=self.runner), '1')

    def test_unrelated_file_changes_refuse_publication(self):
        (self.runner / 'README.md').write_text('new activity\n')
        (self.runner / 'other.txt').write_text('unexpected change\n')
        self.assertNotEqual(self.publish().returncode, 0)
        self.assertEqual(self.git('rev-list', '--count', 'main', cwd=self.origin), '1')

    def test_missing_private_token_stops_before_collection(self):
        result = subprocess.run(
            ['bash', '-e', '-o', 'pipefail', '-c',
             step('Collect and reconcile activity')],
            cwd=self.runner, env=dict(self.env, GH_TOKEN=''),
            capture_output=True, text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Configure PROFILE_METADATA_TOKEN', result.stdout)
        self.assertNotIn('python', result.stderr)


if __name__ == '__main__':
    unittest.main()
