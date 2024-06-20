from core.conf.environ import env

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_DB_HOST'),
        'PORT': env('POSTGRES_DB_PORT'),
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
