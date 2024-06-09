from pathlib import Path
import os
import dj_database_url
from django_storage_url import dsn_configured_storage_class

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    "anymail",
    "equipment",
    "evidence",
    "fontawesomefree",
    "news",
    "pages",
    "team",
    "django_recaptcha",
    "wagtailcaptcha",
    "wagtail.contrib.styleguide",
    "wagtail.contrib.table_block",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sitemaps",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.legacy.sitemiddleware.SiteMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

sentry_dsn = os.environ.get("SENTRY_DSN", "")
if sentry_dsn:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    def ignore_disallowedhost(event, hint):
        if event.get("logger", None) == "django.security.DisallowedHost":
            return None
        return event

    sentry_sdk.init(
        dsn=sentry_dsn,
        before_send=ignore_disallowedhost,
        integrations=[DjangoIntegration()],
        release=os.environ.get("GIT_COMMIT", "develop"),
        environment=os.environ.get("STAGE", "local"),
        traces_sample_rate=0.2,
    )

ROOT_URLCONF = "urls"

SECRET_KEY = os.environ.get("SECRET_KEY", "<a string of random characters>")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG") == "True"

DIVIO_DOMAIN = os.environ.get("DOMAIN", "")
DIVIO_DOMAIN_ALIASES = [
    d.strip() for d in os.environ.get("DOMAIN_ALIASES", "").split(",") if d.strip()
]
DIVIO_DOMAIN_REDIRECTS = [
    d.strip() for d in os.environ.get("DOMAIN_REDIRECTS", "").split(",") if d.strip()
]

ALLOWED_HOSTS = [DIVIO_DOMAIN] + DIVIO_DOMAIN_ALIASES + DIVIO_DOMAIN_REDIRECTS

CSRF_TRUSTED_ORIGINS = [
    os.environ.get("CSRF_TRUSTED_ORIGINS", default="https://flinthillsparanormal.com")
]

# Redirect to HTTPS by default, unless explicitly disabled
SECURE_SSL_REDIRECT = os.environ.get("SECURE_SSL_REDIRECT") != "False"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "wsgi.application"

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite://:memory:")

DATABASES = {"default": dj_database_url.parse(DATABASE_URL)}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"
USE_I18N = True
USE_TZ = True

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = ["static"]

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media files
# DEFAULT_FILE_STORAGE is configured using DEFAULT_STORAGE_DSN

# read the setting value from the environment variable
DEFAULT_STORAGE_DSN = os.environ.get("DEFAULT_STORAGE_DSN")

# dsn_configured_storage_class() requires the name of the setting
DefaultStorageClass = dsn_configured_storage_class("DEFAULT_STORAGE_DSN")

# Django's DEFAULT_FILE_STORAGE requires the class name
DEFAULT_FILE_STORAGE = "settings.DefaultStorageClass"

# only required for local file storage and serving, in development
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join("/data/media/")

WAGTAIL_SITE_NAME = "Flint Hills Paranormal"
WAGTAILADMIN_BASE_URL = "https://flinthillsparanormal.com/"

# DJANGO ANYMAIL
ANYMAIL = {
    "MAILGUN_API_KEY": os.environ.get("MAILGUN_API_KEY", default=""),
    "MAILGUN_SENDER_DOMAIN": os.environ.get("MAILGUN_SENDER_DOMAIN", default=""),
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", default="do.not.reply@flinthillsparanormal.com")
SERVER_EMAIL = os.environ.get("SERVER_EMAIL", default="do.not.reply@flinthillsparanormal.com")

RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY", default="")
RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY", default="")
NOCAPTCHA = True

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
PREPEND_WWW = False

# Make low-quality but small images
WAGTAILIMAGES_JPEG_QUALITY = 40
WAGTAILIMAGES_WEBP_QUALITY = 45
WAGTAIL_ENABLE_WHATS_NEW_BANNER = False
