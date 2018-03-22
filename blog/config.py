# -*- coding:utf-8 -*-

import logging


class Config():
    DEBUG = False
    TESTING = False
    LOG_INFO_FILE_PATH = '/opt/log/stdout.log'
    LOG_ERROR_FILE_PATH = '/opt/log/stderr.log'
    LOG_LEVEL = logging.INFO
    REDIS_IP = '192.168.1.3'
    REDIS_PORT = 6379
    REDIS_DB_PAGE = 0
    REDIS_DB_SORT = 1
    REDIS_DB_TAGS = 2


class DebugConfig(Config):
    DEBUG = True
    LOG_LEVEL = logging.NOTSET


class ProductConfig(Config):
    pass
