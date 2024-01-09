from braspag_sdk.utils import ApiBase


class CreateSale(ApiBase):

    def __init__(self, merchant, environment):

        super(CreateSale, self).__init__(merchant)

        self.environment = environment

    def execute(self, sale):

        uri = '%s/sales' % self.environment.api

        response = self.send_request("POST", uri, sale)

        sale.update_return(response)

        return response
