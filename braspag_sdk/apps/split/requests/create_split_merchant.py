from braspag_sdk.utils import ApiOauthBase


class CreateSplitMerchant(ApiOauthBase):

    def __init__(self, access_token, environment):
        super(CreateSplitMerchant, self).__init__(access_token)
        self._environment = environment

    def execute(self, subordinate_merchant):
        uri = '%s/api/merchants' % self._environment.split_onboarding_v2
        response = self.send_request("POST", uri, subordinate_merchant)
        return response
