from braspag_sdk.utils import ApiOauthBase

from braspag_sdk.apps.split.environment import SplitEnvironment


class CreateSplitMerchant(ApiOauthBase):

    def __init__(self, access_token: str, environment: SplitEnvironment):
        super(CreateSplitMerchant, self).__init__(access_token)
        self.environment = environment

    def execute(self, subordinate_merchant):
        uri = '%s/api/merchants' % self.environment.split_onboarding_v2
        response = self.send_request("POST", uri, subordinate_merchant)
        return response
