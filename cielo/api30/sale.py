
from .objectJSON import ObjectJSON

class Sale(ObjectJSON):

    def __init__(self, merchant_order_id):

        self.merchant_order_id = merchant_order_id
        self.customer = None
        self.payment = None

    def update_return(self, r):

        payment = r.get('Payment') or {}

        self.payment.payment_id = payment.get('PaymentId')

        recurrent = payment.get('RecurrentPayment') or {}

        self.payment.recurrent_payment.recurrent_payment_id = recurrent.get('RecurrentPaymentId')
