from textnode import *
from textnode import TextNode, TextType
from convert import extract_markdown_links, split_nodes_link
from copystatic import copy_static, del_public
def main():

    del_public()

    copy_static()

if __name__ == "__main__":
    main()
