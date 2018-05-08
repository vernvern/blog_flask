# -*- coding:utf-8 -*-

from flask import request

from blog.toolkit.route.route import http
from blog.modules.page import Page


urls = 'api/page'
page = Page()


@http(methods=['POST'])
def get_page_list():
    size = int(request.form.get('size', 0))
    sort = request.form.get('sort', None)
    index = int(request.form.get('index', 0))
    return page.get_page_list(index=index, size=size, sort=sort)


@http(methods=['POST'])
def get_page_detail():
    _id = request.form['id']
    _page = page.get_page(_id)
    return {'data': _page.__dict__}


@http(methods=['POST'])
def get_simple_page_list():
    index = int(request.form.get('index', 1))
    size = int(request.form.get('size', 20))
    return page.get_page_list(mode='simple', index=index, size=size)
