from braspag_sdk.apps.payments.data import MerchantCredentials
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

    def _get_oauth2_token(self):
        request = Oauth2Token(
            merchant_id=self._merchant_credentials.merchant_id,
            client_secret=self._split_credentials.client_secret,
            environment=self._environment,
        )
        response = request.execute()
        return response['access_token']

    def create_split_merchant(self, split_merchant: SplitMerchant):
        oauth2_token = self._get_oauth2_token()
        request = CreateSplitMerchant(oauth2_token, self._environment)
        return request.execute(split_merchant)
