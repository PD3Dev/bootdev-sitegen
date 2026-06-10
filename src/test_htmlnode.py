from htmlnode import *
import unittest

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        htmlnode = HTMLNode("p", "This is a value text")
        htmlnode2 = HTMLNode("p", "This is a value text")
        self.assertEqual(htmlnode, htmlnode2)

    def test_eq_none_values(self):
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

    def test_leaf_to_html_p_w_link(self):
        node2 = LeafNode("a", "Hello, world!", {"href": "google.de"})
        self.assertEqual(node2.to_html(), "<a>Hello, world!</a>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_greatgrandchildren(self):
        greatgrandchild_node = LeafNode("i", "greatgrandchild")
        grandchild_node = ParentNode("b", [greatgrandchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b><i>greatgrandchild</i></b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()

