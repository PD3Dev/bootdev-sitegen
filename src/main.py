from textnode import *
from textnode import TextNode, TextType
from convert import extract_markdown_links, split_nodes_link
def main():
    testnode = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')

    print(f'TextNode({testnode.text}, {testnode.text_type.value}, {testnode.url})')

    link_node = TextNode("link", TextType.LINK, "http://google.de")
    leaf = text_node_to_html_node(link_node)
    print(repr(leaf))
    print(leaf.to_html())

if __name__ == "__main__":
    main()
