import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq2(self):
        node1 = TextNode("New Node", TextType.CODE, "http://")
        node2 = TextNode("New Node", TextType.CODE, "http://")
        self.assertEqual(node1, node2)
    
    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node2", TextType.NORMAL)
        self.assertNotEqual(node, node2)
    
    def test_not_eq(self):
        node1 = TextNode("New Node", TextType.CODE, "http://")
        node2 = TextNode("New Node", TextType.CODE )
        self.assertNotEqual(node1, node2)
    
    def test_not_eq_url(self):
        node1 = TextNode("New Node", TextType.CODE, "http://")
        node2 = TextNode("New Node", TextType.LINK, "http://")
        self.assertNotEqual(node1, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.NORMAL, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, normal, https://www.boot.dev)", repr(node)
        )  

"""     def test_node_to_html_node_normal(self):
        text_node = TextNode("Normal text", TextType.NORMAL, None)
        self.assertEqual(text_node.text_node_to_html_node(self), "Normal text") """

class TestTextNodetoHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is text", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is text")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"href": "https://www.example.com", "alt": "This is an image"},
        )

if __name__ == "__main__":
    unittest.main()