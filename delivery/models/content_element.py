class ContentElement:
    def __init__(self, element_codename, element_value):
        self.codename = element_codename
        self.name = element_value['name']
        self.type = element_value['type']