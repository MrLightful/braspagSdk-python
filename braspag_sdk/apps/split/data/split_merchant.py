from braspag_sdk.utils import ObjectJSON


class SplitMerchantAddress(ObjectJSON):
    def __init__(self, *, street: str, number: str, complement: str, neighborhood: str, zip_code: str, city: str,
                 state: str):
        self.street = street
        self.number = number
        self.complement = complement
        self.neighborhood = neighborhood
        self.zip_code = zip_code
        self.city = city
        self.state = state


class SplitMerchantBank(ObjectJSON):
    def __init__(self, *, bank: str, bank_account_type: str, number: str, operation: str,
                 verifier_digit: str, agency_number: str, agency_digit: str):
        self.bank = bank
        self.bank_account_type = bank_account_type
        self.number = number
        self.operation = operation
        self.verifier_digit = verifier_digit
        self.agency_number = agency_number
        self.agency_digit = agency_digit


class SplitMerchantAgreement(ObjectJSON):

    def __init__(self, percent=None, fee=None):
        self.percent = percent
        self.fee = fee


class SplitMerchant(ObjectJSON):

    def __init__(self, *, master_merchant_id):
        self.type = 'Subordinate'
        self.master_merchant_id = master_merchant_id
        self.fancy_name = None
        self.website = None
        self.mail_address = None
        self.contact_name = None
        self.contact_phone = None
        self.corporate_name = None
        self.document_number = None
        self.document_type = None
        self.birthday_date = None
        self.business_activity_id = None
        self.address = None
        self.bank_account = None
        self.agreements = None
