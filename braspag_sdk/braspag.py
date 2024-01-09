from typing import Optional

from .apps import BraspagEMV3DSServices, BraspagPaymentsServices, BraspagSplitServices, \
                  MerchantCredentials, EMV3DSCredentials, SplitCredentials, SilentOrderPostCredentials


class Braspag(object):

    def __init__(self, merchant_credentials: MerchantCredentials, is_sandbox: bool):

        # Creds & config
        self._is_sandbox = is_sandbox
        self._merchant_credentials = merchant_credentials
        self.split_credentials: Optional[SplitCredentials] = None
        self.emv3ds_credentials: Optional[EMV3DSCredentials] = None
        self.sop_credentials: Optional[SilentOrderPostCredentials] = None

        # Apps
        self._payments = BraspagPaymentsServices(self._merchant_credentials, self._is_sandbox)
        self._split = None
        self._emv3ds = None
        self._sop = None

    def init(self):

        if self.split_credentials:
            self._split = BraspagSplitServices(self._merchant_credentials, self.split_credentials, self._is_sandbox)

        if self.emv3ds_credentials:
            self._split = BraspagEMV3DSServices(self.emv3ds_credentials, self._is_sandbox)

        # if self.sop_credentials:
        #     self._split = BraspagSOPApp(self.sop_credentials, self._is_sandbox)

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
                            "please define SplitCredentials and call init() method first")
        return self._split

    @property
    def emv3ds(self) -> BraspagEMV3DSServices:
        if not self._emv3ds:
            raise Exception("EMV3DS app is not initialized, "
                            "please define EMV3DSCredentials and call init() method first")
        return self._emv3ds

    # @property
    # def sop(self) -> BraspagSOPServices:
    #     if not self._sop:
    #         raise Exception("SOP app is not initialized, "
    #                         "please define SilentOrderPostCredentials and call init() method first")
    #     return self._sop
