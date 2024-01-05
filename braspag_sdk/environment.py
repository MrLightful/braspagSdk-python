class Environment(object):

    def __init__(self, sandbox):

        # Production
        if not sandbox:
            self.api = 'https://apisandbox.braspag.com.br/'
            self.oauth2_api = 'https://authsandbox.braspag.com.br/'
            self.query_api = 'https://apiquerysandbox.braspag.com.br/'
            self.split_api = 'https://splitsandbox.braspag.com.br/'
        else:
            self.api = 'https://api.braspag.com.br/'
            self.oauth2_api = 'https://auth.braspag.com.br/'
            self.query_api = 'https://apiquery.braspag.com.br/'
            self.split_api = 'https://split.braspag.com.br/'
