from flask import render_template

from blog.toolkit.route.route import http
from blog import app

urls = '/'


@http('/')
def index():
    return render_template('index.html')


@http('/test1', methods=['POST'])
def test1():
    return 'hello world1'


@app.errorhandler(500)
def raise_error(e):
    app.logger.exception(e)
    return '500', 500
