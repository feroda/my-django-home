
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
    POSTGRES_PORT=(int, 5432),
    SQL_SERVER_PORT=(int, 1433),
    HOSTNAMEs=(str, '*'),
    DEFAULT_NEWSLETTER_FROM_ADDRESS=(str, 'notizie@confartigianatoimprese.net'),
    UI_PATH=(str, 'ui/'),
    SHARED_IMPORT_SUBDIR=(str, '000_IMPORT/')
)

environ.Env.read_env()

SHARED_DIR = '/shared/'
IMPORT_DIR = os.path.join(SHARED_DIR, env("SHARED_IMPORT_SUBDIR"))
DATA_UPLOAD_MAX_NUMBER_FIELDS = 20000

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ADHOC_LOGIN_USERNAME = env("ADHOC_LOGIN_USERNAME")
ADHOC_LOGIN_PASSWORD = env("ADHOC_LOGIN_PASSWORD")
ADHOC_LOGIN_COMPANY = env("ADHOC_LOGIN_COMPANY")
ADHOC_BASE_URL = env("ADHOC_BASE_URL")
ADHOC_DATA_CACHE_TIMEOUT = 14400

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

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
    'django.contrib.postgres',
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    # 'rest_framework_simplejwt',
    # 'django_q',
    'web',
    'location_field.apps.DefaultConfig',
    'i4h',
    'tgbot',
    'aziende',
    'inapa',
    'caaf',
    'anap',
    'cenpi',
    'settore_sistema',
    'adhoc',
    'persone',
    'leads',
    'axga',
    'zucchetti_adhoc',
    'django.contrib.sites',
    'microsoft_auth',
    'm365',
    'segmenti',
    'widget_tweaks',
    'captcha',
    'django_celery_beat',
    'django_celery_results',
    'simple_history',
    'django.contrib.staticfiles'
]

SECURE_CROSS_ORIGIN_OPENER_POLICY = None  # Needed to close Oauth2 popup

TG_BOT_TOKEN = env("TELEGRAM_BOT_TOKEN")

SITE_ID = 1

LOCATION_FIELD = {
    'map.provider': 'openstreetmap',
    'map.zoom': 8,
    'search.provider': 'nominatim',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'noicrm.middleware.UpdateRequestUserMiddleware',
    'noicrm.middleware.RedirectToHomeIfUnauthorized',
]

if MY_IOT_ENV == "dev":
    LIVERELOAD_HOST = "web-livereload"
    INSTALLED_APPS.insert(INSTALLED_APPS.index('django.contrib.staticfiles')-1, 'livereload')
    MIDDLEWARE.append('livereload.middleware.LiveReloadScript')
    PROFILER = False
    # CORS_ALLOWED_ORIGINS = [ "http://127.0.0.1:3000", "http://localhost:3000"]
    CORS_ORIGIN_ALLOW_ALL = True
else:
    CORS_ORIGIN_ALLOW_ALL = False

ROOT_URLCONF = 'noicrm.urls'
X_FRAME_OPTIONS = "SAMEORIGIN"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates' ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'microsoft_auth.context_processors.microsoft',
                'noicrm.context_processors.export_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'noicrm.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("POSTGRES_DB"),
        'USER': env("POSTGRES_USER"),
        'PASSWORD': env("POSTGRES_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': env("POSTGRES_PORT"),
    },
    'sqlite3': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'mssql': {
        'ENGINE': "mssql",
        'NAME': env("SQL_SERVER_DB"),
        'USER': env("SQL_SERVER_USER"),
        'PASSWORD': env("SQL_SERVER_PASSWORD"),
        'HOST': env("SQL_SERVER_IP"),
        'PORT': env("SQL_SERVER_PORT"),
        "OPTIONS": {
            "driver": "ODBC Driver 18 for SQL Server", 
            "extra_params": "TrustServerCertificate=yes"
        },
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
        'noicrm': {
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
        'noicrm.commands': {
            'handlers': ['mail_admins',],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

AUTH_GROUPS_TO_SECTIONS_PATH = {
    "caaf": ["caaf", "persone"],
    "inapa": ["inapa", "persone"],
    "anap": ["persone"],
    "persone": ["persone"],
    "dirigenza": ["persone", "reports"],
    "promotori": ["tasks-promotori", "segnalazioni"],
    "operatori": ["tasks-operatori"],
    "users": ["persone"],
}

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'it'

TIME_ZONE = 'Europe/Rome'

USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'STATIC'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'MEDIA'

AUTH_USER_MODEL = 'web.User'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TGPOLL_DEFAULT_WEIGHTED_OPTIONS = [
    {"value": -20, "text": "Arrabbiata/o", "icon": "😡👊🏻"},
    {"value": -10, "text": "Triste", "icon": "😭🙈"},
    {"value": 0, "text": "Spaventata/o", "icon": "😱🤞🏻"},
    {"value": 10, "text": "In progress...", "icon": "🐣👍🏻"},
    {"value": 20, "text": "Alla grande!", "icon": "😁🤟🏻"}]

TGPOLL_DEFAULT_WEIGHTED_OPTIONS = [
    {"value": -20, "text": "Arrabbiata/o", "icon": "😡👊🏻"},
    {"value": -10, "text": "Triste", "icon": "😭🙈"},
    {"value": 0, "text": "Ho mille domande per la testa!", "icon": "😱🤞🏻"},
    {"value": 10, "text": "Curiosa/o", "icon": "😊👌🏻"},
    {"value": 20, "text": "Sto già imparando...", "icon": "🐣👍🏻"},
    {"value": 30, "text": "Alla grande!", "icon": "😁🤟🏻"}]


SHORT_DATE_FORMAT = "d/m/Y"
SHORT_DATETIME_FORMAT = "d/m/Y H:i"
DATE_FORMAT = "d/m/Y"
DATETIME_FORMAT = "d/m/Y H:i"
it_formats.DATETIME_FORMAT = "D d M Y H:i"
USE_THOUSAND_SEPARATOR = False
THOUSAND_SEPARATOR = "."
NUMBER_GROUPING = 3
DECIMAL_SEPARATOR = ","

EMAIL_BACKEND=env("EMAIL_BACKEND")
EMAIL_HOST=env("EMAIL_HOST")
EMAIL_PORT=env("EMAIL_PORT")
EMAIL_HOST_USER=env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD=env("EMAIL_HOST_PASSWORD")
DEBUG_EMAIL_CONTACT=env("DEBUG_EMAIL_CONTACT")

DEFAULT_NEWSLETTER_FROM_ADDRESS=env("DEFAULT_NEWSLETTER_FROM_ADDRESS")

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'url_filter.integrations.drf.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
    ),
    'EXCEPTION_HANDLER': 'noicrm.drf.utils.exception_handler',
}
handler500 = 'rest_framework.exceptions.server_error'

AUTHENTICATION_BACKENDS = [
    'microsoft_auth.backends.MicrosoftAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend' # if you also want to use Django's authentication
]

# values you got from step 2 from your Mirosoft app
MICROSOFT_AUTH_CLIENT_ID = env('MICROSOFT_AUTH_CLIENT_ID')
MICROSOFT_AUTH_CLIENT_SECRET = env('MICROSOFT_AUTH_CLIENT_SECRET')
# Tenant ID is also needed for single tenant applications
MICROSOFT_AUTH_TENANT_ID = env('MICROSOFT_AUTH_TENANT_ID')

# Microsoft authentication
# include Microsoft Accounts, Office 365 Enterprise and Azure AD accounts
MICROSOFT_AUTH_LOGIN_TYPE = 'ma'

# --- CAAF: scadenze per servizio ----

CAAF_SERVICE_EXPIRE = {
    "730": {
        "exprire_kind": "dates",
        "dates": ["09/30"],
        "to_notify": True,
        "notify_days": 180,
        "notify_interval": "weekly",
    },
    "REDDITI": {
        "exprire_kind": "dates",
        "dates": ["09/30"],
        "to_notify": True,
        "notify_days": 180,
        "notify_interval": "weekly",
    },
    "DSU": {
        "exprire_kind": "yearly",
        "dates": [],
        "to_notify": True,
        "notify_days": 120,
        "notify_interval": "weekly",
    },
    "IMU": {
        "exprire_kind": "dates",
        "dates": ["06/16", "12/16"],
        "to_notify": True,
        "notify_days": 45,
        "notify_interval": "weekly",
    },
    "SUCC_ONLINE": {
        "exprire_kind": None,
        "dates": [],
        "to_notify": False,
        "notify_days": None,
        "notify_interval": None,
    },
    "SUCC_MOD4": {
        "exprire_kind": None,
        "dates": [],
        "to_notify": False,
        "notify_days": None,
        "notify_interval": None,
    },
    "BONUS": {
        "exprire_kind": None,
        "dates": [],
        "to_notify": False,
        "notify_days": None,
        "notify_interval": None,
    }
}

# --- DRIVER DI IMPORTAZIONE DOCUMENTI
IMPORT_DRIVERS_CHOICES = (
    ("command", "Django command"),
    ("caaf.ImportPraticaQWEB", "QWEB - Aggiorna Pratiche"),
    ("caaf.ImportPersonaQWEB", "QWEB - Aggiorna Persone"),
    ("caaf.ImportFatturaQWEB", "QWEB - Aggiorna Fatture"),
    ("cenpi.ImportPersonaEPraticaCENPI", "CENPI - Aggiorna Persone e Pratiche"),
    ("settore_sistema.ImportPersonaEPraticaSISTEMA", 
            "SISTEMA - Aggiorna Persone da Eventi Confartigianato"),
    ("inapa.ImportPersonaEPraticaGAP", "GAP - Aggiorna Persone e Pratiche"),
    ("inapa.ImportScadenzePersonaGAP", "GAP - Aggiorna Scadenzario"),
    ("anap.InitPersonaEPraticaANAP", "ANAP - Inizializza Persone e Pratiche"),
    ("anap.ImportPersonaEPraticaANAP", "ANAP - Aggiorna Persone e Pratiche"),
    ("persone.ImportPersonaPAGHE", "PAGHE - Aggiorna Persone di Aziende a servizio Paghe"),
    ("persone.ImportSegmentiPERSONE", "PERSONE - Aggiorna Segmenti Persone"),
    ("web.ImportUsersHR", "HR - Aggiorna Utenti Confartigianato"),
    ("zucchetti_adhoc.ImportFonteADHOC", 
            "ADHOC - Aggiorna da ADHOC (Tabellone, Trattative e Appuntamenti)"),
    ("axga.ImportCategoryTABELL1", "TABELLONE - Aggiorna Categorie Aziende da Tabellone"),
    ("axga.ImportPlaceTABELL1", "TABELLONE - Aggiorna Luoghi da Tabellone"),
    ("axga.ImportPersonEAziendaTABELL1", "TABELLONE - Aggiorna Persone e Aziende da Tabellone"),
    ("axga.ImportSegmentiTABELL1", "TABELLONE - Aggiorna Segmenti Aziende da Tabellone"),
)

# SECTORS = ["INAPA", "CAAF", "ANAP", "CENPI", "SANARTI", "ANCOS", "PAGHE", "ADHOC"]
SECTORS = ["INAPA", "CAAF", "ANAP", "PAGHE", "ADHOC", "CENPI", "SISTEMA"]

# Celery Configuration Options
CELERY_TIMEZONE = "Europe/Rome"
CELERY_TASK_TRACK_STARTED = True
# CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True

CELERY_BROKER_URL = "redis://redis:6379/0"
CELERY_RESULT_BACKEND = "redis://redis:6379/0"

CELERY_CACHE_BACKEND = 'django-cache'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

