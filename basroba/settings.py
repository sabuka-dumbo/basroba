from pathlib import Path
import os
import dj_database_url
import cloudinary

# ----------------------------
# Base directory
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------
# Security
# ----------------------------
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "unsafe-secret-key")
DEBUG = os.environ.get("DJANGO_DEBUG", "False") == "False"
ALLOWED_HOSTS = ["*"]

# ----------------------------
# Installed apps
# ----------------------------
INSTALLED_APPS = [
    "app",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "modeltranslation",
    "cloudinary",
    "cloudinary_storage",
]

# ----------------------------
# Middleware
# ----------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'app.middleware.LanguageRedirectMiddleware',
]

ROOT_URLCONF = "basroba.urls"

# ----------------------------
# Templates
# ----------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
            ],
        },
    },
]

WSGI_APPLICATION = "basroba.wsgi.application"

# ----------------------------
# Database
# ----------------------------
DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get(
            "DATABASE_URL",
            "postgresql://neondb_owner:npg_ikPsUJe1Z8Ab@ep-cold-bonus-agulcmoz-pooler.c-2.eu-central-1.aws.neon.tech:5432/neondb"
        ),
        conn_max_age=600,
        ssl_require=True,
    )
}

# ----------------------------
# Auth
# ----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

AUTH_USER_MODEL = "app.User"

# ----------------------------
# Internationalization
# ----------------------------
USE_I18N = True
USE_TZ = True
TIME_ZONE = "UTC"

LANGUAGE_CODE = "en"
LANGUAGES = [
    ('en', 'English'),
    ('ka', 'ქართული'),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ----------------------------
# Static files
# ----------------------------
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ----------------------------
# Media files
# ----------------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# ----------------------------
# Cloudinary configuration
# ----------------------------
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.environ.get("CLOUDINARY_CLOUD_NAME", "672893682634297"),
    "API_KEY": os.environ.get("CLOUDINARY_API_KEY", "o5NFe6MTWWyEGUfx3fPyYiavdZI"),
    "API_SECRET": os.environ.get("CLOUDINARY_API_SECRET", "o5NFe6MTWWyEGUfx3fPyYiavdZI"),
}

# Use Cloudinary for media files in production
if not DEBUG:
    DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
    MEDIA_URL = "/media/"