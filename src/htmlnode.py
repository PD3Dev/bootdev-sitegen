
class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

        def to_html(self):
            raise NotImplementedError

        def props_to_html(self):
            keys = list(self.props)
            prop_str = ""

            for key in keys:
                prop_str += f'{key}="{self.props[key]}" '
            return prop_str

        def __repr__(self):
            print(f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})')
