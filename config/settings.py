import os
import dj_database_url

from decouple import config, Csv

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static'),
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'price_monitor',
	'price_monitor.product_advertising_api',
	'rest_framework',
]

MIDDLEWARE_CLASSES = [
	# Simplified static file serving.
	# https://warehouse.python.org/project/whitenoise/
	'whitenoise.middleware.WhiteNoiseMiddleware'
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
	'default': {
		'ENGINE': config('DB_ENGINE'),
		'NAME': config('DB_NAME'),
		'USER': config('DB_USER'),
		'PASSWORD': config('DB_PASSWORD'),
		'HOST': config('DB_HOST'),
		'PORT': config('DB_PORT', cast=int),
	}
}

# HEROKU: Update database configuration with $DATABASE_URL.
# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/
LANGUAGE_CODE = config('LANGUAGE_CODE')
TIME_ZONE = config('TIME_ZONE')
USE_I18N = config('USE_I18N', cast=bool)
USE_L10N = config('USE_L10N', cast=bool)
USE_TZ = config('USE_TZ', cast=bool)


# Email
# EMAIL_HOST = config('EMAIL_HOST', default='localhost')
# EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
# EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
# EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)


# Celery
BROKER_URL = ...
CELERY_RESULT_BACKEND = ...
CELERY_ACCEPT_CONTENT = ['pickle', 'json']
CELERY_CHORD_PROPAGATES = True


# Rest-Framework for Angular
REST_FRAMEWORK = {
	'PAGINATE_BY': 50,
	'PAGINATE_BY_PARAM': 'page_size',
	'MAX_PAGINATE_BY': 100,
}


# base url to the site
PRICE_MONITOR_BASE_URL = 'http://localhost:8000'

# AMAZON:
# Product Advertising API
PRICE_MONITOR_AWS_ACCESS_KEY_ID = config('AMZN_ACCESS_KEY')
PRICE_MONITOR_AWS_SECRET_ACCESS_KEY = config('AMZN_SECRET_KEY')
PRICE_MONITOR_AMAZON_PRODUCT_API_ASSOC_TAG = config('AMZN_ASSOCIATE_TAG')

# Name of site
PRICE_MONITOR_AMAZON_ASSOCIATE_NAME = 'admin/krakn.cc'

# Possible region values: CA, CN, DE, ES, FR, IT, JP, UK, US
PRICE_MONITOR_AMAZON_PRODUCT_API_REGION = 'US'

# Amazon site being used, choose from on of the following
PRICE_MONITOR_AMAZON_ASSOCIATE_SITE = 'amazon.com'

# Domain to use for image serving.
# https://images-<REGION>.ssl-images-amazon.com
PRICE_MONITOR_AMAZON_SSL_IMAGE_DOMAIN = 'https://images-us.ssl-images-amazon.com'

# Set to True if using HTTPS URLs for Amazon images.
PRICE_MONITOR_IMAGES_USE_SSL = False

# SYNCHRONIZATION
# Time after which products will be refreshed
# Amazon allows caching for up to 24 hours (1440 minutes)
PRICE_MONITOR_AMAZON_PRODUCT_REFRESH_THRESHOLD_MINUTES = 720


# NOTIFICATIONS
# time after which to notify the user again about a price limit hit (in minutes)
PRICE_MONITOR_SUBSCRIPTION_RENOTIFICATION_MINUTES = 10080  # 7 days

# sender address of the notification email
PRICE_MONITOR_EMAIL_SENDER = 'noreply@localhost'

# currency name to use on notifications
PRICE_MONITOR_DEFAULT_CURRENCY = 'USD'

# subject and body of the notification emails
gettext = lambda x: x
PRICE_MONITOR_I18N_EMAIL_NOTIFICATION_SUBJECT = gettext(
	'Price limit for %(product)s reached'
)
PRICE_MONITOR_I18N_EMAIL_NOTIFICATION_BODY = gettext(
	'The price limit of %(price_limit)0.2f %(currency)s has been reached for the '
	'article "%(product_title)s" - the current price is %(price)0.2f %(currency)s.'
	'\n\nPlease support our platform by using this '
	'link for buying: %(link)s\n\n\nRegards,\nThe Team'
)

# name of the site in notifications
PRICE_MONITOR_SITENAME = 'Krakn Price Trakn'

# CACHING
# None disables caching.
PRICE_MONITOR_GRAPH_CACHE_NAME = None

# prefix for cache key used for graphs
PRICE_MONITOR_GRAPH_CACHE_KEY_PREFIX = 'graph_'