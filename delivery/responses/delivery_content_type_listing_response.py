from delivery.responses.base_api_response import BaseApiResponse
from delivery.models.content_type import ContentType

class DeliveryContentTypeListingResponse(BaseApiResponse):
    def __init__(self, base_api_response):
        super().__init__(base_api_response.content, base_api_response.headers, base_api_response.request_url)       

    async def create_content_type_array(self, delivery_types_response):
            delivery_types_response = delivery_types_response.content
            content_types = []

            for content_type in delivery_types_response['types']:      
                content_type = ContentType(content_type)
                content_types.append(content_type)
            return content_types