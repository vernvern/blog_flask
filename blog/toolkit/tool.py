# -*- coding=utf-8 -*-


def singleton(cls, *args, **kw):
    ''' 使用装饰器实现单例模式 '''
    cls_list = {}

    def _singleton(*args, **kw):
        if cls not in cls_list:
            cls_list[cls] = cls(*args, **kw)
        return cls_list[cls]
    return _singleton
