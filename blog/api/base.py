# -*- coding=utf-8 -*-

from blog import app


@app.errorhandler(500)
def raise_error(e):
    app.logger.exception(e)
    return '500', 500
