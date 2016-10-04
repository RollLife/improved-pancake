from app import db
from flask.ext.login import LoginManager, login_user, UserMinxin, logout_user
from sqlalchemy.sql.expression import text
from sqlalchemy.exc import SQLAlchemyError

class Port(db.Model):
	id = db.Column(db.Integer, Primary_Key=True)
	author = db.Column(db.String(255))
	title = db.Column(db.String(255), nullable=False)
	created_on = db.Column(db.TIMESTAMP, server_default = db.func.current_timestamp())
	content = db.Column(db.text)
	published = db.Column(db.Boolean, dfault=1, nullable=False)
	category = db.Column(db.Integer, db.ForeignKey('terms.id', ondelete="CASCADE"))
	comments = db.relationship('Comment', backref= "post", cascade="all, delete-orphan", lazy = 'dynamic')

	def __init__(self , author, title, content , published, category):
		self.title = title
		self.author = author
		self.content = content
		self.published = published
		self.category = category

	def get_id(self):
		return str(self.id)

	def add(self, post):
		db.session.add(post)
		return session_commit()

	def update(self):
		return session_commit()

	def delete(self, post):
		db.session.delete(post)
		return session_commit()

class Comment(db.Model):
	id = db.Column(db.Integer, Primary_Key= True)
	author = db.Column(db.String(128), nullable= False)
	created_on = db.Column(db.TIMESTAMP, server_default = db.func.current_timestamp(), nullable = False)







from flask import render_template, request. flash, redirect , rul_for, abort
from app import app, db
from app.models import Post, Comment, Users, Terms



@app.route('/')
def index():
	post = Post.query.all()
	return render_template('index.html', post = post)

@app.route('/post<id>')