from htmlnode import *
import unittest

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        htmlnode = HTMLNode("p", "This is a value text")
        htmlnode2 = HTMLNode("p", "This is a value text")
        self.assertEqual(htmlnode, htmlnode2)
        htmlnode5 = HTMLNode("p", "This is a value text")
        htmlnode6 = HTMLNode("p", "This is a value text", None, None)
        self.assertEqual(htmlnode5, htmlnode6)

    def test_uneq(self):
        child1 = HTMLNode("a", "text")
        child2 = HTMLNode("a", "diff text")
        htmlnode3 = HTMLNode("i", "some text", [child1], {"href": "google.de"})
        htmlnode4 = HTMLNode("i", "some text", [child2], {"href": "google.de"})
        self.assertNotEqual(htmlnode3, htmlnode4)

    def test_proptohtml(self):
        htmlnode7 = HTMLNode("i", "some text", None, {"href": "google.de"})
        test_str = htmlnode7.props_to_html()
        ctrl_str = 'href="google.de" '
        self.assertEqual(test_str, ctrl_str)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node2 = LeafNode("a", "Hello, world!", {"href": "google.de"})
        self.assertEqual(node2.to_html(), "<a>Hello, world!</a>")

if __name__ == "__main__":
    unittest.main()

