

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = lambda *x: os.path.join(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir, os.path.pardir)).
    replace('\\', '/'), *x)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('DEBUG', '1')))

ALLOWED_HOSTS = [
    'oxd.gluu.org',
    'devaccount.gluu.org',
    '159.203.83.70',
    '104.236.58.43',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_countries',
    'social.apps.django_app.default',
    'account',
    'payment',
    'gluu_license',
    'gluu_ecommerce'
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

ROOT_URLCONF = 'gluu_ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR('templates')],
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


WSGI_APPLICATION = 'gluu_ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config()
}

# Authentication

AUTH_USER_MODEL = 'account.EcommerceUser'

AUTHENTICATION_BACKENDS = (
    'account.authentication.GluuOAuth2Backend',
    'django.contrib.auth.backends.ModelBackend'
)

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'account.authentication.sync_phone_number'
)

SOCIAL_AUTH_POST_LOGOUT_REDIRECT_URL = os.environ.get('SOCIAL_AUTH_POST_LOGOUT_REDIRECT_URL')
SOCIAL_AUTH_END_SESSION_ENDPOINT = 'https://idp.gluu.org/oxauth/seam/resource/restv1/oxauth/end_session'

GLUU_OAUTH2_CLIENT_ID = os.environ.get('GLUU_OAUTH2_CLIENT_ID_V2')
GLUU_OAUTH2_CLIENT_SECRET = os.environ.get('GLUU_OAUTH2_CLIENT_SECRET_V2')
SOCIAL_AUTH_GLUU_KEY = os.environ.get('SOCIAL_AUTH_GLUU_KEY_V2')
SOCIAL_AUTH_GLUU_SECRET = os.environ.get('SOCIAL_AUTH_GLUU_SECRET_V2')

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

STATIC_ROOT = 'static'
STATIC_URL = '/static/'

MEDIA_ROOT = 'media/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    BASE_DIR('staticfiles'),
)

# Logging ==========================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s] [%(asctime)s] [%(funcName)s line: %(lineno)d] - %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'log_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR('logs/django.log'),
            'maxBytes': '16777216',  # 16Mb
            'formatter': 'verbose'
        },
        'idp_log': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR('logs/idp.log'),
            'maxBytes': '16777216',  # 16Mb
            'formatter': 'verbose'
        },
        'billing_log': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR('logs/billing.log'),
            'maxBytes': '16777216',  # 16Mb
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['log_file', 'console'],
            'level': 'DEBUG',
            'propagate': True
        },
        'idp': {
            'handlers': ['idp_log'],
            'level': 'INFO'
        },
        'billing': {
            'handlers': ['billing_log'],
            'level': 'INFO'
        },
    }
}

if bool(int(os.environ.get('SELF_SIGNED_CERT', '1'))):
    VERIFY_SSL = os.environ.get('SELF_SIGNED_CERT_PATH')
else:
    VERIFY_SSL = True

HTTPS = bool(int(os.environ.get('HTTPS', '1')))

if HTTPS:
    os.environ['HTTPS'] = 'on'
    PROTOCOL = 'https'
else:
    PROTOCOL = 'http'

DOMAIN = os.environ.get('DOMAIN')

# Emails
LIVE_EMAIL = bool(int(os.environ.get('LIVE_EMAIL', '1')))

if LIVE_EMAIL:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_FILE_PATH = '/tmp/email-messages/'
EMAIL_USE_TLS = bool(int(os.environ.get('EMAIL_USE_TLS', '1')))
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', '587'))

DEFAULT_FROM_EMAIL = 'Gluu support <support@gluu.org>'

BILLING_EMAIL = 'Gluu billing <billing@gluu.org>'
BILLING_BCC = 'will@gluu.org'
NEW_ACCOUNT_EMAIL = 'will@gluu.org'
EMAIL_HOST_USER_BILLING = os.environ.get('EMAIL_HOST_USER_BILLING')
EMAIL_HOST_PASSWORD_BILLING = os.environ.get('EMAIL_HOST_PASSWORD_BILLING')

RECIPIENT_TEST_EMAIL = os.environ.get('RECIPIENT_TEST_EMAIL')
TEST_TEXT_EMAIL = bool(int(os.environ.get('TEST_TEXT_EMAIL', '0')))

# SCIM and UMA
SCIM_TEST_MODE = bool(int(os.environ.get('SCIM_TEST_MODE', '1')))

if SCIM_TEST_MODE:
    SCIM_TEST_MODE_ACCESS_TOKEN = os.environ.get('SCIM_TEST_MODE_ACCESS_TOKEN')

else:
    UMA_CLIENT_ID = os.environ.get('UMA_CLIENT_ID')
    UMA_CLIENT_SECRET = os.environ.get('UMA_CLIENT_SECRET')

# Stripe Payments
STRIPE_API_KEY = os.environ.get('STRIPE_API_KEY')
STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')

LOGIN_URL = '/login/gluu/'

# Business Logic
PRICE_PER_LICENSE = float(os.environ.get('PRICE_PER_LICENSE', 0.33))
MOCK_LICENSE = bool(int(os.environ.get('MOCK_LICENSE', '1'))) & DEBUG
