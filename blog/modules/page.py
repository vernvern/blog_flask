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
PAGE_PATH = 'blog/data/'


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


def get_page_list(mode='title'):
    page_path_list = glob.glob(PAGE_PATH + '**/*.md', recursive=True)
    total = len(page_path_list)
    page_list = []
    for page_path in page_path_list:
        file_name = page_path.split('/')[-1][:-3]
        date_modified = arrow.get(os.stat(page_path).st_mtime).for_json()
        with open(page_path, 'r') as f:
            meta, body = split_meta(f.read())
            title = meta['title'] if meta.get('title', False) else file_name
            page = {'date_modified': date_modified,
                    'title': title,
                    'name': file_name}

            # 只返回title
            if mode == 'title':
                pass

            # 返回title和body头部
            elif mode == 'simple':
                toc = re.search('\[TOC\]', body, re.S)
                if toc:
                    body = body[:toc.span()[1]]
                else:
                    preview = re.search(r'\#\#.*\#\#', body, re.S | re.M)
                    if preview:
                        body = preview.group()[:-2]
                # print('\n\n\n', body, '\n', '-'*20)
                body = markdown.markdown(body, extensions=EXTENSTIONS)
                page['body'] = body

            page_list.append(page)
    page_list = sorted(
            page_list, key=lambda x: x['date_modified'], reverse=True)

    return {'data': page_list, 'total': total}


def get_page_detail(name):
    page_path = glob.glob(PAGE_PATH + '**/' + name + '.md', recursive=True)[0]
    date_modified = arrow.get(os.stat(page_path).st_mtime).for_json()
    with open(page_path, 'r') as f:
        meta, body = split_meta(f.read())
        title = meta['title'] if meta.get('title', False) else file_name
        page = {'date_modified': date_modified,
                'date_created': meta['date_created'],
                'title': title,
                'name': name,
                'body': markdown.markdown(body, extensions=EXTENSTIONS)}
        return page

    raise Exception('居然找不到')
