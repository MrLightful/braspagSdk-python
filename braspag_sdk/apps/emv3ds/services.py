from datetime import datetime, timedelta

from braspag_sdk.credentials import EMV3DSCredentials
from braspag_sdk.utils import Environment
from .requests.get_access_token import AccessToken


class BraspagEMV3DSServices(object):

    def __init__(
        self,
        emv3ds_credentials: EMV3DSCredentials,
        environment: Environment,
    ):
        self._environment = environment
        self._emv3ds_credentials = emv3ds_credentials

    def get_access_token(self):
        request = AccessToken(
            emv3ds_credentials=self._emv3ds_credentials,
            environment=self._environment,
        )
        return request.execute()

