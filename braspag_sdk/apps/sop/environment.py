class SOPEnvironment(object):

    def __init__(self, is_sandbox: bool):

        if is_sandbox:
            self.oauth2_api = 'https://authsandbox.braspag.com.br'
            self.sop_auth = 'https://transactionsandbox.pagador.com.br'
        else:
            self.oauth2_api = 'https://auth.braspag.com.br'
            self.sop_auth = 'https://transaction.pagador.com.br'
