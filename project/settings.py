"""Project settings"""
import os

from split_settings.tools import optional, include


DEBUG = True

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4)xgm#p_7)&iuek_qjcm+&+l&^8stqanzfz)h)@#9xgukk-0@^'

# Middleware settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Application definition
INSTALLED_APPS = [
    # Castom theme for admin-panel
    'simpleui',

    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # Auth
    'allauth',
    'allauth.account',

    # Wrapper phonenumbers
    'phonenumber_field',

    # Project applications
    'apps.chat',
    'apps.index',
    'apps.profile',
    'apps.publications',
]

include(
    # BASE SETTINGS FROM PROJECT
    'components/base.py',
    'components/session.py',

    # AUTHENTIFICATION SETTINGS
    'components/account.py',


    # CUSTOM ADMIN
    'components/simple_ui.py',

    # DATABASE SETTINGS
    # 'components/database/mysql.py',
    # 'components/database/postgresql.py',
    # 'components/database/redis.py',
     'components/database/sqlite.py',

    # INTERNATIONALIZATION SETTINGS
    'components/internationalization.py',

    # SMTP SETTINGS
    'components/smtp.py',

    # WYSIWYG EDITORS SETTINGS
    'components/ckeditor.py',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
if DEBUG:
    STATIC_DIR = os.path.join(os.path.dirname(BASE_DIR), 'static')
    STATICFILES_DIRS = [STATIC_DIR]
else:
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')
