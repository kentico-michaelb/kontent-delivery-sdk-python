from delivery.models.content_element import ContentElement
from delivery.models.multiple_choice_element import MultipleChoiceElement

class ContentType:
    def __init__(self, delivery_content_type_response):
        content_type = delivery_content_type_response
        self.system = content_type['system']          
        self.id = self.system['id']
        self.name = self.system['name']
        self.codename = self.system['codename']
        self.elements = self.get_elements(content_type['elements'])

    def get_elements(self, elements):
        typed_elements = []
        for element_codename, element_value in elements.items():
            if element_value['type'] == 'multiple_choice':
                content_element = MultipleChoiceElement(element_codename, element_value)
                typed_elements.append(content_element)
            else:
                content_element = ContentElement(element_codename, element_value)
                typed_elements.append(content_element)
        return typed_elements




