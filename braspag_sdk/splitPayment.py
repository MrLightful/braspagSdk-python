from .objectJSON import ObjectJSON


class SplitPaymentFares(ObjectJSON):

    def __init__(self, mdr=None, fee=None):
        self.mdr = mdr
        self.fee = fee


class SplitPayment(ObjectJSON):

    def __init__(self, subordinadate_merchant_id, amount, mdr=None, fee=None):
        self.subordinadate_merchant_id = subordinadate_merchant_id
        self.amount = amount
        self.fares = SplitPaymentFares(mdr, fee)
