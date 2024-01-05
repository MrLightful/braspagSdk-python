class Credentials(object):

    def __init__(self, merchant_id, merchant_key, client_id=None, client_secret=None):
        self.merchant_id = merchant_id
        self.merchant_key = merchant_key
        self.client_id = client_id
        self.client_secret = client_secret
