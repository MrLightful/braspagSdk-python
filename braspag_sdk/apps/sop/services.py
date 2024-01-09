from datetime import datetime, timedelta

from .requests import *


class BraspagSOPServices(object):
    """
    App for Braspag's Silent Order Post.
    Learn more: https://braspag.github.io//manualp/braspag-silent-order-post
    """

    def __init__(
        self,
        merchant_id: str,
        sop_credentials: SilentOrderPostCredentials,
        is_sandbox: bool,
    ):
        self._merchant_id = merchant_id
        self._sop_credentials = sop_credentials
        self._environment = SOPEnvironment(is_sandbox)

        self._oauth2_token = None
        self._oauth2_expires_at = None

    def _validate_oauth2_token(self):
        if self._oauth2_expires_at is not None and self._oauth2_expires_at > datetime.now():
            return
        request = Oauth2Token(
            sop_credentials=self._sop_credentials,
            environment=self._environment,
        )
        response = request.execute()
        self._oauth2_token = response['access_token']
        self._oauth2_expires_at = datetime.now() + timedelta(seconds=response['expires_in'])

    def get_access_token(self):
        self._validate_oauth2_token()
        request = AccessToken(
            merchant_id=self._merchant_id,
            access_token=self._oauth2_token,
            environment=self._environment,
        )
        return request.execute()

