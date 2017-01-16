#-*- coding: utf-8 -*-s

import sys
sys.path.insert(0, "./")

import json

from cielo.api30 import *

# Configure o ambiente
environment = Environment(sandbox=True)

# Configure seu merchant, para gerar acesse: https://cadastrosandbox.cieloecommerce.cielo.com.br/
merchant = Merchant('MerchantId', 'MerchantKey')

# Crie uma instância de Credit Card utilizando os dados de teste
# esses dados estão disponíveis no manual de integração
credit_card = CreditCard('123', 'Visa')
credit_card.expiration_date = '12/2018'
credit_card.card_number = '4532117080573700'
credit_card.holder = 'Comprador T Cielo'
credit_card.customer_name = 'Comprador Teste Cielo'

# Cria instância do controlador do ecommerce
cielo_ecommerce = CieloEcommerce(merchant, environment)

# Criar a venda e imprime o retorno
response_create_card_token = cielo_ecommerce.create_card_token(credit_card)
print '----------------------response_create_card_token----------------------'
print json.dumps(response_create_card_token, indent=2)
print '----------------------response_create_card_token----------------------'

# Com o cartão gerado token na Cielo, já temos o Token do cartão para uma futura cobrança
print 'New Card Token:', credit_card.card_token
