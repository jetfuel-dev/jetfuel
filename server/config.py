import os

PROJECT_ROOT = os.path.dirname(__file__)

SQL_MODE = "sqlite"
SQL_VERSION = 0

DEFAULT_USER = True
DEFAULT_API_KEY = os.environ.get("DEFAULT_API_KEY", "default")
