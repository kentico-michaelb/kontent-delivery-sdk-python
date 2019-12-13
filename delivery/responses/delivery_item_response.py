from delivery.responses.base_api_response import BaseApiResponse
from delivery.models.content_item import ContentItem

import json

class DeliveryItemResponse(BaseApiResponse):
    def __init__(self, base_api_response):
        super().__init__(base_api_response.content, base_api_response.headers, base_api_response.request_url)       

    def cast_to_content_item(self, delivery_item_response):
        delivery_item_response = delivery_item_response.content
        content_item = ContentItem(delivery_item_response['item'], delivery_item_response['modular_content'])
        return content_item