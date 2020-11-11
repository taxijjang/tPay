from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db',
        'USER': 'root',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'PASSWORD': '1234',
    }
}
