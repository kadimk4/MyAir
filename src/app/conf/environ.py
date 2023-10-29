import os
import environ

env = environ.Env()
environ.Env.read_env(os.path.join('app/conf', '.env'))
