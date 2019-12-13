import configparser

class DeliveryOptions():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.project_id = self.get_options(config, 'project_id')
        self.use_preview = self.get_options(config, 'use_preview')
        self.preview_api_key = self.get_options(config, 'preview_api_key')
        self.secured_api_key = self.get_options(config, 'secured_api_key')

        # self.content_link_resolver = config.get(delivery_options_section,'project_id')
        # self.inline_content_resolver = config.get(delivery_options_section,'project_id')


    def get_options(self, config, option_name, option_section = 'delivery_options'):
        try:
            return config.get(option_section,option_name)
        except:
            return None

