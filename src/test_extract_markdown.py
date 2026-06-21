import unittest
from convert import *

class TestExtractMarkdown(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
        "This is text with an ![link](https://i.imgur.com/zjjcJKZ.png)"
    )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_invalid(self):
        with self.assertRaises(Exception):
            extract_markdown_links(
        "This is text with an ![link](https://i.imgur.com/zjjcJKZ.png) and an incomplete [link2]"
    )



if __name__ == "__main__":
    unittest.main()
