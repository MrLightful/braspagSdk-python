
class CreditCard(object):

    def __init__(self, security_code, brand):

        self.card_number = None
        self.holder = None
        self.expiration_date = None
        self.security_code = security_code
        self.save_card = None
        self.brand = brand
        self.card_token = None
