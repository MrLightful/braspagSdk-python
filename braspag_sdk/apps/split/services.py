from datetime import datetime, timedelta

from braspag_sdk.apps.payments.data import MerchantCredentials
from .environment import SplitEnvironment
from .data import *
from .requests import *


class BraspagSplitServices(object):
    """
    App for Braspag's Split Payments.
    Learn more: https://braspag.github.io//manual/split-de-pagamentos-pagador
    """

    def __init__(
        self,
        merchant_credentials: MerchantCredentials,
        split_credentials: SplitCredentials,
        is_sandbox: bool,
    ):
        self._environment = SplitEnvironment(is_sandbox)
        self._merchant_credentials = merchant_credentials
        self._split_credentials = split_credentials

        self._access_token = None
        self._token_expires_at = None

    def _validate_access_token(self):
        if self._token_expires_at is not None and self._token_expires_at > datetime.now():
            return
        request = Oauth2Token(
            merchant_id=self._merchant_credentials.merchant_id,
            client_secret=self._split_credentials.client_secret,
            environment=self._environment,
        )
        response = request.execute()
        self._access_token = response['access_token']
        self._token_expires_at = datetime.now() + timedelta(seconds=response['expires_in'])

    def create_split_merchant(self, split_merchant: SplitMerchant):
        self._validate_access_token()
        request = CreateSplitMerchant(self._access_token, self._environment)
        return request.execute(split_merchant)
