# -*- coding: utf-8 -*-
"""
Django settings for Operations project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import os

import djcelery
djcelery.setup_loader()  # 加载djcelery

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r2kh_(4ewg#(dnoyl8eh5^6y&lw@m=y7o(n!a(i1q0&r&j=0*='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rest_framework',

    'firstapp',
    'djcelery',
    'channels',
    # 'kombu.transport.django',
    'corsheaders',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # 跨域中间件
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'firstapp.middleware.CustomAuthorizeMiddleWare',
    'firstapp.middleware.CustomExceptionMiddleWare',
    'firstapp.middleware.CustomDecryptMiddleWare',
)

ROOT_URLCONF = 'Operations.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'Operations.wsgi.application'

# Host local
local_host = '127.0.0.1'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# mysql_host = '193.168.0.91'
mysql_host = local_host
DATABASES_OPTIONS = {
    "MYSQL": {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': mysql_host,
        'PORT': 3306,
        'NAME': 'operations',
        'USER': 'root',
        'PASSWORD':  'root',
    },
    "SQLITE": {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'media/localfiles/monitor.sqlite3'),
    },
    "SAMBA_SQLITE": {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': "Y:\\tinystorage",
    },
}

DATABASES = {
    'default': DATABASES_OPTIONS["MYSQL"]
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# 设置项是否开启URL访问地址后面不为/跳转至带有/的路径
APPEND_SLASH = True
# 自定义用户模型
AUTH_USER_MODEL = 'firstapp.User'
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)

# global config
SYSTEM_NAME = u"四方科技资源管理系统"
SYSTEM_VERSIONS = u"1.0"
SYSTEM_COPYRIGHT = u"成都四方信息技术有限公司平台组"
LOCK_TIME = 5    # 锁定时间限制(单位是分钟)
LOGIN_FAILED_TIMES_LIMIT = 5    # 密码错误限制次数
LOGIN_TIME_OUT = 30  # 登录超时（单位是秒）
VERIFY_IMG_URL = '/media/verify/verify.jpg'  # 验证码生成url
VERIFY_IMG_PATH = os.path.join(BASE_DIR, 'media', 'verify', 'verify.jpg')  # 验证码生成路径
API_ENCRYPT = False  # 是否对api数据机密
API_DECRYPT = False  # 是否对api前端传过来的数据解密
PAGE_SIZE = 10  # 分页大小
WEB_URL_PREFIX = 'operations'  # 最后没有斜杠，项目中不能出现此开头的路径，否则不能重定向
LOGIN_URL = "/login/"
LOGOUT_URL = "/logout/"
TIME_FORMAT = "%Y-%m-%d %H:%M:%S"  # 格式化时间格式化
GIT_REPO_PATH = os.path.abspath('/git_tmp_file/')
# 正式环境
# RANCHER_ACCESS_KEY = '2F6FA7CEF8C4A1D1C896'
# RANCHER_SECRET_KEY = 'nV7zB8rsszZcpKebQnou8NtQQVcAuPQxUKyfzt85'
# 983226B4FB727C4BB969
# 7U23TpkRnnAS2wJ47C26yXkuk1HY8NwDUcGK1yi9
# 测试开发环境
RANCHER_ACCESS_KEY = '2B678BF6DA2629916E25'
RANCHER_SECRET_KEY = 'EMpw28rxpmrm5iqZXVYDC7QcEY2AQiRhFNquvK3H'

# 和风天气配置
HEWEATHER_URL = 'https://free-api.heweather.com/s6/weather/now?key=4656f4c7fce74951bd8ac781dab867e9&location='

# cors config
CORS_ORIGIN_ALLOW_ALL = True  # 全部接受，白名单将会无效。
CORS_ALLOW_CREDENTIALS = True  # 允许跨域验证
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'cookie',
    'access-control-allow-credentials',
    'sessionid',
    'x-requested-with',
)

# session config
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 24 * 60 * 60  # 会话cookie过期时间（秒）
SESSION_COOKIE_HTTPONLY = False  # 会话是否使用httponly，如果为true，js将无法获取会话cookie
SESSION_TIME_OUT = 48 * 60 * 60


# cache config
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',  # 给缓存放置的内存区设置一个名字
        'TIMEOUT': 600,
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = WEB_URL_PREFIX + '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collectstatic')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# media files
MEDIA_URL = WEB_URL_PREFIX + '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# rest_framework config
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    # 'EXCEPTION_HANDLER': 'firstapp.cust_exceptions.custom_exception_handler',
    # 'PAGINATE_BY':10,
    # 'PAGINATE_BY_PARAM':'page_size',
    # 'MAX_PAGINATE_BY':100,
}

# Celery settings
# redis_host = local_host
redis_host = '193.168.0.91'
redis_password = 'root'
BROKER_URL = 'redis://:{0}@{1}:6379/'.format(redis_password, redis_host)
BROKER_POOL_LIMIT = 0

#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'  # 使用django-celery后台

# In settings.py
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgiref.inmemory.ChannelLayer",
        "ROUTING": "Operations.routing.channel_routing",
    },
}

# log config
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(MEDIA_ROOT, 'tempfiles', 'logs', 'debug.log'),
        },
        'running': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(MEDIA_ROOT, 'tempfiles', 'logs', 'info.log'),
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True
        },
        'info': {
            'handlers': ["running"],
            'level': 'INFO',
            'propagate': True
        }
    }
}