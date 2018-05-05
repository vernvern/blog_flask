# -*- coding=utf-8 -*-

from flask import request

from blog import app


@app.errorhandler(500)
def raise_error(e):
    app.logger.exception(e)
    return '500', 500


@app.before_request
def log_request():
    ''' 请求日志
    '''
    log = ''
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


@app.after_request
def log_response(response):
    ''' 响应成功日志
    '''
    log = '[HTTP Code] %s\n' % response.status
    log += '[Return]\n'
    args = response.data.decode('utf-8')
    log += args

    app.logger.info(log)
    return response


@app.teardown_request
def log_response(exc):
    ''' 响应失败日志
    '''
    if exc:
        app.logger.error(exc)
