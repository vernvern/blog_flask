
import logging
from flask_sqlalchemy import SQLAlchemy
from flask import Response, jsonify

from blog import app

# ---------------------------------------------------   log配置

LOG_ADDRESS = './.blog_info.log'

handler = logging.FileHandler(LOG_ADDRESS, encoding='UTF-8')
formatter = logging.Formatter(
        '\n\n\n------------------------- \n'
        '%(levelname)s %(asctime)s \n %(message)s')
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)

# log
app.logger.addHandler(handler)


# ---------------------------------------------  SQLAlchemy

SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# --------------------   views函数返回python对象时，处理成json格式


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


# return format
app.response_class = MyResponse
