import asyncio
import aiohttp

from delivery.builders.url_builder import UrlBuilder
from delivery.responses.base_api_response import BaseApiResponse
from delivery.responses.delivery_item_response import DeliveryItemResponse
from delivery.responses.delivery_item_listing_response import DeliveryItemListingResponse
from delivery.responses.delivery_content_type_response import DeliveryContentTypeResponse
from delivery.responses.delivery_content_type_listing_response import DeliveryContentTypeListingResponse
from delivery.responses.delivery_taxonomy_response import DeliveryTaxonomyResponse
from delivery.responses.delivery_taxonomy_listing_response import DeliveryTaxonomyListingResponse

class DeliveryClient: 
    def __init__(self, delivery_options):
        self.project_id = delivery_options.project_id        
        self.use_preview = delivery_options.use_preview
        self.preview_api_key = delivery_options.preview_api_key
        self.secured_api_key = delivery_options.secured_api_key
        self.use_inline_item_resolver = delivery_options.use_inline_item_resolver
        self.url_builder = UrlBuilder(delivery_options.project_id, delivery_options.use_preview)
        self.custom_inline_resolver = delivery_options.custom_inline_resolver
        self.custom_link_resolver = delivery_options.custom_link_resolver
        

    async def get_item(self, codename, *args):
        url = self.url_builder.get_item_url(codename, args)
        result = await self.build_client_session(self.set_delivery_item_response, url)        

        return result

    async def get_items(self,*args):
        url = self.url_builder.get_items_url(args)
        result = await self.build_client_session(self.set_delivery_listing_response, url)        

        return result

    async def get_content_type(self, codename):
        url = self.url_builder.get_content_type_url(codename)
        result = await self.build_client_session(self.set_delivery_content_type_response, url)

        return result

    async def get_content_types(self):
        url = self.url_builder.get_content_types_url()
        result = await self.build_client_session(self.set_delivery_content_type_listing_response, url)

        return result

    async def get_taxonomy(self, codename):
        url = self.url_builder.get_taxonomy_url(codename)
        result = await self.build_client_session(self.set_delivery_taxonomy_response, url)
        

        return result 

    async def get_taxonomies(self):
        url = self.url_builder.get_taxonomies_url()
        print(url)
        result = await self.build_client_session(self.set_delivery_taxonomy_listing_response, url)

        return result        


    async def send_http_request(self, request_url, session):
        headers = None        
        if self.use_preview:
            headers = {f"Authorization": "Bearer {self.preview_api_key}"}
        
        async with session.get(request_url, headers=headers) as response:
            api_response = await self.set_base_api_response(request_url, response, response.headers)
            return api_response   

        return response.status

    async def set_base_api_response(self, url, response, headers):
        base_api_response = BaseApiResponse(await response.json(), headers, url)
        return base_api_response

    async def set_delivery_item_response(self, url, session):
        delivery_item_response = DeliveryItemResponse(await self.send_http_request(url, session))
        content_item = await delivery_item_response.cast_to_content_item(delivery_item_response, self.custom_inline_resolver, self.custom_link_resolver, self.use_inline_item_resolver)        
        
        return content_item

    async def set_delivery_listing_response(self, url, session):
        delivery_items_response = DeliveryItemListingResponse(await self.send_http_request(url, session))
        content_items = await delivery_items_response.create_content_item_array(delivery_items_response, self.custom_inline_resolver, self.custom_link_resolver, self.use_inline_item_resolver)
        
        return content_items

    async def set_delivery_content_type_response(self, url, session):
        delivery_content_type_response = DeliveryContentTypeResponse(await self.send_http_request(url, session))
        content_type = await delivery_content_type_response.cast_to_content_type(delivery_content_type_response)        
        
        return content_type

    async def set_delivery_content_type_listing_response(self, url, session):
        delivery_content_type_listing_response = DeliveryContentTypeListingResponse(await self.send_http_request(url, session))
        content_types = await delivery_content_type_listing_response.create_content_type_array(delivery_content_type_listing_response)        
        
        return content_types

    async def set_delivery_taxonomy_response(self, url, session):
        delivery_taxonomy_response = DeliveryTaxonomyResponse(await self.send_http_request(url, session))
        taxonomy = await delivery_taxonomy_response.cast_to_taxonomy_group(delivery_taxonomy_response)        
        
        return taxonomy 

    async def set_delivery_taxonomy_listing_response(self, url, session):
        delivery_taxonomy_listing_response = DeliveryTaxonomyListingResponse(await self.send_http_request(url, session))
        taxonomies = await delivery_taxonomy_listing_response.create_taxonomy_array(delivery_taxonomy_listing_response)        
        
        return taxonomies                  


    async def build_client_session(self, method, url):
        tasks = []
        async with aiohttp.ClientSession() as session:
            task = asyncio.ensure_future(method(url, session))    
            tasks.append(task) 
            result = await asyncio.gather(*tasks)                       
            
            return result[0]

