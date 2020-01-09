from delivery.responses.base_api_response import BaseApiResponse
from delivery.models.content_item import ContentItem

import json

class DeliveryItemListingResponse(BaseApiResponse):
    def __init__(self, base_api_response):
        super().__init__(base_api_response.content, base_api_response.headers, base_api_response.request_url)       

    async def create_content_item_array(self, delivery_items_response):
        delivery_items_response = delivery_items_response.content
        items = []

        for item in delivery_items_response['items']:      
            content_item = ContentItem(item)
            items.append(content_item)
        return items