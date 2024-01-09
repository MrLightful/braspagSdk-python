import base64

from braspag_sdk.apps.split import SplitEnvironment
from braspag_sdk.utils import Base


class Oauth2Token(Base):

    def __init__(self, *, merchant_id: str, client_secret: str, environment: SplitEnvironment):
        cred = (merchant_id + ':' + client_secret).encode('utf-8')
        cred_base64 = base64.b64encode(cred).decode('utf-8')
        authorization_headers = {
            'Authorization': 'Basic ' + cred_base64,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        super().__init__(authorization_headers=authorization_headers)
        self.environment = environment

    def execute(self):

        uri = '%s/oauth2/token' % self.environment.oauth2_api
        data = {
            'grant_type': 'client_credentials'
        }

        response = self.send_request("POST", uri, data=data)
        return response
