# -*- coding:utf-8 -*-

import unittest
from blog.modules.page import Page


page = Page()


class TestCasePage(unittest.TestCase):
    def setUp(self):
        self.keyword = '关键字'

    def test_get_page_list(self):
        page.get_page_list()
        page.get_page_list(mode='simple')


if __name__ == '__main':
    unittest.main()
