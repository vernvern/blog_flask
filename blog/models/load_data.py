# -*- coding=utf-8 -*-

import re
import glob
import uuid
import yaml
import arrow

from .database import RedisManager
from blog import app


PAGE_PATH = 'blog/data/'


def _split_meta(string):
    ''' 分离md文件的meta和内容

    return meta, body
    '''

    match = re.match(r'-{3,}.*-{3,}', string, re.M | re.S)
    meta = '\n'.join([x for x in match.group().split('\n')][1:-1])
    meta = yaml.load(meta)

    body = string[match.span()[1]:]

    return meta, body


def load_pages_data():
    rds = RedisManager()
    page_path_list = glob.glob(PAGE_PATH + '**/*.md', recursive=True)
    page_list = []
    for page_path in page_path_list:
        path_split = page_path.split('/')

        if 'hide' in path_split:
            continue

        with open(page_path, 'r+') as f:
            string = f.read()

            if not string.startswith("---"):  # without meta
                file_name = path_split[-1][:-3]
                sort = path_split[-2]

                meta = {'title': file_name,
                        'date_created': arrow.now().to('08:00').for_json(),
                        'date_modified': arrow.now().to('08:00').for_json(),
                        'tags': [],
                        'sort': sort if sort != 'data' else '未分类',
                        'id': str(uuid.uuid4())}

                # complete meta
                f.seek(0)
                f.write("---\n\n" + yaml.dump(meta) + "\n---\n\n" + string)
            else:  # there is meta
                # split meta
                meta, body = _split_meta(string)

            # load into redis
            rds_dict = meta.copy()
            rds_dict['body'] = string

            _id = rds_dict.pop('id')
            sort = rds_dict.pop('sort')
            tags = rds_dict.pop('tags')

            # page
            rds(app.config['REDIS_DB_PAGE']).hmset(_id, rds_dict)

            # sort
            rds(app.config['REDIS_DB_SORT']).zadd(
                sort, float(arrow.get(rds_dict['date_created']).timestamp), _id)

            # tags
            for tag in tags:
                rds(app.config['REDIS_DB_TAGS']).zadd(
                    tag, float(arrow.get(rds_dict['date_created']).timestamp), _id)


if __name__ == '__main__':
    load_pages_data()
