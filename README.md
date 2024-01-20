# Braspag SDK for Python
[![PyPi page link -- version](https://img.shields.io/pypi/v/braspag-sdk.svg)](https://pypi.python.org/pypi/braspag-sdk)
[![License](https://img.shields.io/github/license/romatallinn/braspagSdk-python)](LICENSE)


An unofficial Python SDK for [Braspag](https://braspag.github.io/).

## Disclaimer
This SDK is created for personal use and the functionality is limited to the needs of my projects.
You are more than welcome to contribute the code you need as soon as it follows the same code style.
Fortunately, this is a very simple SDK, so it should be easy to understand and extend.

# Getting Started

## Installation
```bash
pip install --upgrade braspag-sdk
```

## Configuration
```python
import os

from braspag_sdk import Braspag, MerchantCredentials, SplitCredentials, EMV3DSCredentials, SilentOrderPostCredentials

merchant_creds = MerchantCredentials(
    merchant_id=os.environ.get('BRASPAG_MERCHANT_ID'),
    merchant_key=os.environ.get('BRASPAG_MERCHANT_KEY'),
)

split_creds = SplitCredentials(
    client_secret=os.environ.get('BRASPAG_SPLIT_CLIENT_SECRET'),
)

emv3ds_creds = EMV3DSCredentials(
    client_id=os.environ.get('BRASPAG_EMV3DS_CLIENT_ID'),
    client_secret=os.environ.get('BRASPAG_EMV3DS_CLIENT_SECRET'),
)

sop_creds = SilentOrderPostCredentials(
    client_id=os.environ.get('BRASPAG_SOP_CLIENT_ID'),
    client_secret=os.environ.get('BRASPAG_SOP_CLIENT_SECRET'),
)

braspagSdk = Braspag(merchant_creds, is_sandbox=True)
braspagSdk.add_split(split_creds)
braspagSdk.add_emv3ds(emv3ds_creds)
braspagSdk.add_sop(sop_creds)
```

## Usage

### Creating a payment
[Official Documentation](https://braspag.github.io//manual/braspag-pagador)

```python
from braspag_sdk import Braspag, Sale, Customer, Address, CreditCard, Payment, SplitPayment

# Configuration
braspagSdk: Braspag = ...

print(f'Creating payment transaction in Braspag...')

# Prepare the basic sale info.
sale = Sale(merchant_order_id=...)

# Prepare the customer info.
sale.customer = Customer(name=...)
sale.customer.email = ...
sale.customer.identity = ...
sale.customer.identity_type = ...   # 'cpf' or 'cnpj'

# Prepare the customer's address.
sale_address = Address()
sale_address.street = ...
sale_address.number = ...
sale_address.complement = ...
sale_address.zip_code = ...
sale_address.city = ...
sale_address.state = ...
sale_address.country = ...
sale.customer.address = sale_address

# Prepare the payment info and credit card for it.
# Most likely, you are not PCI compliant, so you will need to use Braspag's card tokenization.
credit_card = CreditCard(security_code=None, brand=None)
credit_card.card_token = ''

sale.payment = Payment(amount=..., installments=...)
sale.payment.soft_descriptor = ...,
sale.payment.credit_card = credit_card

# Split payment with subourdintate merchants.
subordinate_merchant_id = ...
amount = ...
sale.payment.do_split = True
sale.payment.split_payments = [
    SplitPayment(subordinate_merchant_id, amount, mdr=..., fee=...)
]

# Create the payment in Cielo.
sale_response = braspagSdk.payments.create_sale(sale)
payment_response = sale_response['Payment']

# Save the payment reference in Dizconto's database.
payment_id = payment_response['PaymentId']
payment_method = payment_response['Type']
payment_status = payment_response['Status']
payment_reason = payment_response['ReturnCode']
payment_amount = payment_response['Amount']
print(f'Created Braspag Payment: {payment_id}')
```

### Creating a subordinate merchant
[Official Documentation](https://braspag.github.io//manual/split-de-pagamentos-pagador)

```python
from braspag_sdk import Braspag, SplitMerchant, SplitMerchantAddress, SplitMerchantBank, SplitMerchantAgreement

# Configuration.
braspagSdk: Braspag = ...
braspagSdk.add_split(...)

print(f'Creating Braspag Split Subordinate Merchant...')

address = SplitMerchantAddress(
    street=...,
    number=...,
    complement=...,
    neighborhood=...,
    zip_code=...,
    city=...,
    state=...,
)

bank_account = SplitMerchantBank(
    bank=...,
    bank_account_type=...,
    number=...,
    verifier_digit=...,
    agency_number=...,
    agency_digit=...,
    operation=...,
)

agreements = [
    SplitMerchantAgreement(
        percent=...,
        fee=...,
    )
]

split_merchant = SplitMerchant(master_merchant_id=...)
split_merchant.fancy_name = ...
split_merchant.website = ...
split_merchant.mail_address = ...
split_merchant.contact_name = ...
split_merchant.contact_phone = ...
split_merchant.corporate_name = ...
split_merchant.document_number = ...
split_merchant.document_type = ...
split_merchant.address = address
split_merchant.bank_account = bank_account
split_merchant.agreements = agreements

result = braspagSdk.split.create_split_merchant(split_merchant)
merchant_id = result['id']
print(f'Created Braspag Split Subordinate Merchant: {merchant_id}')
```

### Other

```python
from braspag_sdk import Braspag

# Configuration.
braspagSdk: Braspag = ...

# Payments
payment_id = ...
braspagSdk.payments.get_sale(payment_id)
braspagSdk.payments.capture_sale(payment_id, amount=...)
braspagSdk.payments.cancel_sale(payment_id, amount=...)

# Generate access token for EMV 3DS.
# Learn more: https://braspag.github.io//manual/emv3ds#1.-criando-o-token-de-acesso
establishment_code = ...
merchant_name = ...
mcc = ...
braspagSdk.emv3ds.get_access_token(establishment_code, merchant_name, mcc)

# Generate access token for Silent Order Post.
# Learn more: https://braspag.github.io//manualp/braspag-silent-order-post#2.-obtendo-accesstoken-sop
braspagSdk.sop.get_access_token()
```

# License
Licensed under the MIT license, see [`LICENSE`](LICENSE).