class EMV3DSCredentials(object):
    """
    Credentials for Braspag EMV 3DS module.
    Learn more: https://braspag.github.io//manual/emv3ds
    """
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
