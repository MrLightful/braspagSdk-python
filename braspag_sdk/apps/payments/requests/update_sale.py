import json

from braspag_sdk.utils import ApiBase

from braspag_sdk.apps.payments.environment import PaymentsEnvironment
from braspag_sdk.apps.payments.data import MerchantCredentials


class UpdateSale(ApiBase):

    def __init__(self, type: str, merchant_credentials: MerchantCredentials, environment: PaymentsEnvironment):

        super(UpdateSale, self).__init__(merchant_credentials)

        self.environment = environment
        self.type = type
        self.service_tax_amount = None
        self.amount = None
        self.data = None

    def execute(self, payment_id):

        uri = '%s/v2/sales/%s/%s' % (self.environment.api, payment_id, self.type)

        data = {}
        params = {}

        if self.amount:
            params['amount'] = self.amount

        if self.service_tax_amount:
            params['serviceTaxAmount'] = self.service_tax_amount

        if self.data:
            data = self.data

        return self.send_request('PUT', uri, params=params, data=data)
