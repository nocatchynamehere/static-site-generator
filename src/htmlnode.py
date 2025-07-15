class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
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