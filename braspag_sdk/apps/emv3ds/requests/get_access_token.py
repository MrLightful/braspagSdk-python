import base64

from braspag_sdk.credentials import EMV3DSCredentials
from braspag_sdk.utils import Base, Environment


class AccessToken(Base):

    def __init__(self, *, emv3ds_credentials: EMV3DSCredentials, environment: Environment):
        cred = (emv3ds_credentials.client_id + ':' + emv3ds_credentials.client_secret).encode('utf-8')
        cred_base64 = base64.b64encode(cred).decode('utf-8')
        authorization_headers = {
            'Authorization': 'Basic ' + cred_base64,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        super().__init__(authorization_headers=authorization_headers)
        self._environment = environment

    def execute(self):

        uri = '%s/v2/auth/token' % self._environment.mpi
        data = {
             "EstablishmentCode": "1006993069",
             "MerchantName": "Loja Exemplo Ltda",
             "MCC": "5912"
        }

        response = self.send_request("POST", uri, data=data)
        return response
