


class Response(object):

    def __init__(self, req_response):
        self.response = req_response
    
    def get_data(self):
        try:
            return self.response.json()
        except ValueError:
            return self.response.content

    def status(self):
        return self.response.status_code

    def to_dict(self):
        return {'status':self.status(), 'data':self.get_data()}