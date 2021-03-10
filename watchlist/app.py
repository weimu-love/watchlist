# -*- coding: utf-8 -*-
"""
   File Name：     app
   Description :
   date：          2021/3/10
"""
from flask import Flask, render_template
from flask import escape, url_for

app = Flask(__name__)

name = 'Wei Mu'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', name=name, movies=movies)


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
