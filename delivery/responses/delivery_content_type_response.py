from delivery.responses.base_api_response import BaseApiResponse
from delivery.models.content_type import ContentType

import json

class DeliveryContentTypeResponse(BaseApiResponse):
    def __init__(self, base_api_response):
        super().__init__(base_api_response.content, base_api_response.headers, base_api_response.request_url)       

    async def cast_to_content_type(self, delivery_content_type_response):
        delivery_content_type_response = delivery_content_type_response.content
        content_type = ContentType(delivery_content_type_response)
        
        return content_type