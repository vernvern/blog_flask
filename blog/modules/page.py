# -*- coding:utf-8 -*-

import re

import markdown

from blog import db
from ..models.page import Page


EXTENSTIONS = ['markdown.extensions.extra',
               'markdown.extensions.codehilite',
               'markdown.extensions.tables',
               'markdown.extensions.toc']


def get_page_list(keyword=None):
    pages = db.session.query(Page).filter_by(is_show=True) \
                      .order_by(Page.date_create.desc())

    if keyword:
        patern = '%' + str(keyword) + '%'
        pages = pages.filter(Page.title.like(patern))

    return {'data': [p._todict() for p in pages.all()]}


def get_page_detail(id_):
    page = db.session.query(Page).filter_by(id=id_).first()
    data = page._todict()
    data['body'] = markdown.markdown(data['body'], extensions=EXTENSTIONS)
    return {'data': data}


def get_simple_page_list(index=1, size=20):
    ''' 获取带简略信息的文章列表 '''
    pages = db.session.query(Page) \
              .filter_by(is_show=True) \
              .order_by(Page.date_create.desc())

    total = pages.count()

    pages = pages.slice((index - 1) * size, index * size).all()
    for page in pages:
        toc = re.search('\[TOC\]', page.body, re.S)
        if toc:
            page.body = page.body[:toc.span()[1]]
        else:
            sd_sd_title = re.search('(\#\#.*\#\#{1})', page.body, re.S)
            if sd_sd_title:
                page.body = page.body[:sd_sd_title.span()[1] - 2]
        page.body = markdown.markdown(page.body, extensions=EXTENSTIONS)
    return {'data': [p._todict() for p in pages],
            'index': index,
            'size': size,
            'total': total}
