from bs4 import BeautifulSoup

class InlineContentResolver:
    def __init__(self):
        pass

    def resolve(self, content, inline_items):
        soup = BeautifulSoup(content, features="html.parser")

        for key, value in inline_items.items(): 
            obj = soup.find("object", attrs={"data-codename":key})            
            if obj:
                from delivery.models.content_item import ContentItem
                item_to_resolve = ContentItem(value)
                resolved_item = self.resolve_item(item_to_resolve)
                obj.replace_with(resolved_item)
                
        return soup.prettify(formatter=None)

    def resolve_item(self, item_to_resolve):
        pass
        