# -*- coding: utf-8 -*-
"""Application configuration."""
import os
from walle.config.settings import Config

class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    ENV = 'test'
    DEBUG = True
    DB_NAME = 'walle_python'
    # Put the db file in project root
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    BCRYPT_LOG_ROUNDS = 4  # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
    WTF_CSRF_ENABLED = False  # Allows form testing
    DEBUG_TB_ENABLED = True
    ASSETS_DEBUG = True  # Don't bundle/minify static assets
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.

    #email config
    MAIL_SERVER = 'smtp.exmail.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_DEFAULT_SENDER = 'service@walle-web.io'
    MAIL_USERNAME = 'service@walle-web.io'
    MAIL_PASSWORD = 'Ki9y&3U82'

    LOG_PATH = os.path.join(Config.PROJECT_ROOT, 'logs')
    LOG_PATH_ERROR = os.path.join(LOG_PATH, 'error.log')
    LOG_PATH_INFO = os.path.join(LOG_PATH, 'info.log')
    LOG_PATH_DEBUG = os.path.join(LOG_PATH, 'debug.log')
    LOG_FILE_MAX_BYTES = 100 * 1024 * 1024
    # 轮转数量是 10 个
    LOG_FILE_BACKUP_COUNT = 10
    LOG_FORMAT = "%(asctime)s %(thread)d %(message)s"


    LOCAL_SERVER_HOST = '127.0.0.1'
    LOCAL_SERVER_USER = 'wushuiyong'
    LOCAL_SERVER_PORT = 22

    SQLALCHEMY_ECHO = True