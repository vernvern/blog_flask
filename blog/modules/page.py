# -*- coding:utf-8 -*-

from blog import db
from ..models.page import Page


def get_page_list(keyword=None):
    pages = db.session.query(Page)

    if keyword:
        patern = '%' + str(keyword) + '%'
        pages = pages.filter(Page.title.like(patern))

    return {'data': [p._todict() for p in pages]}


def get_page_detail(id_):
    page = db.session.query(Page).filter_by(id=id_).first()
    return {'data': page._todict()}
