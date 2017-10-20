# -*- coding: utf-8 -*-

"""
Created by yangshuanglong@wecash.net on 17/10/20
"""

from flask import Flask

app = Flask(__name__)
app.secret_key = 'sfdsfjhkls'


@app.route('/')
def index():
    return 'hello'


@app.errorhandler(404)
def page_not_found(code):
    return 'page not found'


if __name__ == '__main__':
    debug = False
    app.run(host='127.0.0.1', port=5000, debug=debug)
