from flask import Flask
from blog import config


app = Flask(__name__)

# 加载配置
app.config.from_object(config.ProductConfig)
import blog.settings

# 注册url
import blog.api.base
import blog.api.page
