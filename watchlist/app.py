# -*- coding: utf-8 -*-
"""
   File Name：     app
   Description :
   date：          2021/3/10
"""
from flask import Flask, render_template
from flask import escape, url_for
from flask_sqlalchemy import SQLAlchemy
import os, sys
import click

app = Flask(__name__)

# SQLALCHEMY_DATABASE_URI变量值，不同的 DBMS 有不同的格式，对于 SQLite是“sqlite:///数据库文件的绝对地址”
# windows下为3根斜线
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')

# 关闭对模型修改的监控
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 在扩展类实例化前加载配置
db = SQLAlchemy(app)


# User表对应的类
class User(db.Model):
    # 主键ID
    id = db.Column(db.Integer, primary_key=True)
    # 用户名
    name = db.Column(db.String(20))


# Movie表对应的类
class Movie(db.Model):
    # 主键ID
    id = db.Column(db.Integer, primary_key=True)
    # 电影标题
    title = db.Column(db.String(60))
    # 电影年份
    year = db.Column(db.String(4))


"""Generate fake data."""


# 命令行输入 flask forge即可运行
@app.cli.command()
def forge():
    db.create_all()

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

    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)

    db.session.commit()
    click.echo('Done.')


@app.route('/')
@app.route('/home')
def index():
    # 读取用户记录
    # user = User.query.first()
    # 读取所有电影记录
    movies = Movie.query.all()
    # print(user.name)
    return render_template('index.html', movies=movies)


@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    # user = User.query.first()
    # 通的视图函数之所以不用写出状态码，是因为默认会使用 200 状态码，表示成功。
    return render_template('404.html'), 404


# 模板上下文处理函数
# 这个函数返回的变量（以字典键值对的形式）将会统一注入到每一个模板的上下文环境中，因此可以直接在模板中使用。
@app.context_processor
def inject_user():
    user = User.query.first()
    return dict(user=user)


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
