
from .objectJSON import ObjectJSON

class Sale(ObjectJSON):

    def __init__(self, merchant_order_id):

        self.merchant_order_id = merchant_order_id
        self.customer = None
        self.payment = None

    def update_return(self, response_return):

        self.payment.payment_id = response_return['Payment'].get('PaymentId')
