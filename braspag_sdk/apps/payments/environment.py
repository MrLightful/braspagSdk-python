class PaymentsEnvironment(object):

    def __init__(self, is_sandbox: bool):

        if is_sandbox:
            self.api = 'https://apisandbox.braspag.com.br'
            self.query_api = 'https://apiquerysandbox.braspag.com.br'
        else:
            self.api = 'https://api.braspag.com.br'
            self.query_api = 'https://apiquery.braspag.com.br'
