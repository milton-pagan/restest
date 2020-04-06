


class Response(object):

    def __init__(self, req_response):
        self.response = req_response

    def get_json(self):
        try:
            return self.response.json()
        except ValueError:
            return {}

