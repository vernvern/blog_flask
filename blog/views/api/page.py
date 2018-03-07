# -*- coding:utf-8 -*-

from flask import request

from blog.toolkit.route.route import http
from blog.modules import page


urls = 'api/page'


@http(methods=['POST'])
def get_page_list():
    keyword = request.form.get('keyword', None)
    page_list = page.get_page_list(keyword)

    return {'data': page_list}


@http(methods=['POST'])
def get_page_detail():
    name = request.form['name']
    data = page.get_page_detail(name)
    return {'data': data}


@http(methods=['POST'])
def get_simple_page_list():
    index = int(request.form.get('index', 1))
    size = int(request.form.get('size', 20))
    return page.get_simple_page_list(index, size)
