from delivery.responses.base_api_response import BaseApiResponse
from delivery.models.taxonomy_group import TaxonomyGroup

class DeliveryTaxonomyListingResponse(BaseApiResponse):
    def __init__(self, base_api_response):
        super().__init__(base_api_response.content, base_api_response.headers, base_api_response.request_url)       

    async def create_taxonomy_array(self, delivery_taxonomy_listing_response):
        delivery_taxonomy_listing_response = delivery_taxonomy_listing_response.content
        taxonomies = []

        for taxonomy in delivery_taxonomy_listing_response['taxonomies']:      
            taxonomy_group = TaxonomyGroup(taxonomy)
            taxonomies.append(taxonomy_group)

        return taxonomies