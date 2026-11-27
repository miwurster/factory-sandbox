import unittest
from html.parser import HTMLParser
from pathlib import Path

PAGE = Path(__file__).resolve().parent.parent / "site" / "index.html"


class _HeadingCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.headings = []
        self._in_h1 = False

    def handle_starttag(self, tag, attrs):
        if tag == "h1":
            self._in_h1 = True
            self.headings.append("")

    def handle_endtag(self, tag):
        if tag == "h1":
            self._in_h1 = False

    def handle_data(self, data):
        if self._in_h1:
            self.headings[-1] += data


class PageHeadingTest(unittest.TestCase):
    def test_page_has_a_single_factory_sandbox_heading(self):
        collector = _HeadingCollector()
        collector.feed(PAGE.read_text(encoding="utf-8"))
        self.assertEqual([h.strip() for h in collector.headings], ["Factory Sandbox"])


if __name__ == "__main__":
    unittest.main()
