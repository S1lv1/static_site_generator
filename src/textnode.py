from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url 

    def __eq__(Node1, Node2):
        if( Node1.text == Node2.text and
            Node1.text_type == Node2.text_type and
            Node1.url == Node2.url
            ):
            return True 
    def __repr__(TextNode):
        return f"TextNode({TextNode.text}, {TextNode.text_type.value}, {TextNode.url})"

