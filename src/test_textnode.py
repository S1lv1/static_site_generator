import unittest

from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()