from braspag_sdk.utils import ApiBase


class QuerySale(ApiBase):

    def __init__(self, merchant, environment):

        super(QuerySale, self).__init__(merchant)

        self.environment = environment

    def execute(self, payment_id):

        uri = '%s/sales/%s' % (self.environment.query_api, payment_id)

        return self.send_request("GET", uri)