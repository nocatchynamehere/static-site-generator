import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_basic_parent_node(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected_html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_with_single_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        expected_html = "<div><span>child</span></div>"
        self.assertEqual(parent_node.to_html(), expected_html)

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        expected_html = "<div><span><b>grandchild</b></span></div>"
        self.assertEqual(parent_node.to_html(), expected_html)

    def test_to_html_with_props(self):
        child_node = LeafNode("a", "Click me", {"href": "#"})
        parent_node = ParentNode("div", [child_node], {"class": "container", "id": "main"})
        expected_html = '<div class="container" id="main"><a href="#">Click me</a></div>'
        self.assertEqual(parent_node.to_html(), expected_html)

    def test_no_children_error(self):
        with self.assertRaisesRegex(ValueError, "ParentNode must have children"):
            ParentNode("div", [])

    def test_children_is_none_error(self):
        with self.assertRaisesRegex(ValueError, "ParentNode must have children"):
            ParentNode("div", None)

    def test_tag_is_none_error(self):
        with self.assertRaisesRegex(ValueError, "ParentNode must have a tag"):
            ParentNode(None, [LeafNode("p", "text")])

    def test_complex_nesting(self):
        node = ParentNode(
            "div",
            [
                LeafNode("h1", "Welcome"),
                ParentNode(
                    "ul",
                    [
                        LeafNode("li", "Item 1"),
                        LeafNode("li", "Item 2"),
                        ParentNode(
                            "li",
                            [
                                LeafNode("span", "Nested"),
                                LeafNode("b", "Bold Nested"),
                            ]
                        ),
                    ]
                ),
                LeafNode("p", "End of content."),
            ],
            {"id": "main-container"}
        )
        expected_html = '<div id="main-container"><h1>Welcome</h1><ul><li>Item 1</li><li>Item 2</li><li><span>Nested</span><b>Bold Nested</b></li></ul><p>End of content.</p></div>'
        self.assertEqual(node.to_html(), expected_html)

    def test_empty_props_dict(self):
        child_node = LeafNode("span", "no props child")
        parent_node = ParentNode("div", [child_node], {})
        expected_html = "<div><span>no props child</span></div>"
        self.assertEqual(parent_node.to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()