from .base import *

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'db',
#         'USER': 'root',
#         'HOST': '127.0.0.1',
#         'PORT': 3306,
#         'PASSWORD': '1234',
#     }
# }
