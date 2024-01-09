class SilentOrderPostCredentials(object):
    """
    Credentials for Braspag Silent Order Post module.
    Learn more: https://braspag.github.io//manualp/braspag-silent-order-post
    """
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
