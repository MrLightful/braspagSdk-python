from typing import List

from braspag_sdk.utils import ObjectJSON


class SplitPaymentFares(ObjectJSON):

    def __init__(self, mdr=None, fee=None):
        self.mdr = mdr
        self.fee = fee


class SplitPayment(ObjectJSON):

    def __init__(self, subordinate_merchant_id, amount, mdr=None, fee=None):
        self.subordinate_merchant_id = subordinate_merchant_id
        self.amount = amount
        self.fares = SplitPaymentFares(mdr, fee)


class SplitPaymentsCapture(ObjectJSON):
    """ Data model for when capturing payment with a split. """

    def __init__(self, split_payments: List[SplitPayment]):
        self.split_payments = split_payments
