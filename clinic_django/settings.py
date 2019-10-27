"""
Django settings for clinic_django project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{asctime} {module}.{funcName} {lineno:3} {levelname:7} => {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'SECRET_KEY') or 'django-insecure-3m1&01(u1ysowe8f%#9b63l@7kg&yvjgfwe9g2tuiw7l5)!1%*'

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get('DJANGO_PRODUCTION'):
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = ['*', ]


if DEBUG:
    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ALLOW_HEADERS = [
        'accept',
        'accept-encoding',
        'authorization',
        'content-type',
        'dnt',
        'origin',
        'user-agent',
        'x-csrftoken',
        'x-requested-with',
        'x-api-key',
    ]
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'django_celery_beat',
    'django_celery_results',
    'django_cas_ng',
    'clinic.apps.ClinicConfig',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_cas_ng.middleware.CASMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
ROOT_URLCONF = 'clinic_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'clinic_admin', 'dist'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

if DEBUG:
    TEMPLATES[0]["DIRS"] = [os.path.abspath(os.path.join(
        BASE_DIR, os.path.pardir, 'clinic_admin', 'dist'))] + TEMPLATES[0]["DIRS"]
    # TEMPLATES[0]["DIRS"] = [os.path.abspath(os.path.join(
    # BASE_DIR, os.path.pardir, 'clinic_docs', 'docs', '.vuepress', 'dist'))] + TEMPLATES[0]["DIRS"]

WSGI_APPLICATION = 'clinic_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('POSTGRES_DATABASE_NAME') or os.environ.get('DJANGO_DATABASE_NAME') or 'clinic',
            'USER': 'postgres',
            'PASSWORD': os.environ.get('POSTGRES_ENV_POSTGRES_ROOT_PASSWORD') or os.environ.get('DJANGO_DATABASE_PASSWORD') or 'example',
            'HOST': os.environ.get('POSTGRES_PORT_3306_TCP_ADDR') or os.environ.get('DJANGO_DATABASE_HOST') or 'db',
            'PORT': '5432',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_cas_ng.backends.CASBackend',
)

CAS_SERVER_URL = "https://login.bitnp.net/cas/"
if DEBUG:
    CAS_SERVER_URL = 'https://login.bit.edu.cn/devcas/'

CAS_LOGIN_MSG = None
CAS_LOGGED_MSG = None
CAS_REDIRECT_URL = '/manage/'

AUTH_USER_MODEL = 'clinic.ClinicUser'
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}
STATIC_ROOT = '/usr/share/nginx/html/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "clinic_admin", "dist"),
    os.path.join(BASE_DIR, "clinic_docs", "docs", ".vuepress", "dist"),
]
if DEBUG:
    STATICFILES_DIRS = [os.path.abspath(
        os.path.join(BASE_DIR, os.path.pardir, 'clinic_docs', 'docs', '.vuepress', 'dist')),
        os.path.abspath(
        os.path.join(BASE_DIR, os.path.pardir, 'clinic_admin', 'dist'))] + STATICFILES_DIRS

apikey = os.environ.get('apikey') or "oh-my-tlb"

EMAIL_HOST = os.environ.get('EMAIL_HOST') or 'mail.bit.edu.cn'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER') or ''
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD') or ''
# EMAIL_PORT = 465
# EMAIL_USE_SSL = True

if DEBUG:
    CELERY_BROKER_URL = 'amqp://guest:guest@localhost//'
else:
    CELERY_BROKER_URL = 'amqp://guest:guest@mq//'

# celery beat配置
# CELERY_ENABLE_UTC = False

# CELERY_ENABLE_UTC = False
CELERY_TIMEZONE = TIME_ZONE
# DJANGO_CELERY_BEAT_TZ_AWARE = False
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_RESULT_BACKEND = 'django-db'
