import unittest
from textnode import TextNode, TextType

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


if __name__ == "__main__":
    unittest.main()