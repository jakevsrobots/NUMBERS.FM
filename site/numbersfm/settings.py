ADMIN_PASSWORD = 'party'
SECRET_KEY = 'notverysecret'

try:
    from local_settings import *
except ImportError:
    pass
