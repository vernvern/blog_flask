# -*- coding=utf-8 -*-

from blog.toolkit.route.route import http
from blog.modules.page import PageHelper


urls = 'api/sort'
page = PageHelper()


@http(methods=['GET'])
def get_sort_list():
    return {'data': page.get_sorts()}
