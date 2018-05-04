# -*- coding:utf-8 -*-

import logging


class Config():
    DEBUG = False
    TESTING = False
    LOG_INFO_FILE_PATH = '/opt/log/stdout.log'
    LOG_ERROR_FILE_PATH = '/opt/log/stderr.log'
    LOG_LEVEL = logging.INFO
    PAGE_PATH = 'blog/data/'

    # markdown
    EXTENSTIONS = ['markdown.extensions.extra',
                   'markdown.extensions.codehilite',
                   'markdown.extensions.tables',
                   'markdown.extensions.toc']


class DebugConfig(Config):
    DEBUG = True
    LOG_LEVEL = logging.NOTSET


class ProductConfig(Config):
    pass
