# -*- coding: utf-8 -*-
"""
   File Name：     app
   Description :
   date：          2021/3/10
"""

from flask import Flask, escape, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello():
    return 'welcome to my watchlist'


@app.route('/img')
def get_img():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % escape(name)


@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('get_img'))
    print(url_for('user_page', name='weimu'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'test page'
