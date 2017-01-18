# API-3.0-Python

SDK API-3.0 Python Cielo

Índice:

* [Principais recursos](#principais-recursos)
* [Limitações](#limitações)
* [Exemplos](#exemplos)
    * [Criando um pagamento com cartão de crédito](#criando-um-pagamento-com-cartão-de-crédito)
* [Manual Oficial da Cielo](#manual-oficial-da-cielo)

## Principais recursos

* [x] Pagamentos por cartão de crédito.
* [x] Pagamentos recorrentes.
    * [x] Com autorização na primeira recorrência.
    * [x] Com autorização a partir da primeira recorrência.
* [x] Pagamentos por cartão de débito.
* [x] Pagamentos por boleto (Bradesco e Banco do Brasil).
* [ ] Pagamentos por transferência eletrônica.
* [x] Cancelamento de autorização.
* [x] Consulta de pagamentos.

## Limitações

Por envolver a interface de usuário da aplicação, o SDK funciona apenas como um framework para criação das transações. Nos casos onde a autorização é direta, não há limitação; mas nos casos onde é necessário a autenticação ou qualquer tipo de redirecionamento do usuário, o desenvolvedor deverá utilizar o SDK para gerar o pagamento e, com o link retornado pela Cielo, providenciar o redirecionamento do usuário.

## Utilizando o SDK
Para criar um pagamento simples com cartão de crédito com o SDK, basta fazer:

## Instalação
O API-3.0 Python Cielo pode ser facilmente instalado com o comando a seguir:
```bash
pip install cieloApi3
```

## Exemplos
### Criando um pagamento com cartão de crédito

```python
from cieloApi3 import *

import json

# Configure o ambiente
environment = Environment(sandbox=True)

# Configure seu merchant, para gerar acesse: https://cadastrosandbox.cieloecommerce.cielo.com.br/
merchant = Merchant('MerchantId', 'MerchantKey')

# Crie uma instância de Sale informando o ID do pagamento
sale = Sale('123')

# Crie uma instância de Customer informando o nome do cliente
sale.customer = Customer('Fulano de Tal')

# Crie uma instância de Credit Card utilizando os dados de teste
# esses dados estão disponíveis no manual de integração
credit_card = CreditCard('123', 'Visa')
credit_card.expiration_date = '12/2018'
credit_card.card_number = '0000000000000001'
credit_card.holder = 'Fulano de Tal'

# Crie uma instância de Payment informando o valor do pagamento
sale.payment = Payment(15700)
sale.payment.credit_card = credit_card

# Cria instância do controlador do ecommerce
cielo_ecommerce = CieloEcommerce(merchant, environment)

# Criar a venda e imprime o retorno
response_create_sale = cielo_ecommerce.create_sale(sale)
print '----------------------response_create_sale----------------------'
print json.dumps(response_create_sale, indent=2)
print '----------------------response_create_sale----------------------'

# Com a venda criada na Cielo, já temos o ID do pagamento, TID e demais
# dados retornados pela Cielo
payment_id = sale.payment.payment_id

# Com o ID do pagamento, podemos fazer sua captura,
# se ela não tiver sido capturada ainda
response_capture_sale = cielo_ecommerce.capture_sale(payment_id, 15700, 0)
print '----------------------response_capture_sale----------------------'
print json.dumps(response_capture_sale, indent=2)
print '----------------------response_capture_sale----------------------'

# E também podemos fazer seu cancelamento, se for o caso
response_cancel_sale = cielo_ecommerce.cancel_sale(payment_id, 15700)
print '---------------------response_cancel_sale---------------------'
print json.dumps(response_cancel_sale, indent=2)
print '---------------------response_cancel_sale---------------------'
```

## Manual Oficial da Cielo

Para mais informações sobre a integração com a API 3.0 da Cielo, vide o manual em: [Integração API 3.0](https://developercielo.github.io/Webservice-3.0/)
