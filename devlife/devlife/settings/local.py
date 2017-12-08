from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env('DJANGO_SECRET_KEY', default='kl^biaul9klceb%@=mvy94)m@^f-c9v=4g+%t#zptzy403-^f6')