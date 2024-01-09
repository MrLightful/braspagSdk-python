class SplitCredentials(object):
    """
    Credentials for Braspag Split Payments module.
    Learn more: https://braspag.github.io//manual/split-de-pagamentos-pagador
    """
    def __init__(self, client_secret):
        self.client_secret = client_secret
