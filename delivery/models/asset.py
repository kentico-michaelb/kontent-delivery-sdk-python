class Asset:
    def __init__(self, asset):
        self.name = asset['name'] 
        self.type = asset['type'] 
        self.size = asset['size'] 
        self.url = asset['url']
        self.description = asset['description']
        self.width = asset['width'], 
        self.height = asset['height']        