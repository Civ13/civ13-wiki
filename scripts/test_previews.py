"""Regression tests for raw-text safety, fallbacks, and invalid component limits."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from check_preview import HeadParser, check_html, validate_payload
from previews import MARKER, generate, metadata, serialize


class PreviewsTest(unittest.TestCase):
    def setUp(self):
        self.head = metadata('Quotes " & café </ScRiPt>', '日本語 <tag> & details', 'https://example.com/wiki/chapter.html')
        self.html = '<html><head>' + self.head + '</head><body></body></html>'
        parser = HeadParser()
        parser.feed(self.html)
        self.raw = parser.scripts[0]
        self.payload = json.loads(self.raw)

    def test_serialization_and_fallback(self):
        self.assertEqual(check_html(self.html)[0], [])
        self.assertNotIn('<', self.raw)
        self.assertIn('</ScRiPt>', self.payload['component']['components'][0]['content'])
        fallback = self.html.replace('<script id="discord:component-embed" type="application/json">' + self.raw + '</script>', '')
        parser = HeadParser()
        parser.feed(fallback)
        self.assertEqual(parser.metadata['og:title'], 'Quotes " & café </ScRiPt>')
        self.assertEqual(parser.metadata['twitter:description'], '日本語 <tag> & details')

    def test_reject_invalid_payloads(self):
        self.assertTrue(validate_payload(' ' * 3001)[0])
        variants = []
        nested = copy.deepcopy(self.payload)
        nested['component']['components'].append({'type': 17, 'components': []})
        variants.append(nested)
        many = copy.deepcopy(self.payload)
        many['component']['components'] = [{'type': 10, 'content': 'a'}] * 40
        variants.append(many)
        gallery = copy.deepcopy(self.payload)
        gallery['component']['components'][2]['items'] *= 11
        variants.append(gallery)
        for key in ('custom_id', 'unexpected'):
            button = copy.deepcopy(self.payload)
            button['component']['components'][3]['components'][0][key] = 'bad'
            variants.append(button)
        for payload in variants:
            self.assertTrue(validate_payload(json.dumps(payload).replace('<', '\\u003c'))[0])
        with self.assertRaises(ValueError):
            serialize({'text': '日' * 1001})
        with self.assertRaises(ValueError):
            metadata('title', 'description', 'https://example.com/' + 'x' * 512)

    def test_alternate_base_empty_prose_and_utilities(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            chapter = root / 'nested' / 'café.html'
            chapter.parent.mkdir()
            chapter.write_text('<html><head><title>Empty chapter</title>' + MARKER + '</head><body><main></main></body></html>', encoding='utf-8')
            utility = root / 'print.html'
            utility.write_text('<html><head>' + MARKER + '</head></html>')
            generate(root, 'https://example.com/alternate/')
            source = chapter.read_text(encoding='utf-8')
            self.assertEqual(check_html(source)[0], [])
            self.assertIn('https://example.com/alternate/nested/caf%C3%A9.html', source)
            self.assertNotIn('discord:component-embed', utility.read_text())


if __name__ == '__main__':
    unittest.main()
