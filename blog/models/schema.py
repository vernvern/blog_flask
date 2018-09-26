# -*- coding=utf-8 -*-

import graphene

from blog.models.page import PageQL
from blog.modules.schema import SchemaHelper


schema_helper = SchemaHelper()


class Query(graphene.ObjectType):

    page = graphene.Field(PageQL, id=graphene.ID())

    def resolve_page(self, info, id):
        return schema_helper.get_page(id)


schema = graphene.Schema(query=Query)
