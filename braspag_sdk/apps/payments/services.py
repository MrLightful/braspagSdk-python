from braspag_sdk.credentials import MerchantCredentials
from braspag_sdk.utils import Environment
from .data.sale import Sale
from .requests.create_sale import CreateSale
from .requests.query_sale import QuerySale
from .requests.update_sale import UpdateSale


class BraspagPaymentsServices(object):

    def __init__(self, merchant_credentials: MerchantCredentials, environment: Environment):
        self._environment = environment
        self.merchant_credentials = merchant_credentials

    def create_sale(self, sale: Sale):
        request = CreateSale(self.merchant_credentials, self._environment)
        return request.execute(sale)

    def capture_sale(self, payment_id: str, amount=None, service_tax_amount=None):
        request = UpdateSale('capture', self.merchant_credentials, self._environment)
        request.amount = amount
        request.service_tax_amount = service_tax_amount
        return request.execute(payment_id)

    def cancel_sale(self, payment_id: str, amount=None):
        request = UpdateSale('void', self.merchant_credentials, self._environment)
        request.amount = amount
        return request.execute(payment_id)

    def get_sale(self, payment_id: str):
        request = QuerySale(self.merchant_credentials, self._environment)
        return request.execute(payment_id)
