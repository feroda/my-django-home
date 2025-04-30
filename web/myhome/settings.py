import os
import environ
from pathlib import Path

from django.conf.locale.it import formats as it_formats

env = environ.Env(
    DEBUG=(bool, False),
    EMAIL_BACKEND=(str, "django.core.mail.backends.console.EmailBackend"),
    EMAIL_USE_TLS=(bool, True),
    EMAIL_USE_SSL=(bool, False),
    EMAIL_HOST=(str, "mail"),
    HOSTNAMEs=(str, '*'),
    UI_PATH=(str, 'ui/'),
)

environ.Env.read_env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")
MY_IOT_ENV = env("MY_IOT_ENV")
MY_IOT_PROJECT = env("MY_IOT_PROJECT")

BASE_URL = env("BASE_URL")
if not BASE_URL.endswith("/"):
    BASE_URL += "/" 
API_BASE_URL = f"{BASE_URL}api/"
UI_PATH = env("UI_PATH")
ALLOWED_HOSTS = env("HOSTNAMEs").split(",")
CSRF_TRUSTED_ORIGINS = [ BASE_URL[:-1] ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'web',
    'django.contrib.sites',
    'widget_tweaks',
    'captcha',
]

SECURE_CROSS_ORIGIN_OPENER_POLICY = None  # Needed to close Oauth2 popup

TG_BOT_TOKEN = env("TELEGRAM_BOT_TOKEN")

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myhome.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myhome.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://redis:6379',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    'formatters': {
        'verbose': {
            'format': '{asctime} {levelname} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'timestamp': {
            'format': '{asctime} {name}.{levelname} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {asctime} {message}',
            'style': '{',
        },
        'app': {
            '()': 'django.utils.log.ServerFormatter',
            'style': '{',
            'format': '[{server_time}] {message}'
        }
    },
    'handlers': {
        'app': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'app'
        },
        'console': {
            'level': os.getenv('DJANGO_LOG_LEVEL', 'WARNING'),
            'class': 'logging.StreamHandler',
            'formatter': 'timestamp'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / f"{MY_IOT_PROJECT}.log",
            'maxBytes': 10000000,
            'backupCount': 9999999,
            'formatter': 'simple',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ["require_debug_false"],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        }
    },
    'loggers': {
        'myhome': {
            'handlers': ['app'],
            'level': 'INFO',
            'propagate': False
        },
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins',],
            'level': 'ERROR',
            'propagate': True,
        },
        'myhome.commands': {
            'handlers': ['mail_admins',],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

CAPTCHA_LENGTH = 6
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'it'
TIME_ZONE = 'Europe/Rome'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'STATIC'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'MEDIA'

# AUTH_USER_MODEL = 'web.User'



# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
