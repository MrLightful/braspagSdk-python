## 0.0.2

The release mostly meant to improve project & code quality.

- Clean code
- Remove unused dependencies
- Add CHANGELOG

*Breaking change:*
- Add missing arguments to EMV3DS access token generation (`establishment_code`, `merchant_name`, `mcc`)

## 0.0.1

The first public release of the package.
It integrates the most basic features of Braspag.

#### Features
- SDK's core initialization with options
- Payments integration (`create_sale`, `get_sale`, `capture_sale`, `cancel_sale`)
- Split Payments integration (`create_split_merchant`)
- Silent Order Post (SOP) integration (`get_access_token`)
- EMV3DS integration (`get_access_token`)
