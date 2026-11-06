"""Checks which built page each changed source file maps to."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_previews import map_source  # noqa: E402


class MapSourceTest(unittest.TestCase):
    def test_mdbook(self):
        self.assertEqual(map_source('src/guides/Guide_to_Boats.md', 'mdbook'), 'guides/Guide_to_Boats.html')
        self.assertEqual(map_source('src/SUMMARY.md', 'mdbook'), '')
        self.assertEqual(map_source('theme/compiled/admonish.css', 'mdbook'), '')
        self.assertIsNone(map_source('src/images/maps/x.png', 'mdbook'))
        self.assertIsNone(map_source('scripts/build.py', 'mdbook'))


if __name__ == '__main__':
    unittest.main()
