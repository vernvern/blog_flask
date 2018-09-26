# -*- coding=utf-8 -*-

import graphene

from blog.models.page import PageQL
from blog.modules.page import PageQLHelper


class Query(graphene.ObjectType):

    page = graphene.Field(PageQL, id=graphene.ID())
    page_with_sort = graphene.Field(PageQL, sort=graphene.String())

    def resolve_page(self, info, id):
        page_helper = PageQLHelper()
        return page_helper.get_page(id)


schema = graphene.Schema(query=Query)
