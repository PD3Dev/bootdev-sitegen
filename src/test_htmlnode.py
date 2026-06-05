from htmlnode import *
import unittest

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a value text")
        node2 = HTMLNode("p", "This is a value text")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()

