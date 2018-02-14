
import sys
import arrow
import logging
import functools

from flask import Response, jsonify, request

from blog import app


# ---------------------------------------------------   log配置


# 去掉默认的handler
for tmp_handler in app.logger.handlers:
    app.logger.removeHandler(tmp_handler)

# 设置日志级别
if not app.debug and app.config['LOG_LEVEL']:
    app.logger.setLevel(app.config['LOG_LEVEL'])


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
info_file_handler = logging.FileHandler(app.config['LOG_INFO_FILE_PATH'],
                                        encoding='UTF-8')
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


def log_request(func, rule, **options):
    ''' api 请求日志
    '''
    @functools.wraps(func)
    def wrapper(*args, **kw):
        ret = func(*args, **kw)
        log = '[API] %s\n' % request.path
        log += '[Func] %s.%s\n' % (func.__module__, func.__name__)
        log += '[Methods] %s\n' % request.method
        if request.method == 'POST' and request.form.keys():
            args = ['    %s: %s' % (k, v) for k, v in request.form.items()]
            log += '[Args]\n'
            log += '\n'.join(args)
        elif request.method == 'GET' and dict(request.args.keys()):
            args = ['    %s: %s' % (k, v) for k, v in request.args.items()]
            log += '[Args]\n'
            log += '\n'.join(args)
        # 调用接口 log
        app.logger.info(log)
        return ret
    return wrapper


def log_api_200(response, message):
    ''' api 200 日志
    '''
    log = '[API] %s\n' % request.path
    log += '[Methods] %s\n' % request.method
    log += '[HTTP Code] %s\n' % response.status_code
    log += '[Return]\n'
    log += message
    return log


# api 500 日志


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
                response['size'] = 0

            if not response.get('total', False):
                response['total'] = 0

            args = ['    %s: %s' % (k, v) for k, v in response.items()]
            message = '\n'.join(args)

            response = jsonify(response)

            message = log_api_200(response, message)

            # 返回参数日志 info_200
            app.logger.info(message)

        return super(Response, cls).force_type(response, environ)


# return format
app.response_class = MyResponse
