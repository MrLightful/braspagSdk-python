class EMV3DSEnvironment(object):

    def __init__(self, is_sandbox: bool):

        if is_sandbox:
            self.mpi = 'https://mpisandbox.braspag.com.br'
        else:
            self.mpi = 'https://mpi.braspag.com.br'
