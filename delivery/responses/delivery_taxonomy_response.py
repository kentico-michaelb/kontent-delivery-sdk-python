from delivery.responses.base_api_response import BaseApiResponse
from delivery.models.taxonomy_group import TaxonomyGroup

class DeliveryTaxonomyResponse(BaseApiResponse):
    def __init__(self, base_api_response):
        super().__init__(base_api_response.content, base_api_response.headers, base_api_response.request_url)       

    async def cast_to_taxonomy_group(self, delivery_taxonomy_response):
        delivery_taxonomy_response = delivery_taxonomy_response.content
        taxonomy = TaxonomyGroup(delivery_taxonomy_response)
        
        return taxonomy