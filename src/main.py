from textnode import *
from textnode import TextNode, TextType
from convert import extract_markdown_links, generate_page, generate_pages_recursive, split_nodes_link
from copystatic import copy_static, del_docs
import sys
def main():

    del_docs()

    basepath = '/'
    if sys.argv[1]:
        basepath = sys.argv[1]

    copy_static('static/', 'docs/')

    generate_pages_recursive('content', 'template.html', 'docs/', basepath)

if __name__ == "__main__":
    main()
