"""
Django settings for samplecms project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'home',
    'search',
    'kb',
    'streams',
    
    'wagtail.api.v2',
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtailinventory',

    'modelcluster',
    'taggit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_python3_ldap',

    'rest_framework',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

SECRET_KEY = os.environ.get("SECRET_KEY", 'adminTest')

 #####             ####
### LDAP SETTINGS ###
 #####             ####
AUTHENTICATION_BACKENDS = [
    "django_python3_ldap.auth.LDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
]

# The URL of the LDAP server.
# localhost is placeholder remove and replace with actual auth URL
LDAP_AUTH_HOST = '10.231.19.10'
LDAP_AUTH_PORT = 389
LDAP_AUTH_URL = 'ldap://{host}:{port}'.format(
    host=LDAP_AUTH_HOST,
    port=LDAP_AUTH_PORT,
)
#"LDAP://mmisdc01.centrilogic.internal:389/DC=centrilogic,DC=internal"

# Initiate TLS on connection.
LDAP_AUTH_USE_TLS = False

# The LDAP search base for looking up users.
LDAP_AUTH_SEARCH_BASE = "dc=centrilogic,dc=internal"

# The LDAP class that represents a user.
LDAP_AUTH_OBJECT_CLASS = "user" #"inetOrgPerson"


LDAP_AUTH_FORMAT_USERNAME = "django_python3_ldap.utils.format_username_active_directory_principal"
LDAP_AUTH_ACTIVE_DIRECTORY_DOMAIN = "centrilogic.com"

# User model fields mapped to the LDAP
# attributes that represent them.
LDAP_AUTH_USER_FIELDS = {
    "username": "sAMAccountName",
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
}

# try this if the above settings doesnt work
# below more catered around openLDAP instead though
# LDAP_AUTH_USER_FIELDS = {
#     "username": "uid",
#     "first_name": "givenName",
#     "last_name": "sn",
#     "email": "mail",
# }

# A tuple of django model fields used to uniquely identify a user.
LDAP_AUTH_USER_LOOKUP_FIELDS = ("username",)

# Path to a callable that takes a dict of {model_field_name: value},
# returning a dict of clean model data.
# Use this to customize how data loaded from LDAP is saved to the User model.
LDAP_AUTH_CLEAN_USER_DATA = "django_python3_ldap.utils.clean_user_data"
# Path to a callable that takes a user model and a dict of {ldap_field_name: [value]},
# and saves any additional user relationships based on the LDAP data.
# Use this to customize how data loaded from LDAP is saved to User model relations.
# For customizing non-related User model fields, use LDAP_AUTH_CLEAN_USER_DATA.
LDAP_AUTH_SYNC_USER_RELATIONS = "django_python3_ldap.utils.sync_user_relations"
# Path to a callable that takes a dict of {ldap_field_name: value},
# returning a list of [ldap_search_filter]. The search filters will then be AND'd
# together when creating the final search filter.
LDAP_AUTH_FORMAT_SEARCH_FILTERS = "django_python3_ldap.utils.format_search_filters"
# The LDAP username and password of a user for querying the LDAP database for user
# details. If None, then the authenticated user will be used for querying, and
# the `ldap_sync_users` command will perform an anonymous query.
LDAP_AUTH_CONNECTION_USERNAME = None
LDAP_AUTH_CONNECTION_PASSWORD = None

# Set connection/receive timeouts (in seconds) on the underlying `ldap3` library.
LDAP_AUTH_CONNECT_TIMEOUT = None
LDAP_AUTH_RECEIVE_TIMEOUT = None

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django_python3_ldap": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}

 #####             ####
### END LDAP SETTINGS ###
 #####             ####

ROOT_URLCONF = 'samplecms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'samplecms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# belos is for standard sqlite3 db
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# my sql implementation
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.getenv('MYSQL_DATABASE'),
#         'USER': os.getenv('MYSQL_USER'),
#         'PASSWORD': os.getenv('MYSQL_PASSWORD'),
#         'HOST': '127.0.0.1', #'db',
#         'PORT': 3306,
#     },
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wagtail',
        'HOST': 'mysql',
        # 'PORT': '3306',
        'USER': 'mysqladmin',
        'PASSWORD': 'cladmin',
        'OPTIONS': {
            'sql_mode': 'traditional',
            'init_command': 'SET innodb_strict_mode=1',
            'charset': 'utf8mb4',
        },
    },
}

# Use Elasticsearch as the search backend for extra performance and better search results
# below is default for elastic
# WAGTAILSEARCH_BACKENDS = {
#     'default': {
#         'BACKEND': 'wagtail.search.backends.elasticsearch2',#'wagtail.search.backends.db',
#         'URLS': ['http://localhost:9200'],
#         'INDEX': 'wagtail',
#         'TIMEOUT': 5,
#         'OPTIONS': {},
#         'INDEX_SETTINGS': {},
#     },
# }

# this is for default search via db type
WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.search.backends.db',
    }
}

# Configure Elasticsearch, if present in os.environ
ELASTICSEARCH_ENDPOINT = os.getenv('ELASTICSEARCH_ENDPOINT', '')

# if ELASTICSEARCH_ENDPOINT:
#     from elasticsearch import RequestsHttpConnection
#     WAGTAILSEARCH_BACKENDS = {
#         'default': {
#             'BACKEND': 'wagtail.search.backends.elasticsearch2',
#             'ATOMIC_REBUILD': True,
#             'AUTO_UPDATE': True,
#             'HOSTS': [{
#                 'host': ELASTICSEARCH_ENDPOINT,
#                 'port': 9200,#int(os.getenv('ELASTICSEARCH_PORT', '9200')),
#                 # 'use_ssl': os.getenv('ELASTICSEARCH_USE_SSL', 'off') == 'off',
#                 # 'verify_certs': os.getenv('ELASTICSEARCH_VERIFY_CERTS', 'off') == 'off',
#             }],
#             'OPTIONS': {
#                 'connection_class': RequestsHttpConnection,
#             },
#         }
#     }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# Javascript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/2.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Wagtail settings

WAGTAIL_SITE_NAME = "samplecms"
# WAGTAILDOCS_DOCUMENT_MODEL = 'home.CustomDocument'

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://centrilogickb.com'
