from delivery.models.content_element import ContentElement
from delivery.models.multiple_choice_option import MultipleChoiceOption

class MultipleChoiceElement(ContentElement):
    def __init__(self, element_codename, element_value):
        super().__init__(element_codename, element_value)
        self.options = self.get_options(element_value['options'])

    def get_options(self, options):
        typed_options = []
        for option in options:
            typed_option = MultipleChoiceOption(option)
            typed_options.append(typed_option)
            
        return typed_options