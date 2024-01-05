from datetime import datetime, timedelta

from . import Credentials, Environment, Sale, SplitMerchant
from .request.createSale import CreateSale
from .request.createSplitMerchant import CreateSplitMerchant
from .request.getOauth2Token import Oauth2Token
from .request.querySale import QuerySale
from .request.updateSale import UpdateSale


class Braspag(object):

    def __init__(self, credentials: Credentials, environment: Environment):

        self.environment = environment
        self.credentials = credentials

        # Oauth2 access tokens
        self.access_token = None
        self.token_expires_at = None

    def _validate_access_token(self):
        if self.token_expires_at is not None and self.token_expires_at > datetime.now():
            return
        request = Oauth2Token(self.credentials, self.environment)
        response = request.execute()
        self.access_token = response['access_token']
        self.token_expires_at = datetime.now() + timedelta(seconds=response['expires_in'])

    def create_sale(self, sale: Sale):
        request = CreateSale(self.credentials, self.environment)
        return request.execute(sale)

    def capture_sale(self, payment_id: str, amount=None, service_tax_amount=None):
        request = UpdateSale('capture', self.credentials, self.environment)
        request.amount = amount
        request.service_tax_amount = service_tax_amount
        return request.execute(payment_id)

    def cancel_sale(self, payment_id: str, amount=None):
        request = UpdateSale('void', self.credentials, self.environment)
        request.amount = amount
        return request.execute(payment_id)

    def get_sale(self, payment_id: str):
        request = QuerySale(self.credentials, self.environment)
        return request.execute(payment_id)

    def create_split_merchant(self, split_merchant: SplitMerchant):
        self._validate_access_token()
        request = CreateSplitMerchant(self.environment, self.access_token)
        return request.execute(split_merchant)
