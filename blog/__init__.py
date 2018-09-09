# -*- coding: UTF-8 -*-

from flask import Flask
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

# 读数据
from blog.modules.page import Page
Page.load_pages_data()
