import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single(self):
        node = HTMLNode(tag="a", props={"href": "boot.dev/dashboard"})
        self.assertEqual(node.props_to_html(), ' href="boot.dev/dashboard"')

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p", props={})
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_none(self):
        node = HTMLNode(tag="p")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_multiple(self):
        node = HTMLNode(tag="a", props={
            "href": "boot.dev/dashboard",
            "target": "_blank"
        })
        self.assertEqual(
            node.props_to_html(),
            ' href="boot.dev/dashboard" target="_blank"'
        )

if __name__ == "__main__":
    unittest.main()