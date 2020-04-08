


class Response(object):

    def __init__(self, req_response):
        self.response = req_response
    
    def get_data(self):
        try:
            return self.response.json()
        except ValueError:
            return self.response.text()

    def status(self):
        return self.response.status_code

