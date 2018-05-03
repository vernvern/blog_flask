# -*- coding:utf-8 -*-

import re
import glob
import yaml
import uuid
import arrow

from markdown import markdown

from blog import app


PAGE_PATH = 'blog/data/'


class Page:
    ''' 文章辅助类 '''
    _pages = {}  # {'id': page_dict}
    _singleton = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kw):
        if not cls._singleton:
            cls._singleton = object.__new__(cls, *args, **kw)
        return cls._singleton

    @property
    def pages(self):
        return sorted((p for p in self._pages.values()),
                      key=lambda x: x['date_created'],
                      reverse=True)

    def get_page_list(self, mode='title', index=0, size=0, sort=None):

        page_list = []
        for page in self.pages:
            body = markdown(page['body'],
                            extensions=app.config['EXTENSTIONS'])

            if mode == 'simple':
                preview = re.search(r'<div class="toc">\n<ul>.*</ul>\n</div>',
                                    body, re.S | re.M)
                if preview:
                    body = body[:preview.span()[1]]

            tmp_page = dict(title=page['title'], id=page['id'],
                            body=body, date_created=page['date_created'])
            page_list.append(tmp_page)

        # 分类筛选
        if sort:
            page_list = [p for p in page_list if p['sort'] == sort]

        # 分页
        if index and size:
            start = size * (index - 1)
            end = start + size
            page_list = page_list[start:end]

        return {'data': page_list, 'total': len(self._pages),
                'index': index, 'size': size}

    def get_sorts(self):
        return list(set([p['sort'] for p in self.pages]))

    def get_page(self, _id):
        page = self._pages[_id]
        page['body'] = markdown(
            page['body'], extensions=app.config['EXTENSTIONS'])
        return page

    @staticmethod
    def _split_meta(string):
        ''' 分离md文件的meta和内容

        return meta, body
        '''

        match = re.match(r'-{3,}.*-{3,}', string, re.M | re.S)
        meta = '\n'.join([x for x in match.group().split('\n')][1:-1])
        meta = yaml.load(meta)

        body = string[match.span()[1]:]

        return meta, body

    @classmethod
    def load_pages_data(cls):
        if cls._pages != {}:
            return

        page_path_list = glob.glob(app.config['PAGE_PATH'] + '**/*.md',
                                   recursive=True)
        for page_path in page_path_list:
            path_split = page_path.split('/')

            with open(page_path, 'r+') as f:
                string = f.read()

                if not string.startswith("---"):  # without meta
                    file_name = path_split[-1][:-3]
                    sort = path_split[-2]

                    meta = {
                        'title': file_name,
                        'date_created': arrow.now().to('08:00').for_json(),
                        'date_modified': arrow.now().to('08:00').for_json(),
                        'tags': [],
                        'sort': sort if sort != 'data' else '未分类',
                        'id': str(uuid.uuid4()),
                        'removed': False}
                    body = string

                    # complete meta
                    f.seek(0)
                    f.write("---\n\n" + yaml.dump(meta) + "\n---\n\n" + string)
                else:  # there is meta
                    # split meta
                    meta, body = cls._split_meta(string)

                if meta.get('removed', False):
                    continue

                meta.update({'body': body})
                cls._pages[meta['id']] = meta
