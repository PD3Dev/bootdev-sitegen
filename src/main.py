from textnode import *
def main():
    testnode = TextNode('This is some anchor text', TextType.link, 'https://www.boot.dev')

    print(f'TextNode({testnode.text}, {testnode.text_type.value}, {testnode.url})')

if __name__ == "__main__":
    main()
