import unittest
from html.parser import HTMLParser
from pathlib import Path

PAGE = Path(__file__).resolve().parent.parent / "site" / "index.html"


class _TextOfTags(HTMLParser):
    def __init__(self, tags):
        super().__init__()
        self.found = {tag: [] for tag in tags}
        self._open = None

    def handle_starttag(self, tag, attrs):
        if tag in self.found:
            self._open = tag
            self.found[tag].append("")

    def handle_endtag(self, tag):
        if tag == self._open:
            self._open = None

    def handle_data(self, data):
        if self._open:
            self.found[self._open][-1] += data


def _texts_of(*tags):
    parser = _TextOfTags(tags)
    parser.feed(PAGE.read_text(encoding="utf-8"))
    return {tag: [text.strip() for text in texts] for tag, texts in parser.found.items()}


class PageTest(unittest.TestCase):
    def test_has_one_heading_reading_factory_sandbox(self):
        self.assertEqual(_texts_of("h1")["h1"], ["Factory Sandbox"])

    def test_tab_title_stays_sandbox(self):
        self.assertEqual(_texts_of("title")["title"], ["Sandbox"])


if __name__ == "__main__":
    unittest.main()
