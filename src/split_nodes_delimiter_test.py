import unittest
from convert import *

class TestDelimiterSplit(unittest.TestCase):
    def test_eq_bold(self):
        node1 = TextNode('This contains **bold** text.', TextType.PLAIN)
        conv1 = split_nodes_delimiter([node1], '**', TextType.BOLD)
        check1 = [
    TextNode('This contains ', TextType.PLAIN),
    TextNode('bold', TextType.BOLD),
    TextNode(' text.', TextType.PLAIN),
        ]
        self.assertEqual(conv1, check1)

    def test_eq_italic(self):
        node2 = TextNode('This contains _italic_ text.', TextType.PLAIN)
        conv2 = split_nodes_delimiter([node2], '_', TextType.ITALIC)
        check2 = [
    TextNode('This contains ', TextType.PLAIN),
    TextNode('italic', TextType.ITALIC),
    TextNode(' text.', TextType.PLAIN),
        ]
        self.assertEqual(conv2, check2)


if __name__ == "__main__":
    unittest.main()
