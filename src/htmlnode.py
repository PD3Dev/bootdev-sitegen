
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
                prop_str += f' {key}="{self.props[key]}"'
            return prop_str
        else:
            return ''

    def __repr__(self):
            return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'

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
         super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("No content found")
        if self.tag == None:
            return str(self.value)
        if self.tag == 'img':
            return f'<{self.tag}{self.props_to_html()} />'

        
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
         return f'LeafNode({self.tag}, {self.value}, {self.props})'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
         super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("HTML tag required")
        if self.children == None:
            raise ValueError("No child nodes")
        html_str = f'<{self.tag}{self.props_to_html()}>'

#Iterate over children and add them in between parent's HTML tag
        for child in self.children:
            html_str += child.to_html()
        html_str += f'</{self.tag}>'
        return html_str
