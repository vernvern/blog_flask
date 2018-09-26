# -*- coding=utf-8 -*-

import copy
import graphene

from blog.modules.schema import SchemaHelper


class PageQL(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String(default_value='未分类')
    body = graphene.String()
    date_created = graphene.String()
    date_modified = graphene.String()
    tags = graphene.List(graphene.String)
    sort = graphene.String(default_value='未分类')
    removed = graphene.Boolean()


class Query(graphene.ObjectType):

    page = graphene.Field(PageQL, id=graphene.ID())

    def resolve_page(self, info, **kw):
        variables = copy.deepcopy(info.variable_values)
        variables.update(kw)
        schema_helper = SchemaHelper()
        return schema_helper.get_page(variables['id'])


schema = graphene.Schema(query=Query)
