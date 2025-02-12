import unittest

from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()