from flask import render_template

from blog.toolkit.route.route import http

urls = '/'


@http('/')
def index():
    return render_template('index.html')


@http('/test1', methods=['POST'])
def test1():
    return 'hello world1'


@http()
def test2():
    return {'data': []}
