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
            'id': '1a2467e3-bc16-4e75-a432-4ad35796975f',
            'sort': '未分类'
        }
    }
}

snapshots['TestCaseSchema::test_get_pages_with_sort 1'] = {
    'data': {
        'getPagesBySort': [
            {
                'id': 'b0b9c5c4-011f-4c62-bc6c-9c348e40148d',
                'title': '在django上应用sphinx生成文档'
            },
            {
                'id': 'ab48e67f-5bc1-4342-9cc0-dc7920e38be3',
                'title': 'celeryInDjango'
            },
            {
                'id': '4d36570e-68c4-42f9-b106-bc50225b4f51',
                'title': 'add_xiaobing_in_wechat'
            }
        ]
    }
}
