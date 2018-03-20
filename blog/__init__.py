from flask import Flask
from blog import config


app = Flask(__name__)

# 加载配置
app.config.from_object(config.DebugConfig)
import blog.settings

# 注册url
import blog.views.views
import blog.views.api.page
