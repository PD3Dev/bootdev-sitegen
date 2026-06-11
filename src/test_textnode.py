import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_uneq(self):
        node3 = TextNode("This is a link node", TextType.LINK, "https://gidf.de")
        node4 = TextNode("This is a link node", TextType.LINK, None)
        self.assertNotEqual(node3, node4)

        node5 = TextNode("This is a link node", TextType.LINK, "https://gidf.de")
        node6 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node5, node6)

    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("", TextType.IMAGE, "https://boot.dev/logo.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {'src': 'https://boot.dev/logo.png', 'alt': ''})

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {'href': 'https://google.com'})

if __name__ == "__main__":
    unittest.main()
