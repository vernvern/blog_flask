import inspect
import os.path
import functools
import logging

from flask import request

from blog import app


def log(func, rule, **options):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        ret = func(*args, **kw)
        log = '[API] %s\n' % rule
        log += '[Func] %s: %s\n' % (func.__module__, func.__name__)
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


def http(rule=None, **options):

    def decorator(func, rule=rule, options=options):
        ''' 封装flask的路由'''
        # 处理前缀
        try:
            imp = 'from %s import urls' % func.__module__
            exec(imp)
        except ImportError as e:
            profix = '/'.join(func.__module__.split('.')[2:])
        else:
            profix = eval('urls')
        finally:
            if profix[0] != '/':
                profix = '/' + profix
        if rule is None:
            rule = func.__name__
        elif rule.startswith('/'):
            rule = rule[1:]

        # 具体路径
        rule = os.path.join(profix, rule)

        # 写路由
        endpoint = options.pop('endpoint', None)
        app.add_url_rule(rule, endpoint, log(func, rule, **options), **options)
        return func

    return decorator
