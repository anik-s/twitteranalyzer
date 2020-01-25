class UnAuthorizedException(Exception):
    def __init__(self, message):
        self.code = 401
        self.message = message
        Exception.__init__(self)


class InternalException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message
        Exception.__init__(self)
