class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, comparison):
        equality = False
        if self.text == comparison.text:
            equality = True
        else:
            return False
        if self.text_type == comparison.text_type:
            equality = True
        else:
            return False
        if self.url == comparison.url:
            equality = True
        else:
            return False
        return equality
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"