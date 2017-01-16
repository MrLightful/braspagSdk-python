
from .request.createSale import CreateSale
from .request.querySale import QuerySale
from .request.updateSale import UpdateSale

class CieloEcommerce(object):

    def __init__(self, merchant, environment):

        self.environment = environment
        self.merchant = merchant

    def create_sale(self, sale):

        request = CreateSale(self.merchant, self.environment)

        response = request.execute(sale)

        sale.update_return(response)

        return response

    def capture_sale(self, payment_id, amount = None, service_tax_amount = None):
        request = UpdateSale('capture', self.merchant, self.environment)

        request.amount = amount
        request.service_tax_amount = service_tax_amount

        return request.execute(payment_id)

    def cancel_sale(self, payment_id, amount = None):
        request = UpdateSale('void', self.merchant, self.environment)

        request.amount = amount

        return request.execute(payment_id)

    def get_sale(self, payment_id):
        request = QuerySale(self.merchant, self.environment)

        return request.execute(payment_id)
