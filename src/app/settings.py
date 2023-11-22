from app.conf.environ import *
from app.conf.auth import *
from app.conf.boilerplate import *
from app.conf.db import *
from app.conf.http import *
from app.conf.installed_apps import *
from app.conf.media import *
from app.conf.middleware import *
from app.conf.static import *
from app.conf.templates import *
from app.conf.timezone import *

SECRET_KEY = env("SECRET_KEY")
AVIA_API_KEY = env("AVIA_API_KEY")
AVIA_SECRET_KEY = env("AVIA_SECRET_KEY")
DEBUG = env("DEBUG", cast=bool, default=False)
