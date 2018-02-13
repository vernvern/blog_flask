import time
import logging

from flask import Flask, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import request

from . import settings

app = Flask(__name__)


class MyResponse(Response):
    @classmethod
    def force_type(cls, response, environ=True):
        if isinstance(response, dict):
            if not response.get('code', False):
                response['code'] = '0'

            if not response.get('data', False):
                response['data'] = []

            if not response.get('index', False):
                response['index'] = 1

            if not response.get('size', False):
                response['size'] = len(response['data'])

            if not response.get('total', False):
                response['total'] = len(response['data'])

            log = '[Methods] %s\n' % request.method
            log += '[Log Level] into_200'
            log += '[Return Args]:\n'
            args = ['    %s: %s' % (k, v) for k, v in response.items()]
            log += '\n'.join(args)

            # 返回参数日志 info_200
            app.logger.info(log)

            response = jsonify(response)
        return super(Response, cls).force_type(response, environ)


# log
handler = logging.FileHandler(settings.LOG_ADDRESS, encoding='UTF-8')
formatter = logging.Formatter(
        '\n\n\n------------------------- \n'
        '%(levelname)s %(asctime)s \n %(message)s')
handler.setFormatter(formatter)

# return format
app.response_class = MyResponse

# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# log
app.logger.addHandler(handler)

# 加载数据表
from blog.models.page import *

# 注册url
import blog.views.views
import blog.views.api.page
