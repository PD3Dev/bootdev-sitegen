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

    def test_eq_code(self):
        node3 = TextNode('This contains `code` text.', TextType.PLAIN)
        conv3 = split_nodes_delimiter([node3], '`', TextType.CODE)
        check3 = [
    TextNode('This contains ', TextType.PLAIN),
    TextNode('code', TextType.CODE),
    TextNode(' text.', TextType.PLAIN),
        ]
        self.assertEqual(conv3, check3)

    def test_eq_emptybold(self):
        node4 = TextNode('This contains **** text.', TextType.PLAIN)
        conv4 = split_nodes_delimiter([node4], '**', TextType.BOLD)
        check4 = [
    TextNode('This contains ', TextType.PLAIN),
    TextNode(' text.', TextType.PLAIN),
        ]
        self.assertEqual(conv4, check4)

    def test_exception(self):
        exception_node = TextNode('This contains **bold text.', TextType.PLAIN)
        with self.assertRaises(Exception):
            split_nodes_delimiter([exception_node], '**', TextType.BOLD)

    def test_multi_nodes(self):
        node1 = TextNode('This has some **bold** text.', TextType.PLAIN)
        node2 = TextNode('So does **this** text.', TextType.PLAIN)
        node3 = TextNode('And **THIS** one as well.', TextType.PLAIN)
        node4 = TextNode('This one is the **last** string.', TextType.PLAIN)
        conv = split_nodes_delimiter([node1, node2, node3, node4], '**', TextType.BOLD)
        check = [
            TextNode('This has some ', TextType.PLAIN),
            TextNode('bold', TextType.BOLD),
            TextNode(' text.', TextType.PLAIN),
            TextNode('So does ', TextType.PLAIN),
            TextNode('this', TextType.BOLD),
            TextNode(' text.', TextType.PLAIN),
            TextNode('And ', TextType.PLAIN),
            TextNode('THIS', TextType.BOLD),
            TextNode(' one as well.', TextType.PLAIN),
            TextNode('This one is the ', TextType.PLAIN),
            TextNode('last', TextType.BOLD),
            TextNode(' string.', TextType.PLAIN),
        ]
        self.assertEqual(conv, check)

    def test_eq_bold_multi(self):
        node1 = TextNode('This contains **bold** text and then some **more**.', TextType.PLAIN)
        conv1 = split_nodes_delimiter([node1], '**', TextType.BOLD)
        check1 = [
    TextNode('This contains ', TextType.PLAIN),
    TextNode('bold', TextType.BOLD),
    TextNode(' text and then some ', TextType.PLAIN),
    TextNode('more', TextType.BOLD),
    TextNode('.', TextType.PLAIN),
        ]
        self.assertEqual(conv1, check1)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
    )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.PLAIN),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.PLAIN),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )

if __name__ == "__main__":
    unittest.main()
