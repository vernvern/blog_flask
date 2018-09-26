# -*- coding=utf-8 -*-

import unittest
from snapshottest import TestCase
from graphene.test import Client

from blog.modules.schema import SchemaHelper
from blog.models.schema import schema


class TestCaseSchema(TestCase):

    client = Client(schema)

    def setup(self):
        self.schema_helper = SchemaHelper()

    def test_blog_title(self):
        query = '''
            query PageTitle {
                page (id: "1a2467e3-bc16-4e75-a432-4ad35796975f"){
                    id,
                    title,
                }
            }
        '''
        self.assertMatchSnapshot(self.client.execute(query))

        query = """
            query Page($id: ID) {
                page(id: $id) {
                    id
              }
            }
        """
        kw = {'id': "1a2467e3-bc16-4e75-a432-4ad35796975f"}
        self.assertMatchSnapshot(self.client.execute(query, variables=kw))


if __name__ == '__main__':
    unittest.main()
