# -*- coding:utf-8 -*-

from flask import request

from blog.toolkit.route.route import http
from blog.modules import page


urls = 'api/page'


@http(methods=['POST'])
def get_page_list():
    keyword = request.form.get('keyword', None)
    ret = page.get_page_list(keyword)
    return ret


@http(methods=['POST'])
def get_page_detail():
    id_ = request.form['id']
    return page.get_page_detail(id_)


@http(methods=['POST'])
def get_simple_page_list():
    index = int(request.form.get('index', 1))
    size = int(request.form.get('size', 20))
    return page.get_simple_page_list(index, size)
