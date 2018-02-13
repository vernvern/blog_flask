
import sys
import arrow
import logging

from flask_sqlalchemy import SQLAlchemy
from flask import Response, jsonify, request

from blog import app


# ---------------------------------------------------   log配置

LOG_ADDRESS = './.blog_info.log'

# 去掉默认的handler
for tmp_handler in app.logger.handlers:
    app.logger.removeHandler(tmp_handler)


# 自定义filter
class AppFilter(logging.Filter):
    def filter(self, record):
        record.datetime = arrow.now().to('08:00').for_json()
        return True


app_filter = AppFilter()

# 日志输入formatter
formatter = logging.Formatter(
        '\n[Level] %(levelname)s\n[DateTime] %(datetime)s\n' +
        '%(message)s\n')

# info 文件日志
info_file_handler = logging.FileHandler(LOG_ADDRESS, encoding='UTF-8')
info_file_handler.addFilter(app_filter)
info_file_handler.setLevel(logging.INFO)
info_file_handler.setFormatter(formatter)

# debug console日志
info_console_handler = logging.StreamHandler(sys.stdout)
info_console_handler.addFilter(app_filter)
info_console_handler.setLevel(logging.DEBUG)
info_console_handler.setFormatter(formatter)

# 添加handler
app.logger.addHandler(info_file_handler)
app.logger.addHandler(info_console_handler)


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
            log += '\n\n\n'

            # 返回参数日志 info_200
            # app.logger.info(log)

            response = jsonify(response)
        return super(Response, cls).force_type(response, environ)


# return format
app.response_class = MyResponse
