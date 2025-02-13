from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

def main():
    dummy_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(dummy_node)



main()