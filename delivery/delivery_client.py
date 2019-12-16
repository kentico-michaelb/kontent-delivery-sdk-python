import requests
from delivery.builders.url_builder import UrlBuilder
from delivery.responses.base_api_response import BaseApiResponse
from delivery.responses.delivery_item_response import DeliveryItemResponse
from delivery.responses.delivery_item_listing_response import DeliveryItemListingResponse

class DeliveryClient: 
    def __init__(self, delivery_options):
        self.project_id = delivery_options.project_id        
        self.use_preview = delivery_options.use_preview
        self.preview_api_key = delivery_options.preview_api_key
        self.secured_api_key = delivery_options.secured_api_key

        self.url_builder = UrlBuilder(delivery_options.project_id, delivery_options.use_preview)


    def get_item_response(self, codename):
        url = self.url_builder.get_item_url(codename)
        api_response = self.send_http_request(url)

        delivery_item_response = DeliveryItemResponse(api_response)

        return delivery_item_response

    def get_item(self, codename):
        url = self.url_builder.get_item_url(codename)
        api_response = self.send_http_request(url)

        delivery_item_response = DeliveryItemResponse(api_response)        

        content_item = delivery_item_response.cast_to_content_item(delivery_item_response)        

        return content_item

    def get_items(self,*args):
        url = self.url_builder.get_items_url(args)
        api_response = self.send_http_request(url)

        delivery_items_response = DeliveryItemListingResponse(api_response)

        content_items = delivery_items_response.create_content_item_array(delivery_items_response)

        return content_items    

    def send_http_request(self, request_url):
        headers = None        
        if self.use_preview:
            headers = {"Authorization": "Bearer {}".format(self.preview_api_key)}
        
        response = requests.get(request_url, headers=headers)
        response.raise_for_status()

        if response.status_code == 200:
            api_response = self.set_base_api_response(request_url, response, response.headers)        
            return api_response

        return response.status_code

    def set_base_api_response(self, url, response, headers):
        base_api_response = BaseApiResponse(response.json(), response.headers, url)
        return base_api_response



