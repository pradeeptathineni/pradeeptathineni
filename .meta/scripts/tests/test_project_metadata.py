# .meta/scripts/tests/test_project_metadata.py - Preserve scoped metadata refreshes.

import contextlib
from datetime import date, timedelta
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location(
    "metadata", Path(__file__).parents[1] / "project_metadata.py"
)
metadata = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(metadata)


class MetadataTests(unittest.TestCase):
    def test_reconcile_preserves_everything_outside_activity_and_check_date(self):
        before = (
            'keep atypical wording  \n'
            '<details>\n<summary>Group</summary>\n<details>\n'
            '<summary>🔒 <a href="https://github.com/owner/private">'
            '<strong>Private</strong></a> — Original.</summary>\n'
            '| **Status**   | Original status and spacing.   |\n'
            '| **Activity** | Updated 2000-01-01 · `Quiet`    |\n'
            '</details>\n</details>\n'
            '`#` Public release and activity facts last checked on 2000-01-01.\n'
            'trailing material  \n'
        )
        expected = before.replace(
            'Updated 2000-01-01 · `Quiet`    ',
            'Updated 2026-10-22 · `Recent`   ',
        ).replace(
            'Public release and activity facts last checked on 2000-01-01.',
            'Release and activity facts last checked on 2026-10-23.',
        )
        facts = [
            {
                'repository': 'owner/private',
                'updated': '2026-10-22',
                'activity': 'Recent',
            }
        ]
        result, count = metadata.reconcile(before, facts, date(2026, 10, 23))
        self.assertEqual(result, expected)
        self.assertEqual(count, 1)
        self.assertEqual(
            metadata.reconcile(result, facts, date(2026, 10, 23))[0], result
        )

    def test_unknown_project_and_non_activity_dates_survive(self):
        text = (
            '<details>\n<summary>'
            '<a href="https://github.com/owner/unknown">Name</a></summary>\n'
            '| **Activity** | Planning only. |\n'
            '| **Status** | Since 2020-01-01. |\n</details>\n'
        )
        self.assertEqual(metadata.reconcile(text, [], date(2026, 10, 23)), (text, 0))

    def collect(self, age, private=False, allow=False, archived=False):
        today = date(2026, 10, 23)
        # Noon UTC remains on the same New York calendar date
        timestamp = f'{today - timedelta(days=age)}T12:00:00Z'
        replies = [
            {
                'private': private,
                'full_name': 'owner/repo',
                'default_branch': 'main',
                'archived': archived,
                'html_url': 'https://github.com/owner/repo',
            },
            [{'commit': {'committer': {'date': timestamp}}}],
            [],
        ]
        with patch.object(metadata, 'github', side_effect=replies) as fetch:
            result = metadata.collect(
                'owner/repo', today, 30, ['owner/repo'] if allow else []
            )
            return result, fetch.call_count

    def test_quiet_boundary_is_after_thirty_days(self):
        self.assertEqual(self.collect(30)[0]['activity'], 'Recent')
        self.assertEqual(self.collect(31)[0]['activity'], 'Quiet')

    def test_future_and_archived_states(self):
        self.assertEqual(self.collect(-1)[0]['activity'], 'Unknown')
        self.assertEqual(self.collect(31, archived=True)[0]['activity'], 'Archived')

    def test_private_facts_require_explicit_opt_in(self):
        row, count = self.collect(0, private=True)
        self.assertIn('error', row)
        self.assertEqual(count, 1)
        row, count = self.collect(0, private=True, allow=True)
        self.assertEqual(row['visibility'], 'Private')
        self.assertIsNone(row['url'])
        self.assertEqual(count, 3)

    def test_new_york_date_release_and_private_release_url(self):
        release = {
            'draft': False,
            'published_at': '2026-10-16T10:00:00Z',
            'tag_name': 'v0.3.0',
            'prerelease': True,
            'html_url': 'https://github.com/owner/repo/releases/tag/v0.3.0',
        }
        for private in (False, True):
            replies = [
                {
                    'private': private,
                    'full_name': 'owner/repo',
                    'default_branch': 'main',
                    'archived': False,
                    'html_url': 'https://github.com/owner/repo',
                },
                [{'commit': {'committer': {'date': '2026-10-17T01:00:00Z'}}}],
                [release],
            ]
            with (
                self.subTest(private=private),
                patch.object(metadata, 'github', side_effect=replies),
            ):
                row = metadata.collect(
                    'owner/repo', date(2026, 10, 17), 30, ['owner/repo']
                )
            self.assertEqual(row['updated'], '2026-10-16')
            self.assertEqual(row['maturity'], 'v0.3.0')
            self.assertTrue(row['preview'])
            self.assertEqual(
                row['release_url'], None if private else release['html_url']
            )
            self.assertNotIn('trl', row)

    def test_missing_cli_and_redirect_are_explicit(self):
        with patch.object(metadata, 'github', side_effect=FileNotFoundError()):
            row = metadata.collect('owner/repo', date(2026, 10, 24), 30, [])
        self.assertEqual(row['error'], 'FileNotFoundError')
        with patch.object(
            metadata, 'github',
            return_value={'private': False, 'full_name': 'owner/new'},
        ):
            row = metadata.collect('owner/repo', date(2026, 10, 24), 30, [])
        self.assertEqual(row['redirects_to'], 'owner/new')

    def test_write_refuses_incomplete_facts(self):
        for reply in [
            {'private': True},
            {'private': False, 'full_name': 'owner/new'},
        ]:
            with self.subTest(reply=reply), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                script = root / '.meta/scripts/project_metadata.py'
                script.parent.mkdir(parents=True)
                readme = root / 'README.md'
                original = (
                    '<details>\n<summary>'
                    '<a href="https://github.com/owner/private">Private</a>'
                    '</summary>\n| **Activity** | Original. |\n</details>\n'
                )
                readme.write_text(original)
                stdout, stderr = io.StringIO(), io.StringIO()
                with (
                    patch.object(metadata, '__file__', str(script)),
                    patch.object(sys, 'argv', ['metadata', '--write']),
                    patch.object(metadata, 'github', return_value=reply),
                    contextlib.redirect_stdout(stdout),
                    contextlib.redirect_stderr(stderr),
                ):
                    result = metadata.main()
                self.assertEqual(result, 1)
                self.assertEqual(readme.read_text(), original)
                self.assertIn('README unchanged', stderr.getvalue())
                self.assertEqual(json.loads(stdout.getvalue())['recent_days'], 30)

    def test_write_applies_complete_collection(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            script = root / '.meta/scripts/project_metadata.py'
            script.parent.mkdir(parents=True)
            readme = root / 'README.md'
            readme.write_text(
                '<details>\n<summary>'
                '<a href="https://github.com/owner/repo">Repo</a></summary>\n'
                '| **Activity** | Original. |\n</details>\n'
            )
            replies = [
                {
                    'private': False,
                    'full_name': 'owner/repo',
                    'default_branch': 'main',
                    'archived': False,
                    'html_url': 'https://github.com/owner/repo',
                },
                [{'commit': {'committer': {'date': '2026-09-22T12:00:00Z'}}}],
                [],
            ]
            stdout = io.StringIO()
            with (
                patch.object(metadata, '__file__', str(script)),
                patch.object(
                    sys, 'argv', ['metadata', '--write', '--as-of', '2026-10-23']
                ),
                patch.object(metadata, 'github', side_effect=replies),
                contextlib.redirect_stdout(stdout),
            ):
                result = metadata.main()
            self.assertEqual(result, 0)
            self.assertIn('Updated 2026-09-22 · `Quiet`', readme.read_text())
            self.assertEqual(
                json.loads(stdout.getvalue())['activity_cells_reconciled'], 1
            )


if __name__ == '__main__':
    unittest.main()
