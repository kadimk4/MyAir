import os.path

from app.conf.boilerplate import BASE_DIR
from app.conf.environ import env

MEDIA_URL = env('MEDIA_URL', default='/media/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
