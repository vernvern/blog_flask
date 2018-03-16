# -*- coding=utf-8 -*-

import redis
from blog.config import Config


class RedisManager(dict):
    def __getitem__(self, key, *args, **kw):
        try:
            return super(RedisManager, self).__getitem__(key, *args, **kw)
        except KeyError as e:
            rds = redis.Redis(
                    host=Config.REDIS_IP, port=Config.REDIS_IP, db=key)
            self.setdefault(key, rds)
            return super(RedisManager, self).__getitem__(key, *args, **kw)
