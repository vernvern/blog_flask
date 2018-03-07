# -*- coding:utf-8 -*-

import re
import os
import glob
import yaml
import arrow

import markdown


EXTENSTIONS = ['markdown.extensions.extra',
               'markdown.extensions.codehilite',
               'markdown.extensions.tables',
               'markdown.extensions.toc']


def split_meta(string):
    ''' 分离md文件的meta和内容

    return meta, body
    '''
    ret_meta = {'date_created': '居然忘记写',
                'tags': []}

    match = re.match(r'-{3,}.*-{3,}', string, re.M | re.S)
    if match:
        meta = '\n'.join([x for x in match.group().split('\n')][1:-1])
        meta = yaml.load(meta)

        ret_meta.update(meta)
        body = string[match.span()[1]:]
    else:
        body = string

    return ret_meta, body


def get_page_list(keyword=None):
    page_path_list = glob.glob('blog/data/**/*.md', recursive=True)
    page_list = []
    for page_path in page_path_list:
        title = page_path.split('/')[-1][:-3]
        date_modified = arrow.get(os.stat(page_path).st_mtime).for_json()
        with open(page_path, 'r') as f:
            meta, _ = split_meta(f.read())
            title = meta['title'] if meta.get('title', False) else title
            page = {'date_modified': date_modified,
                    'title': title}
            page_list.append(page)
    page_list = sorted(page_list, key=lambda x: x['date_modified'], reverse=True)

    return page_list


def get_page_detail(id_):
    # page = db.session.query(Page).filter_by(id=id_).first()
    # data = page._todict()
    # data['body'] = markdown.markdown(data['body'], extensions=EXTENSTIONS)
    # return {'data': data}
    return {}


def get_simple_page_list(index=1, size=20):
    ''' 获取带简略信息的文章列表 '''
    # pages = db.session.query(Page) \
    #           .filter_by(is_show=True) \
    #           .order_by(Page.date_create.desc())

    # total = pages.count()

    # pages = pages.slice((index - 1) * size, index * size).all()
    # for page in pages:
    #     toc = re.search('\[TOC\]', page.body, re.S)
    #     if toc:
    #         page.body = page.body[:toc.span()[1]]
    #     else:
    #         sd_sd_title = re.search('(\#\#.*\#\#{1})', page.body, re.S)
    #         if sd_sd_title:
    #             page.body = page.body[:sd_sd_title.span()[1] - 2]
    #     page.body = markdown.markdown(page.body, extensions=EXTENSTIONS)
    # return {'data': [p._todict() for p in pages],
    #         'index': index,
    #         'size': size,
    #         'total': total}
    return {}
