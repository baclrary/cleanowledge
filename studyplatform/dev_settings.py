from .settings import *

DEBUG = True
ALLOWED_HOSTS = []

LOGGING["loggers"]["django.db.backends"]["level"] = "DEBUG"

CACHES["default"]["BACKEND"] = "django.core.cache.backends.filebased.FileBasedCache"
SESSION_ENGINE = "django.contrib.sessions.backends.file"
