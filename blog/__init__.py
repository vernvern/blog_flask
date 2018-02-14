import time

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import config

app = Flask(__name__)
app.config.from_object(config.DebugConfig)

# sqlalchemy
db = SQLAlchemy(app)

# 加载配置
import blog.settings

# 加载数据表
from blog.models.page import *

# 注册url
import blog.views.views
import blog.views.api.page
