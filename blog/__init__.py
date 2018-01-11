from flask import Flask, Response, jsonify
from flask_sqlalchemy import SQLAlchemy


class MyResponse(Response):
    @classmethod
    def force_type(cls, response, environ=True):
        if isinstance(response, dict):
            if not response.get('code', False):
                response['code'] = '0'

            if not response.get('data', False):
                response['data'] = []

            if not response.get('index', False):
                response['index'] = 1

            if not response.get('size', False):
                response['size'] = len(response['data'])

            if not response.get('total', False):
                response['total'] = len(response['data'])

            response = jsonify(response)
        return super(Response, cls).force_type(response, environ)


app = Flask(__name__)
app.response_class = MyResponse
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 加载数据表
from blog.models.page import *

# 注册url
import blog.views.views
import blog.views.api.page
