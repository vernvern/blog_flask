# -*- coding=utf-8 -*-

import uuid
import arrow


class Page:

    def __init__(self, **kw):
        self.title = kw.get(title, None)
        self.body = kw.get(body, None)
        self.date_created = kw.get(date_created,
                                   arrow.now().to('08:00').for_json())
        self.date_modified = kw.get(date_modified,
                                    arrow.now().to('08:00').for_json())
        self.tags = kw.get(tags, [])
        self.sort = kw.get(sort, '未分类')
        self.id = kw.get(uuid, str(uuid.uuid4()))
        self.removed = kw.get(removed, False)
