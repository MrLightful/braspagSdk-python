# Braspag SDK for Python
Unofficial SDK for Python to integrate with Braspag payment gateway.

## Installation
```bash
pip install --upgrade braspag-sdk
```

## Configuration
```python
from braspag_sdk import Braspag, Credentials, Environment

creds = Credentials(
    merchant_id=BRASPAG_MERCHANT_ID,
    merchant_key=BRASPAG_MERCHANT_KEY,
    client_secret=BRASPAG_CLIENT_SECRET,
)
environment = Environment(sandbox=True)
braspagSdk = Braspag(creds, environment)
```

## Usage

### Creating a simple credit card payment

```python
from braspag_sdk import *

creds = Credentials('MerchantId', 'MerchantKey')
environment = Environment(sandbox=True)
braspag = Braspag(creds, environment)

# Create a Sale instance informing the payment ID
sale = Sale('123')

# Create a Customer instance informing the customer name
sale.customer = Customer('Fulano de Tal')

# Create a Credit Card instance informing the credit card data
credit_card = CreditCard('123', 'Visa')
credit_card.expiration_date = '12/2018'
credit_card.card_number = '0000000000000001'
credit_card.holder = 'Fulano de Tal'

# Create a Payment instance informing the payment amount
sale.payment = Payment(15700)
sale.payment.credit_card = credit_card

# Request Braspag API to create a sale
response_create_sale = braspag.create_sale(sale)

# Get the payment ID
payment_id = sale.payment.payment_id

# With the payment ID, we can capture it,
# if it has not been captured yet
response_capture_sale = braspag.capture_sale(payment_id, 15700, 0)

# And we can also cancel it, if necessary.
response_cancel_sale = braspag.cancel_sale(payment_id, 15700)
```
