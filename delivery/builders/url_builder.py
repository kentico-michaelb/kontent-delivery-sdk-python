class UrlBuilder:
    def __init__(self, project_id, use_preview):
        self.url_max_length = 65519
        self.url_template_item = '/items/{0}'
        self.url_template_items = '/items'
        self.url_template_items_feed = '/items-feed'
        self.url_template_type = '/types/{0}'
        self.url_template_types = '/types'
        self.url_template_element = '/types/{0}/elements/{1}'
        self.url_template_taxonomy = '/taxonomies/{0}'
        self.url_template_taxonomies = '/taxonomies'

        if use_preview == 'True':
            self.endpoint_url = f'https://preview-deliver.kontent.ai/{project_id}'          
        else:
            self.endpoint_url = f'https://deliver.kontent.ai/{project_id}'

    def get_item_url(self, codename):
        url = self.endpoint_url 
        url += self.url_template_item.format(codename)

        return url

    def get_items_url(self,*args):
        url = self.endpoint_url 
        url += self.url_template_items

        for count, arg in enumerate(*args):
            if count == 0:
                url += f'?{arg.query_string}'             
            else:
                url += f'&{arg.query_string}' 
                            
        return url

    def get_content_type_url(self, codename):
        url = self.endpoint_url 
        url += self.url_template_type.format(codename)

        return url

    def get_content_types_url(self):
        url = self.endpoint_url 
        url += self.url_template_types

        return url
