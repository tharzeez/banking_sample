class AppException(Exception):
    def __init__(self, message=None):
        if message is not None:
            self.message = message
        super().__init__(message)
