import configparser

class DeliveryOptions():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.project_id = self.get_options(config, 'project_id')
        self.use_preview = self.get_options(config, 'use_preview')
        self.preview_api_key = self.get_options(config, 'preview_api_key')
        self.secured_api_key = self.get_options(config, 'secured_api_key')
        self.use_inline_item_resolver = self.get_options(config, 'use_inline_item_resolver')
        self.custom_inline_resolver = None
        self.custom_link_resolver = None

    def get_options(self, config, option_name, option_section = 'delivery_options'):
        try:
            return config.get(option_section,option_name)
        except:
            return None

    def with_inline_resolver(self, custom_inline_resolver):
        self.custom_inline_resolver = custom_inline_resolver

    def with_link_resolver(self, custom_link_resolver):
        self.custom_link_resolver = custom_link_resolver
        

