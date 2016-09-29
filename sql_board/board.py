from __future__ import with_statement
from contextlib import closing

import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

#db setting
DATABASE = '/tmp/sqlite.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.from_envvar('FALSKER_SETTINGS', silent=True)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

# create data base command
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route('/')
def show_entries():
    cur = g.db.execute('select title, writer, content from info order by id desc')
    entries = [dict(title=row[0], writer=row[1], content=row[2]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    g.db.execute('insert into info (title, writer, content) values (?, ?, ?)',
                 [request.form['title'], request.form['text'], request.form['content']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
	app.run(debug = True)



