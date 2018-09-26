# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCaseSchema::test_blog_title 1'] = {
    'data': {
        'page': {
            'id': '1a2467e3-bc16-4e75-a432-4ad35796975f',
            'title': 'hexo在github上搭建博客'
        }
    }
}

snapshots['TestCaseSchema::test_blog_title 2'] = {
    'data': {
        'page': {
            'id': '1a2467e3-bc16-4e75-a432-4ad35796975f'
        }
    }
}
