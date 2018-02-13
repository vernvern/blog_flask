import time

from flask import Flask


app = Flask(__name__)

# 加载配置
import blog.settings

# 数据库对象
from blog.settings import db

# 加载数据表
from blog.models.page import *

# 注册url
import blog.views.views
import blog.views.api.page
