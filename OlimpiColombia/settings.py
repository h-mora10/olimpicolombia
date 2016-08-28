"""
Django settings for OlimpiColombia project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '*',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'OlimpiColombiaApp',
    'storages',
    's3_folder_storage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'OlimpiColombia.urls'

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

WSGI_APPLICATION = 'OlimpiColombia.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
#Credenciales para conectarse a la base de datos de PostgreSQL, no subir cambios en esta conexion al repositorio.
#Pueden comentarearlos localmente para dejar la configuracion de cada base local.


####Production
DATABASES = {'default': dj_database_url.config(default= os.environ.get('DATABASE_URL'))}


#####Developement
#DATABASES = {
#   'default': {
#       'ENGINE': 'django.db.backends.postgresql_psycopg2',
#       'NAME': 'OlimpiColombia',
#       'HOST': 'localhost',
#       'PORT': '5432',
#        'USER': 'postgres',
#        'PASSWORD': 'julpipe06',
#   }
# }


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
#STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

# AWS S3 Credentials
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
#AWS_PRELOAD_METADATA = True
#AWS_QUERYSTRING_AUTH = False
#AWS_S3_HOST = os.environ.get('AWS_S3_HOST')

DEFAULT_FILE_STORAGE = os.environ.get('DEFAULTFILES_STORAGE')
DEFAULT_S3_PATH = 'media'
STATICFILES_STORAGE = os.environ.get('STATICFILES_STORAGE')
STATIC_S3_PATH = 'static'

MEDIA_ROOT = '/media/'
MEDIA_URL = os.environ.get('MEDIA_URL')
STATIC_ROOT = '/static/'
STATIC_URL = os.environ.get('STATIC_URL')
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

#Redirect after login
LOGIN_REDIRECT_URL = 'index'

LOGOUT_REDIRECT_URL = 'logged_out'