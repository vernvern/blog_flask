# -*- coding: UTF-8 -*-

from flask import Flask
from flask_graphql import GraphQLView

from blog import config

app = Flask(__name__)

# 加载配置
if app.config['DEBUG']:
    app.config.from_object(config.DebugConfig)
else:
    app.config.from_object(config.ProductConfig)

import blog.settings


# 注册url
import blog.api.base
import blog.api.page
import blog.api.sort

from blog.modules.schema import schema
# graphene web test
if app.config['DEBUG'] is True:
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
    )
# graphene api
app.add_url_rule(
    '/api/graphql/batch',
    view_func=GraphQLView.as_view('graphql-batch', schema=schema, batch=True)
)


# 读数据
from blog.modules.page import PageHelper
PageHelper.load_pages_data()
