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

    def _get_oauth2_token(self):
        request = Oauth2Token(
            sop_credentials=self._sop_credentials,
            environment=self._environment,
        )
        response = request.execute()
        return response['access_token']

    def get_access_token(self):
        oauth2_token = self._get_oauth2_token()
        request = AccessToken(
            merchant_id=self._merchant_id,
            access_token=oauth2_token,
            environment=self._environment,
        )
        return request.execute()
