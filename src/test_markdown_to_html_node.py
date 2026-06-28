import unittest
from convert import *

class TestMDtoHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_links(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

This is a [link](http://google.de).

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p><p>This is a <a href="http://google.de">link</a>.</p></div>',
        )

    def test_image(self):
        md = """
This is an image ![image](http://google.de/test.png).
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>This is an image <img alt="image" src="http://google.de/test.png" />.</p></div>',
        )

    def test_image_and_link(self):
        md = """
This is an image ![image](http://google.de/test.png).

And here is a [link](https://google.de).
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>This is an image <img alt="image" src="http://google.de/test.png" />.</p><p>And here is a <a href="https://google.de">link</a>.</p></div>',
        )

if __name__ == '__main__':
    unittest.main()
