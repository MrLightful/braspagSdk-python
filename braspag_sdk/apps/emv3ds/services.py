from .requests import *


class BraspagEMV3DSServices(object):
    """
    App for Braspag's EMV 3DS.
    Learn more: https://braspag.github.io//manual/emv3ds
    """

    def __init__(
        self,
        emv3ds_credentials: EMV3DSCredentials,
        is_sandbox: bool,
    ):
        self._environment = EMV3DSEnvironment(is_sandbox)
        self._emv3ds_credentials = emv3ds_credentials

    def get_access_token(self, establishment_code: str, merchant_name: str, mcc: str):
        request = AccessToken(
            emv3ds_credentials=self._emv3ds_credentials,
            environment=self._environment,
        )
        return request.execute(establishment_code, merchant_name, mcc)

