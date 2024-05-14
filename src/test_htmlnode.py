import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_correct_formatting(self):
        node = HTMLNode(props={"href": "https://boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://boot.dev" target="_blank"')

    def test_empty_dictionary(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()