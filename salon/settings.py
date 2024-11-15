"""
Django settings for salon project.

Generated by 'django-admin startproject' using Django 3.2.25.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
import dj_database_url

# CORS settings
CORS_ALLOWED_ORIGINS = []
if "CLIENT_ORIGIN" in os.environ:
    CORS_ALLOWED_ORIGINS.extend(
        [
            os.environ.get("CLIENT_ORIGIN"),
            os.environ.get("CLIENT_ORIGIN_DEV"),
        ]
    )
else:
    CORS_ALLOWED_ORIGIN_REGEXES = [
        r"^https://.*\.codeinstitute-ide\.net$",
    ]

if os.path.isfile("env.py"):
    import env

# Build paths inside the project like this: os.path.join(BASE_DIR,...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = (
    os.environ.get("ALLOWED_HOSTS", "").split(",")
    if os.environ.get("ALLOWED_HOSTS")
    else []
)

# Additional allowed hosts for development and production
ALLOWED_HOSTS.extend(
    [
        "8000-josseyo-salon-s8mmgxdiu91.ws.codeinstitute-ide.net",
        "salon-talks-af192748bd52.herokuapp.com",
    ]
)

CSRF_TRUSTED_ORIGINS = [
    "https://8000-josseyo-salon-s8mmgxdiu91.ws.codeinstitute-ide.net",
    "https://salon-talks-af192748bd52.herokuapp.com",
]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "home",
    "products",
    "bag",
    "checkout",
    "profiles",
    "crispy_forms",
    "storages",
    "faq",
    "about",
    "subscribe",
    "contact",
    "csp",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "csp.middleware.CSPMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "salon.urls"

CRISPY_TEMPLATE_PACK = "bootstrap4"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
            os.path.join(BASE_DIR, "templates", "allauth"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
                "bag.contexts.bag_contents",
            ],
            "builtins": [
                "crispy_forms.templatetags.crispy_forms_tags",
                "crispy_forms.templatetags.crispy_forms_field",
            ],
        },
    },
]

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = "/accounts/login"
LOGIN_REDIRECT_URL = "/"

# Email Configuration
if "DEVELOPMENT" in os.environ:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    DEFAULT_FROM_EMAIL = "salon@example.com"
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")  # Heroku config var
    EMAIL_HOST_PASSWORD = os.environ.get(
        "EMAIL_HOST_PASS"
    )  # Heroku config var
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # Using the EMAIL_HOST_USER directly
    ADMIN_EMAIL = "josefin@yomaco.com"

# Optional: Check if the required environment variables are set
if not EMAIL_HOST_USER or not EMAIL_HOST_PASSWORD:
    raise ValueError(
        "Please set the EMAIL_HOST_USER and "
        "EMAIL_HOST_PASSWORD environment variables."
    )


WSGI_APPLICATION = "salon.wsgi.application"

# Database Configuration
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Database
if "DATABASE_URL" in os.environ:
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation." "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# https://docs.djangoproject.com/en/3.2/howto/static-files/

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

SESSION_ENGINE = "django.contrib.sessions.backends.db"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# AWS S3 Configuration
if "USE_AWS" in os.environ:
    AWS_S3_OBJECT_PARAMETERS = {
        "Expires": "Thu, 31 Dec 2099 20:00:00 GMT",
        "CacheControl": "max-age=94608000",
    }
    AWS_STORAGE_BUCKET_NAME = "salontalks-e6485414bbd3"
    AWS_S3_REGION_NAME = "eu-north-1"
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

    # Static and media files
    STATICFILES_STORAGE = "custom_storages.StaticStorage"
    STATICFILES_LOCATION = "static"
    DEFAULT_FILE_STORAGE = "custom_storages.MediaStorage"
    # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    MEDIAFILES_LOCATION = "media"

    # Override static and media URLs in production
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/"

# Stripe Configuration
DISCOUNT_THRESHOLD = 50
DISCOUNT_PERCENTAGE = 10
STRIPE_CURRENCY = "usd"
STRIPE_PUBLIC_KEY = os.getenv("STRIPE_PUBLIC_KEY", "")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
STRIPE_WH_SECRET = os.getenv("STRIPE_WH_SECRET", "")


# Content Security Policy
CSP_DEFAULT_SRC = (
    "'self'",
)

CSP_SCRIPT_SRC = (
    "'self'",
    "cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.min.js",
    "stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js",
    "cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js",
    "js.stripe.com",
    "kit.fontawesome.com",
    "salontalks-e6485414bbd3.s3.eu-north-1.amazonaws.com/static/",
    "salontalks-e6485414bbd3.s3.amazonaws.com/static/faq/js/faq.js",
    "salontalks-e6485414bbd3.s3.amazonaws.com/static/checkout/js/stripe_elements.js",
)

CSP_STYLE_SRC = (
    "'self'",
    "'unsafe-inline'",
    "stackpath.bootstrapcdn.com",
    "fonts.googleapis.com",
    "cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css",
    "salontalks-e6485414bbd3.s3.eu-north-1.amazonaws.com/static/",
    "salontalks-e6485414bbd3.s3.amazonaws.com/static/css/base.css",
    "salontalks-e6485414bbd3.s3.amazonaws.com/static/checkout/css/checkout.css",
)

CSP_FONT_SRC = (
    "'self'",
    "fonts.gstatic.com",
    "ka-f.fontawesome.com",
    "js.stripe.com/type-font/Colfax-Medium.woff",
)

CSP_IMG_SRC = (
    "'self'",
    "data:",
    "salontalks-e6485414bbd3.s3.amazonaws.com",
)

CSP_FRAME_SRC = ("'self'", "https://js.stripe.com")
CSP_CONNECT_SRC = (
    "'self'",
    "api.stripe.com",
    "ka-f.fontawesome.com",  # Allow Font Awesome connections
)

# Ensure to add 'unsafe-inline' to script sources if needed
CSP_SCRIPT_SRC += ("'unsafe-inline'",)
CSP_STYLE_SRC += ("js.stripe.com",)
