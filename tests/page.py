# -*- coding:utf-8 -*-

import unittest
from blog.modules import page as modules_page


class TestCasePage(unittest.TestCase):
    def setUp(self):
        self.keyword = '关键字'

    def test_get_page_list(self):
        ret = modules_page.get_page_list(self.keyword)
        for data in ret['data']:
            self.assertTrue(self.keyword in data['title'])

    def test_get_page_detail(self):
        ret = modules_page.get_page_detail(123123123)
        self.assertTrue(isinstance(ret['data'], dict))


if __name__ == '__main':
    unittest.main()
