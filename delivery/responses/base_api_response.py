class BaseApiResponse:
    def __init__(self, content, headers, request_url):
        self.content = content
        self.headers = headers
        self.has_stale_content = headers.get('X-Stale-Content')   
        self.request_url = request_url

        if 'X-Continuation' in dict(headers):
            self.continuation_token = headers['X-Continuation']
        else:
            self.continuation_token = None