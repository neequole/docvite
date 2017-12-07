from functools import wraps


def needs_doctor_login(func):
    @wraps(func)
    def wrapper(self):
        """ Performs login before each test """
        self.client.login(**self.DOCTOR_ACCOUNT)
        return func(self)
    return wrapper


def needs_client_login(func):
    @wraps(func)
    def wrapper(self):
        """ Performs login before each test """
        self.client.login(**self.CLIENT_ACCOUNT)
        return func(self)
    return wrapper
