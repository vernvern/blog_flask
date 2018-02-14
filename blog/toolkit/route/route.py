import os.path

from blog import app
from blog.settings import log_request


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
        app.add_url_rule(
            rule, endpoint, log_request(func, rule, **options), **options)
        return func

    return decorator
