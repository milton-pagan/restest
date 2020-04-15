import requests, json
from util.api.response import Response

class BaseCrud(object):
    def __init__(self, base_url, header):
        super().__init__()
        self.url = base_url
        self.header = header
        self.crud = {"get":self.get, "post":self.post, "put": self.put, "delete":self.delete}

    def _construct_url(self, **kwargs):
        new_url = self.url
        for key in kwargs.keys():
            new_url = new_url.replace("{"+key+"}", f"{kwargs[key]}")
        return new_url

    def get(self, body=None, **kwargs):
        new_url = self._construct_url(**kwargs)
        if body:
            return Response(requests.get(new_url, data=json.loads(body), headers=self.header))
        else:
            return Response(requests.get(new_url, headers=self.header))

    def put(self, body=None, **kwargs):
        new_url = self._construct_url(**kwargs)
        if body:
            return Response(requests.put(new_url, data=json.loads(body), headers=self.header))
        else:
            return Response(requests.put(new_url, headers=self.header))

    def post(self, body=None, **kwargs):
        new_url = self._construct_url(**kwargs)
        
        if body:
            data = json.loads(body) 
            return Response(requests.post(new_url, data=json.loads(body), headers=self.header))
        else:
            return Response(requests.post(new_url, headers=self.header))

    def delete(self, body=None, **kwargs):
        new_url = self._construct_url(**kwargs)
        if body:
            return Response(requests.delete(new_url, data=json.loads(body), headers=self.header))
        else:
            return Response(requests.delete(new_url, headers=self.header))


    
        
    