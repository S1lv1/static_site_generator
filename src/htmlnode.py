class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented yet")

    def props_to_html(self):
        if self.props is None:
            return ""
        text = ""
        for prop in self.props:
            text += f' {prop}="{self.props[prop]}"'
        return text
    
    def __eq__(Node1, Node2):
        if( Node1.tag == Node2.tag and
            Node1.value == Node2.value and
            Node1.children == Node2.children and
            Node1.props == Node2.props
            ):
            return True 

    def __repr__(self):
        return f"HTMLNode {self.tag}, {self.value}, children: {self.children}, {self.props}"