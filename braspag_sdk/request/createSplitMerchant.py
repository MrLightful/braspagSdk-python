from .base import ApiOauthBase


class CreateSplitMerchant(ApiOauthBase):

        def __init__(self, environment, access_token):

            super(CreateSplitMerchant, self).__init__(access_token)

            self.environment = environment

        def execute(self, subordinate_merchant):

            uri = '%s1/api/merchants' % self.environment.split_onboarding_v2

            response = self.send_request("POST", uri, subordinate_merchant)

            return response
