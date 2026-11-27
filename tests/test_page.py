import unittest
from html.parser import HTMLParser
from pathlib import Path

PAGE = Path(__file__).resolve().parent.parent / "site" / "index.html"


class _TextByTag(HTMLParser):
    def __init__(self, tags):
        super().__init__()
        self.texts = {tag: [] for tag in tags}
        self._open = None

    def handle_starttag(self, tag, attrs):
        if tag in self.texts:
            self._open = tag
            self.texts[tag].append("")

    def handle_endtag(self, tag):
        if tag == self._open:
            self._open = None

    def handle_data(self, data):
        if self._open:
            self.texts[self._open][-1] += data


def _page_texts():
    parser = _TextByTag(["h1", "title"])
    parser.feed(PAGE.read_text(encoding="utf-8"))
    return {tag: [text.strip() for text in texts] for tag, texts in parser.texts.items()}


class PageTest(unittest.TestCase):
    def test_page_has_one_heading_reading_factory_sandbox(self):
        self.assertEqual(_page_texts()["h1"], ["Factory Sandbox"])

    def test_tab_title_reads_sandbox(self):
        self.assertEqual(_page_texts()["title"], ["Sandbox"])


if __name__ == "__main__":
    unittest.main()
