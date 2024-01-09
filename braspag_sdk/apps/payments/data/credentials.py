class MerchantCredentials(object):
    """
    Credentials for general Braspag Payments module.
    Learn more: https://braspag.github.io//manual/braspag-pagador
    """
    def __init__(self, merchant_id, merchant_key):
        self.merchant_id = merchant_id
        self.merchant_key = merchant_key
