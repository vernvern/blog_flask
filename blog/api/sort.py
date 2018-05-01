# -*- coding=utf-8 -*-

from blog import app
from blog.toolkit.route.route import http
from blog.modules.page import Page


urls = 'api/sort'
page = Page()


@http(methods=['GET'])
def get_sort_list():
    return {'data': page.get_sorts()}
