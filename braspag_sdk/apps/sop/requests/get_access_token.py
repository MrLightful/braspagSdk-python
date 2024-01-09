from braspag_sdk.apps.sop.environment import SOPEnvironment
from braspag_sdk.utils import Base


class AccessToken(Base):

    def __init__(self, *, merchant_id: str, access_token: str, environment: SOPEnvironment):
        authorization_headers = {
            'MerchantId': merchant_id,
            'Authorization': 'Bearer ' + access_token,
        }
        super().__init__(authorization_headers=authorization_headers)
        self._environment = environment

    def execute(self):
        uri = '%s/post/api/public/v2/accesstoken' % self._environment.sop_auth
        response = self.send_request("POST", uri)
        return response
