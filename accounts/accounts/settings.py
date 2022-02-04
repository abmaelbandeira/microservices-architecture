"""
Django settings for accounts project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

# .env configuration
from datetime import timedelta

import environ
import os

env = environ.Env()
root_path = environ.Path(__file__) - 2
env.read_env(env_file=root_path(".env"))

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# RabbitMQ
# CLOUDAMQP_URL = env('CLOUDAMQP_URL',
#                     default='amqp://guest:guest@localhost:5672/%2f')
SETTINGS_PATH = env("SETTINGS_PATH", default="")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG", default="False")

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
    'django_filters',
    'drf_spectacular',

    'accounts',
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

    # My Middlewares
    # 'accounts.middleware.CheckTokenIsValidMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'accounts.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'accounts.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DJANGO_DATABASE_URL = env.db("DATABASE_URL")
DATABASES = {"default": DJANGO_DATABASE_URL}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# PASSWORD_HASHERS
PASSWORD_HASHERS = [
    'accounts.hashers.PBKDF2SHA512PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
]

GLOBAL_PEPPER = env("GLOBAL_PEPPER", default="")

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST FRAMEWORK SETTINGS
REST_FRAMEWORK = {
    # YOUR SETTINGS
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend']
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=4),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(hours=4),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

REST_USE_JWT = True
JWT_AUTH_COOKIE = 'jwt-auth'
JWT_AUTH_REFRESH_COOKIE = 'refresh-token'

# DRF SPECTACULAR - DOCUMENTATION SWAGGER SETTINGS
SPECTACULAR_SETTINGS = {
    'TITLE': 'UserUnderProtection API',
    'DESCRIPTION': 'UserUnderProtection API Documentation',
    'VERSION': '1.0.0',
    # OTHER SETTINGS
}

AUTH_USER_MODEL = 'accounts.UserUnderProtection'

# REST_AUTH_SERIALIZERS = {
#     'USER_DETAILS_SERIALIZER':
#         'accounts.serializers.UserUnderProtectionSerializer',
# }

# -----------------------------------------------------------------------------
# Emails
# -----------------------------------------------------------------------------
# Comment when it goes into production
# EMAIL_BACKEND = env(
#     "EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"
# )
# Remove comment below when going to production
EMAIL_USE_TLS = True
EMAIL_HOST = env("EMAIL_HOST", default="smtp.sendgrid.net")
EMAIL_PORT = env("EMAIL_PORT", default="587")
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")
EMAIL_SENDER = env("EMAIL_SENDER", default="")

# EMAIL TEST
EMAIL_TEST_USER = env("EMAIL_TEST_USER", default="")
EMAIL_TEST_PASSWORD = env("EMAIL_TEST_PASSWORD", default="")
