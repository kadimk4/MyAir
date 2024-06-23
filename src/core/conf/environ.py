from pathlib import Path

import environ

env = environ.Env()
environ.Env.read_env(Path(__file__).resolve().parent.parent.parent.parent, '.env')
