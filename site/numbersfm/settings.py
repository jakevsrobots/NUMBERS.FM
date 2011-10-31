ADMIN_PASSWORD = 'party'
SECRET_KEY = 'notverysecret'
SERVER_PORT = '9000'

try:
    from local_settings import *
except ImportError:
    pass
