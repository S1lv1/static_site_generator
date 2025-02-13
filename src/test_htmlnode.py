import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(None, None,)
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = HTMLNode("p", "Hello")
        node2 = HTMLNode("p", "Hello")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode("p", "Hello")
        node2 = HTMLNode("h1", "ref")
        self.assertNotEqual(node,node2)

    def test_to_html(self):
        node = HTMLNode(
            "div",
            "Hello",
            None,
            {"class": "default", "href": "https://example.com"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="default" href="https://example.com"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "Welcome, Welcome",
            None,
            {"class": "secondary"}
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode p, Welcome, Welcome, children: None, {'class': 'secondary'}",
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, weird world!")
        self.assertEqual(node.to_html(), "<p>Hello, weird world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, weird world!")
        self.assertEqual(node.to_html(), "Hello, weird world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("p", [child_node])
        self.assertEqual(parent_node.to_html(), "<p><span>child</span></p>")
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandkid")
        child_node = ParentNode("h2", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><h2><b>grandkid</b></h2></div>")

    def test_to_html_with_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("i", "italic child"),
                LeafNode(None, "test"),
                LeafNode("b", "bold child")
            ],    
        )
        self.assertEqual(node.to_html(), "<p><i>italic child</i>test<b>bold child</b></p>")

    de
if __name__ == "__main__":
    unittest.main()