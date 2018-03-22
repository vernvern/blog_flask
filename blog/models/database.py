# -*- coding=utf-8 -*-

import redis

from blog.config import Config
from blog.toolkit.tool import singleton


@singleton
class RedisManager:
    pool_dict = {}

    def __call__(self, db):
        pool = self.pool_dict.get(db, False)
        if not pool:
            pool = redis.ConnectionPool(
                host=Config.REDIS_IP, port=Config.REDIS_PORT, db=db)
            self.pool_dict[db] = pool
        return redis.StrictRedis(connection_pool=pool)
