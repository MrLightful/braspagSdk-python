from .apps import BraspagEMV3DSServices, BraspagPaymentsServices, BraspagSplitServices, BraspagSOPServices, \
                  MerchantCredentials, EMV3DSCredentials, SplitCredentials, SilentOrderPostCredentials


class Braspag(object):

    def __init__(self, merchant_credentials: MerchantCredentials, is_sandbox: bool):

        # Creds & config
        self._is_sandbox = is_sandbox
        self._merchant_credentials = merchant_credentials

        # Apps
        self._payments = BraspagPaymentsServices(self._merchant_credentials, self._is_sandbox)
        self._split = None
        self._emv3ds = None
        self._sop = None

    @property
    def is_sandbox(self) -> bool:
        return self._is_sandbox

    @property
    def payments(self) -> BraspagPaymentsServices:
        return self._payments

    @property
    def split(self) -> BraspagSplitServices:
        if not self._split:
            raise Exception("Split app is not initialized, "
                            "please add it to Braspag instance using add_split() method")
        return self._split

    @property
    def emv3ds(self) -> BraspagEMV3DSServices:
        if not self._emv3ds:
            raise Exception("EMV3DS app is not initialized, "
                            "please add it to Braspag instance using add_emv3ds() method")
        return self._emv3ds

    @property
    def sop(self) -> BraspagSOPServices:
        if not self._sop:
            raise Exception("SOP app is not initialized, "
                            "please add it to Braspag instance using add_sop() method")
        return self._sop

    def add_split(self, split_credentials: SplitCredentials):
        """
        Add app for Braspag's Split Payments.
        Learn more: https://braspag.github.io//manual/split-de-pagamentos-pagador
        """
        self._split = BraspagSplitServices(self._merchant_credentials, split_credentials, self._is_sandbox)

    def add_emv3ds(self, emv3ds_credentials: EMV3DSCredentials):
        """
        Add app for Braspag's EMV3DS.
        Learn more: https://braspag.github.io//manual/emv3ds
        """
        self._emv3ds = BraspagEMV3DSServices(emv3ds_credentials, self._is_sandbox)

    def add_sop(self, sop_credentials: SilentOrderPostCredentials):
        """
        Add app for Braspag's Silent Order Post.
        Learn more: https://braspag.github.io//manualp/braspag-silent-order-post
        """
        self._sop = BraspagSOPServices(self._merchant_credentials.merchant_id, sop_credentials, self._is_sandbox)
