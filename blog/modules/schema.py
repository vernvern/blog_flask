# -*- coding=utf-8 -*-

import re
import os
import glob
import yaml
import arrow

from blog import app


class SchemaHelper:

    _pages = {}  # {'id': Page object}
    _singleton = None

    def __init__(self):
        SchemaHelper.setup()

    def __new__(cls, *args, **kw):
        if not cls._singleton:
            cls._singleton = object.__new__(cls, *args, **kw)
        return cls._singleton

    def get_page(self, _id):
        return self._pages[_id]

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
    def setup(cls):
        from blog.models.schema import PageQL

        if cls._pages != {}:
            return

        page_path_list = glob.glob(
            os.path.join(app.config['PAGE_PATH'], '**/*.md'),
            recursive=True
        )
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
                cls._pages[meta['id']] = PageQL(**meta)
