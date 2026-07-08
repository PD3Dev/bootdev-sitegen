from textnode import *
from textnode import TextNode, TextType
from convert import extract_markdown_links, generate_page, generate_pages_recursive, split_nodes_link
from copystatic import copy_static, del_public
def main():

    del_public()

    copy_static('static/', 'public/')

    generate_pages_recursive('content', 'template.html', 'public')

if __name__ == "__main__":
    main()
