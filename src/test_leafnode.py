import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "Just plain text.")
        self.assertEqual(node.to_html(), "Just plain text.")

    def test_leaf_to_html_raises_on_empty_value(self):
        node = LeafNode("span", "")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_raises_on_none_value(self):
        with self.assertRaises(ValueError):
            LeafNode("span", None)

    def test_leaf_to_html_with_multiple_props(self):
        node = LeafNode("img", "alt text", {"src": "image.png", "alt": "alt text"})
        self.assertEqual(node.to_html(), '<img src="image.png" alt="alt text">alt text</img>')  # assuming img is not self-closing

if __name__ == "__main__":
    unittest.main()