import os.path

from core.conf.boilerplate import BASE_DIR
from core.conf.environ import env

MEDIA_URL = env('MEDIA_URL', default='/media/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
