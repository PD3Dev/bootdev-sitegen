from enum import Enum

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
        return print(f'TextNode({self.text}, {self.text_type.value}, {self.url}')
