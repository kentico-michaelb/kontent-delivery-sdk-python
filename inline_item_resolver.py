from delivery.resolvers.inline_content_item_resolver import InlineContentResolver

class CustomInlineContentResolver(InlineContentResolver):
    def resolve_item(self, item_to_resolve):
        if item_to_resolve.type == 'article':
            return '<h1>item name: {0}</h1><p> summary: {1}</p>'.format(item_to_resolve.name, item_to_resolve.get_element_value('summary'))
        elif item_to_resolve.type == 'hosted_video':
            return '<h1>component name: {0}</h1><p> video id: {1}</p>'.format(item_to_resolve.name, item_to_resolve.get_element_value('video_id'))            
        else:
            return 'Custom resolver not set for type: {}'.format(item_to_resolve.type)