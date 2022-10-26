# Internationalization settings
# https://docs.djangoproject.com/en/3.0/topics/i18n/
import os

from project.settings import MIDDLEWARE
from project.components.base import BASE_DIR


# Middleware settings
MIDDLEWARE += ('django.middleware.locale.LocaleMiddleware', )

gettext = lambda s: s

LANGUAGE_CODE = 'ru'

LANGUAGES = (
    ('ru', gettext('Russian')),
)

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True
