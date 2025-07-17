import unittest
from textnode import TextNode, TextType, Enum, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.ITALIC)
        node4 = TextNode("This is a text node", TextType.BOLD, "boot.dev/dashboard")
        node5 = TextNode("This is a text node", TextType.BOLD, "boot.dev/courses")
        node6 = TextNode("This is a text node", TextType.ITALIC)
        node7 = TextNode("This is a text node", TextType.BOLD, "boot.dev/dashboard")
        node8 = TextNode("This is a different text node", TextType.BOLD)


        self.assertEqual(node, node2)
        self.assertEqual(node3, node6)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node4, node)
        self.assertNotEqual(node4, node5)
        self.assertNotEqual(node, node8)
        self.assertEqual(node4, node7)

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_type_text(self):
        node = TextNode("plain text", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "plain text")
        self.assertEqual(html_node.props, None)

    def test_text_type_bold(self):
        node = TextNode("bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "bold text")
        self.assertEqual(html_node.props, None)

    def test_text_type_italic(self):
        node = TextNode("italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "italic text")
        self.assertEqual(html_node.props, None)

    def test_text_type_code(self):
        node = TextNode("print('Hello')", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('Hello')")
        self.assertEqual(html_node.props, None)

    def test_text_type_link(self):
        node = TextNode("Visit site", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Visit site")
        self.assertEqual(html_node.props, {"href": "https://example.com"})

    def test_text_type_image(self):
        node = TextNode("An image", TextType.IMAGE, "https://example.com/img.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {
            "src": "https://example.com/img.png",
            "alt": "An image"
        })

    def test_invalid_type_raises(self):
        class FakeType(Enum):
            BAD = "bad"

        node = TextNode("bad", FakeType.BAD)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()