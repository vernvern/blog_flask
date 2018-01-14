# -*- coding:utf-8 -*-

import markdown

from blog import db
from ..models.page import Page


EXTENSTIONS = ['markdown.extensions.extra',
               'markdown.extensions.codehilite',
               'markdown.extensions.tables',
               'markdown.extensions.toc']


def get_page_list(keyword=None):
    pages = db.session.query(Page)

    if keyword:
        patern = '%' + str(keyword) + '%'
        pages = pages.filter(Page.title.like(patern))

    return {'data': [p._todict() for p in pages]}


def get_page_detail(id_):
    page = db.session.query(Page).filter_by(id=id_).first()
    data = page._todict()
    data['body'] = markdown.markdown(data['body'], extenstions=EXTENSTIONS)
    return {'data': data}
