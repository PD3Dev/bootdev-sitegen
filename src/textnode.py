from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    PLAIN = "Plain"
    BOLD = "Bold"
    ITALIC = "Italic"
    CODE = "Code"
    LINK = "Link"
    IMAGE = "Image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        ## Text content of the node
        self.text = text
        ## Member of TextType Enum. Contains the text type of the node.
        self.text_type = text_type
        ## URL or link or image. Default == None
        self.url = url

    def __eq__(self, other):
        if (self.text == other.text
            and
            self.text_type == other.text_type
            and
                self.url == other.url):
            return True

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type.value}, {self.url}'

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == TextType.PLAIN:
        return LeafNode(None, text_node.text)
    
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)

    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)

    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {'href': f'{text_node.url}'})

    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)

    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {'src': f'{text_node.url}', 'alt': f'{text_node.text}'})

    else:
        raise Exception("Unsupported Text Type")
