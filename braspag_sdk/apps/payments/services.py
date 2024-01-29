from .data import *
from .requests import *


class BraspagPaymentsServices(object):
    """
    App for Braspag's Payments.
    Learn more: https://braspag.github.io//manual/braspag-pagador
    """

    def __init__(self, merchant_credentials: MerchantCredentials, is_sandbox: bool):
        self._environment = PaymentsEnvironment(is_sandbox)
        self.merchant_credentials = merchant_credentials

    def create_sale(self, sale: Sale):
        request = CreateSale(self.merchant_credentials, self._environment)
        return request.execute(sale)

    def capture_sale(self, payment_id: str, amount=None, service_tax_amount=None, **kwargs):
        request = UpdateSale('capture', self.merchant_credentials, self._environment)
        request.amount = amount
        request.service_tax_amount = service_tax_amount

        data = None
        if kwargs:
            data = json.dumps(kwargs)
        request.data = data

        return request.execute(payment_id)

    def cancel_sale(self, payment_id: str, amount=None):
        request = UpdateSale('void', self.merchant_credentials, self._environment)
        request.amount = amount
        return request.execute(payment_id)

    def get_sale(self, payment_id: str):
        request = QuerySale(self.merchant_credentials, self._environment)
        return request.execute(payment_id)
