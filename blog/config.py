# -*- coding:utf-8 -*-

import logging


class Config():
    DEBUG = False
    TESTING = False
    LOG_INFO_FILE_PATH = './.blog_info.log'
    LOG_LEVEL = logging.NOTSET
    REDIS_IP = '172.18.0.3'
    REDIS_PORT = 6379


class DebugConfig(Config):
    DEBUG = True


class ProductConfig(Config):
    LOG_LEVEL = logging.INFO
