class MerchantCredentials(object):
    """
    Credentials for general Braspag Payments module.
    Learn more: https://braspag.github.io//manual/braspag-pagador
    """
    def __init__(self, merchant_id, merchant_key):
        self.merchant_id = merchant_id
        self.merchant_key = merchant_key


class SplitCredentials(object):
    """
    Credentials for Braspag Split Payments module.
    Learn more: https://braspag.github.io//manual/split-de-pagamentos-pagador
    """
    def __init__(self, client_secret):
        self.client_secret = client_secret


class EMV3DSCredentials(object):
    """
    Credentials for Braspag EMV 3DS module.
    Learn more: https://braspag.github.io//manual/emv3ds
    """
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret


class SilentOrderPostCredentials(object):
    """
    Credentials for Braspag Silent Order Post module.
    Learn more: https://braspag.github.io//manualp/braspag-silent-order-post
    """
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
