import base64

from .base import Base


class Oauth2Token(Base):

    def __init__(self, credentials, environment):
        cred = (credentials.merchant_id + ':' + credentials.client_secret).encode('utf-8')
        cred_base64 = base64.b64encode(cred).decode('utf-8')
        authorization_headers = {
            'Authorization': 'Basic ' + cred_base64,
        }
        super().__init__(authorization_headers=authorization_headers)
        self.environment = environment

    def execute(self):

        uri = '%s1/oauth/token' % self.environment.oauth2_api
        data = {
            'grant_type': 'client_credentials'
        }

        response = self.send_request("POST", uri, data=data)

        return response
