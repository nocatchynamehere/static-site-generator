class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        strings = ""
        for k, v in self.props.items():
            strings += f' {k}="{v}"'
        return strings
    
    def __repr__(self):
        return (
        f"HTMLNode(tag={self.tag!r}, value={self.value!r}, "
        f"children={self.children!r}, props={self.props!r})"
    )

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag=tag, value=value, props=props, children=None)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError("LeafNode must have a non-empty value.")
        
        if self.tag is None:
            return self.value
        
        props_str = self.props_to_html() if self.props else ""
        return f'<{self.tag}{props_str}>{self.value}</{self.tag}>'
    
class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict = None):
        super().__init__(tag=tag, children=children, props = props)
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if not isinstance(self.children, list) or not self.children:
            raise ValueError("ParentNode must have children")
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: ParentNode must have a tag")
        if not isinstance(self.children, list) or not self.children:
            raise ValueError("Invalid HTML: ParentNode must have children")
        
        children_html_content = ""
        for child in self.children:
            children_html_content += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{children_html_content}</{self.tag}>"
    
    def __repr__(self):
        return (
            f'ParentNode(tag={self.tag}, children={self.children}, props={self.props})'
        )