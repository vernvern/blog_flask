# -*- coding:utf-8 -*-

import logging


class Config():
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_INFO_FILE_PATH = './.blog_info.log'
    LOG_LEVEL = logging.NOTSET


class DebugConfig(Config):
    DEBUG = True


class ProductConfig(Config):
    LOG_LEVEL = logging.INFO
