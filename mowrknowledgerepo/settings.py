import os
import mimetypes
from pathlib import Path
import cx_Oracle



cx_Oracle.init_oracle_client(lib_dir=r"C:\OracleBase\DjangoOraInstantClient")
# cx_Oracle.init_oracle_client(lib_dir=r"C:\OracleBase\product\19.3.0\instantclient_19_16")
# cx_Oracle.init_oracle_client(lib_dir=r"C:\OracleBase\product\19.3.0\instantclient_21_6")


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Template files Directory
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-08pb8@xtn@ctpm6%*wu+p9w1lyy_l&vg%4f$(a0mytc1f%-dhw'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'knowledgebase',
    'accounts',
    'crispy_forms',
    "debug_toolbar",  # debug_toolbar
]
AUTH_USER_MODEL = 'accounts.CustomUser'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",  # debug_toolbar
]

INTERNAL_IPS = [
    # ...
    "127.0.0.1",  # debug_toolbar
    # ...
]

LANGUAGES = [
    ('bn', 'Bengali'),
    ('en', 'English'),
]

mimetypes.add_type("application/javascript", ".js", True)  # for debug toolbar

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

ROOT_URLCONF = 'mowrknowledgerepo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'mowrknowledgerepo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# live_db
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'MOWKBDB',
        'USER': 'MOWKBAdmin',
        'PASSWORD': 'MoWKb#DbAdmin$22',
        'HOST': '130.180.3.146',
        'PORT': '1521',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'static/'

STATIC_DIR = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [STATIC_DIR]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
