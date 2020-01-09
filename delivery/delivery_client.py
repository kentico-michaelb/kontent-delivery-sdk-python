import asyncio
import aiohttp

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
        self.use_inline_item_resolver = delivery_options.use_inline_item_resolver
        self.custom_inline_resolver = delivery_options.custom_inline_resolver
        self.custom_link_resolver = delivery_options.custom_link_resolver

        self.url_builder = UrlBuilder(delivery_options.project_id, delivery_options.use_preview)

    async def get_item(self, codename):
        url = self.url_builder.get_item_url(codename)

        tasks = []
        async with aiohttp.ClientSession() as session:
            task = asyncio.ensure_future(self.set_delivery_item_response(url, session))    
            tasks.append(task) 
            result = await asyncio.gather(*tasks)                       
            
            return result[0]

    async def get_items(self,*args):
        url = self.url_builder.get_items_url(args)
        print(url)
        tasks = []
        async with aiohttp.ClientSession() as session:
            task = asyncio.ensure_future(self.set_delivery_listing_response(url, session))    
            tasks.append(task) 
            result = await asyncio.gather(*tasks)      
            
            return result[0]

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
        content_items = await delivery_items_response.create_content_item_array(delivery_items_response)
        
        return content_items


