from .settings import *

DEBUG = True
ALLOWED_HOSTS = []

LOGGING["loggers"]["django.db.backends"]["level"] = "DEBUG"
