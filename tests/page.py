# -*- coding:utf-8 -*-

import unittest
from blog.modules import page as modules_page


class TestCasePage(unittest.TestCase):
    def setUp(self):
        self.keyword = '关键字'

        # test_split_meta
        self.body = '''---
title: 这是一个模板
date: 2017/08/10 21:30:21
categories: test
updated: 2017/08/10 21:30:12
comments: true
toc: true

tags:
- test

---

## 前言:





## !@#$%^&*



## 参考文献

*参考文献：*

- \[\]\(\)

[T_T]:
    测试
            '''

    def test_get_page_list(self):
        ret = modules_page.get_page_list(self.keyword)
        # for data in ret['data']:
        #     self.assertTrue(self.keyword in data['title'])

    # def test_get_page_detail(self):
    #     ret = modules_page.get_page_detail(123123123)
    #     self.assertTrue(isinstance(ret['data'], dict))


if __name__ == '__main':
    unittest.main()
