import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        link1 = TextNode("This is a link node", TextType.LINK)
        link2 = TextNode("This is a link node", TextType.LINK, None)
        self.assertEqual(link1, link2)

    def test_uneq(self):
        node3 = TextNode("This is a link node", TextType.LINK, "https://gidf.de")
        node4 = TextNode("This is a link node", TextType.LINK, None)
        self.assertNotEqual(node3, node4)

        node5 = TextNode("This is a link node", TextType.LINK, "https://gidf.de")
        node6 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node5, node6)

        plain1 = TextNode("This is a text node", TextType.PLAIN)
        plain2 = TextNode("This is a plain text node", TextType.PLAIN)
        self.assertNotEqual(plain1, plain2)

        nocap = TextNode("This is a text node", TextType.PLAIN)
        cap = TextNode("THIS IS A TEXT NODE", TextType.PLAIN)
        self.assertNotEqual(nocap, cap)

if __name__ == "__main__":
    unittest.main()
