import unittest
from html.parser import HTMLParser
from pathlib import Path

PAGE = Path(__file__).resolve().parent.parent / "site" / "index.html"


class _TextOfTag(HTMLParser):
    def __init__(self, tag):
        super().__init__()
        self.tag = tag
        self.found = []
        self._open = False

    def handle_starttag(self, tag, attrs):
        if tag == self.tag:
            self._open = True
            self.found.append("")

    def handle_endtag(self, tag):
        if tag == self.tag:
            self._open = False

    def handle_data(self, data):
        if self._open:
            self.found[-1] += data


def _texts_of(tag):
    parser = _TextOfTag(tag)
    parser.feed(PAGE.read_text(encoding="utf-8"))
    return [text.strip() for text in parser.found]


class PageTest(unittest.TestCase):
    def test_has_one_heading_reading_factory_sandbox(self):
        self.assertEqual(_texts_of("h1"), ["Factory Sandbox"])

    def test_tab_title_stays_sandbox(self):
        self.assertEqual(_texts_of("title"), ["Sandbox"])


if __name__ == "__main__":
    unittest.main()
