from flask import Flask

app = Flask(__name__)


import blog.views.views
import blog.views.api.test_api

