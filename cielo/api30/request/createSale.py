
from .base import Base

class CreateSale(Base):

    def __init__(self, merchant, environment):

        super(CreateSale, self).__init__(merchant)

        self.environment = environment

    def execute(self, sale):

        uri = '%s1/sales' % self.environment.api

        return self.send_request("POST", uri, sale)
