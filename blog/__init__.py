from flask import Flask
from . import config

app = Flask(__name__)
app.config.from_object(config.DebugConfig)


# 加载配置
import blog.settings

# 注册url
import blog.views.views
import blog.views.api.page
