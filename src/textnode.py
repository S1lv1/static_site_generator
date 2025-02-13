from enum import Enum
from htmlnode import LeafNode

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



def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception("invalid text type")
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href" : text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"href" : text_node.url, "alt" : text_node.text })



