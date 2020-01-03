from bs4 import BeautifulSoup
from delivery.models.content_link import ContentLink

class InlineLinkResolver:
    def __init__(self):
        pass

    def resolve(self, content, links):
        soup = BeautifulSoup(content, features="html.parser")
        for key, value in links.items():
            obj = soup.find("a", attrs={"data-item-id":key})            
            if obj:
                content_link = ContentLink(key, value['codename'], value['type'], value['url_slug'])
                resolved_link = self.resolve_link(content_link)   
                obj["href"] = resolved_link
        return soup

    def resolve_link(self, link_to_resolve):
        pass
        