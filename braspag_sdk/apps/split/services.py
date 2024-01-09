from datetime import datetime, timedelta

from braspag_sdk.credentials import SplitCredentials, MerchantCredentials
from braspag_sdk.utils import Environment
from .data.split_merchant import SplitMerchant
from .requests.create_split_merchant import CreateSplitMerchant
from .requests.get_oauth2_token import Oauth2Token


class BraspagSplitServices(object):

    def __init__(
        self,
        merchant_credentials: MerchantCredentials,
        split_credentials: SplitCredentials,
        environment: Environment,
    ):
        self._environment = environment
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
