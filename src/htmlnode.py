class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        # String representing the HTML tag name
        self.tag = tag

        # String representing the value of the HTML Tag
        self.value = value

        # List of HTMLNode objects representing the children of this node
        self.children = children

        # Dictionary of key-value pairs representing the attributes of the 
        self.props = props


    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        extracted_props = ""
        if self.props is None:
            return ""
        for key in self.props:
            key_value = ""
            if extracted_props != "":
              key_value += " "  
            key_value += f'{key}="{self.props[key]}"'
            extracted_props += key_value
        return extracted_props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
   
        super().__init__(tag, value, None, props)

    def to_html(self):
        extracted = self.props_to_html()

        if self.value == None:
            raise ValueError
        
        if self.tag == None:
            return f'{self.value}'

        if self.props == None:
            return f'<{self.tag}>{self.value}</{self.tag}'
        
        else:
            return f'<{self.tag} {extracted}>{self.value}</{self.tag}>'

