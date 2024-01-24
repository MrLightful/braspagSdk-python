from braspag_sdk.utils import ApiBase

from braspag_sdk.apps.payments.environment import PaymentsEnvironment
from braspag_sdk.apps.payments.data import MerchantCredentials


class QuerySale(ApiBase):

    def __init__(self, merchant_credentials: MerchantCredentials, environment: PaymentsEnvironment):
        super(QuerySale, self).__init__(merchant_credentials)
        self.environment = environment

    def execute(self, payment_id):
        uri = '%s/v2/sales/%s' % (self.environment.query_api, payment_id)
        return self.send_request("GET", uri)
