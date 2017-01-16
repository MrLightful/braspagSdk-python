
from .base import Base

class ReactivateRecorrency(Base):

    def __init__(self, merchant, environment):

        super(ReactivateRecorrency, self).__init__(merchant)

        self.environment = environment

    def execute(self, payment_id):

        uri = '%s1/RecurrentPayment/%s/Reactivate' % (self.environment.api_query, payment_id)

        return self.send_request("PUT", uri)
