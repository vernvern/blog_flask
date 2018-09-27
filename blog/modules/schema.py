# -*- coding=utf-8 -*-

import graphene

from blog.models.page import PageQL
from blog.modules.page import PageQLHelper


class Query(graphene.ObjectType):

    page = graphene.Field(PageQL, id=graphene.ID())
    get_pages_by_sort = graphene.Field(
        graphene.List(lambda: PageQL),
        sort=graphene.String()
    )

    def resolve_page(self, info, id):
        page_helper = PageQLHelper()
        return page_helper.get_page(id)

    def resolve_get_pages_by_sort(self, info, sort):
        page_helper = PageQLHelper()
        return page_helper.get_pages_by_sort(sort)


schema = graphene.Schema(query=Query)
