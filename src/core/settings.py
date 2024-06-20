from split_settings.tools import include

from core.conf.environ import env

include(
    'conf/api.py',
    'conf/auth.py',
    'conf/boilerplate.py',
    'conf/db.py',
    'conf/http.py',
    'conf/i18n.py',
    'conf/installed_apps.py',
    'conf/media.py',
    'conf/middleware.py',
    'conf/static.py',
    'conf/templates.py',
    'conf/timezone.py',
    'conf/rest_framework.py',
    'conf/knox.py'
)


SECRET_KEY = env('SECRET_KEY')
AVIA_API_KEY = env('AVIA_API_KEY')
AVIA_SECRET_KEY = env('AVIA_SECRET_KEY')
DEBUG = env('DEBUG', cast=bool, default=False)
