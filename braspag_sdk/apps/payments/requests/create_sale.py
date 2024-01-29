from braspag_sdk.utils import ApiBase

from braspag_sdk.apps.payments.environment import PaymentsEnvironment
from braspag_sdk.apps.payments.data import MerchantCredentials


class CreateSale(ApiBase):

    def __init__(self, merchant_credentials: MerchantCredentials, environment: PaymentsEnvironment):
        super(CreateSale, self).__init__(merchant_credentials)
        self.environment = environment

    def execute(self, sale):
        uri = '%s/v2/sales' % self.environment.api
        response = self.send_request("POST", uri, sale)
        sale.update_return(response)
        return response
