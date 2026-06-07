
class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
            raise NotImplementedError

    def props_to_html(self):
        if self.props is not None:
            keys = sorted(list(self.props))
            prop_str = ""

            for key in keys:
                prop_str += f'{key}="{self.props[key]}" '
            return prop_str
        else:
            return None

    def __repr__(self):
            print(f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})')

    def __eq__(self, other):
        if (self.tag == other.tag
            and
            self.value == other.value
            and
            self.children == other.children
            and
            self.props == other.props):
            return True

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
         super().__init__(tag, value, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return str(self.value)
        
        return f'<{self.tag}>{self.value}</{self.tag}>'
    
    def __repr__(self):
         print(f'HTMLNode({self.tag}, {self.value}, {self.props})')
