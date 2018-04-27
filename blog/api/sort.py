# -*- coding=utf-8 -*-

from blog.models.database import RedisManager
from blog.toolkit.route.route import http
from blog import app


urls = 'api/sort'

rds = RedisManager()


@http(methods=['GET'])
def get_sort_list():
    sorts = [rds(app.config['REDIS_DB_SORT']).keys('*')
    return [x.decode('utf-8') for x in sorts]
