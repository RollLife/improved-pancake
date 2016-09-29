from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__title__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///boards.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class boards(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    writer = db.Column(db.String(50))
    content = db.Column(db.String(200)) 

    def __init__(self, title, writer, content):
        self.title = title
        self.writer = writer
        self.content = content

@app.route('/')
def show_all():
   return render_template('show_all.html', boards = boards.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['title'] or not request.form['writer'] or not request.form['content']:
        	flash('Please enter all the fields', 'error')
        else:
	        board = boards(request.form['title'], request.form['writer'], request.form['content'])
	        db.session.add(board)
	        db.session.commit()
	        flash('Record was successfully added')
	        return redirect(url_for('show_all'))
    return render_template('new.html')

@app.route('/view')
def view_board():





# @app.route('/')
# @app.route('/index')
# def show_board():
# 	finals = [dict(index = i,title = row[0], writer = row[1], content = row[2]) for i ,row in enumerate(total)]
# 	pagingNum =  len(total)
# 	# if pagingNum/3 ==0:
# 	# 	page.append("")
# 	# print page
# 	# print len(page)
# 	return render_template('index.html', finals = finals)

# @app.route('/insert')
# def insert_form():
# 	return render_template('insert.html')

# @app.route('/add', methods=['GET','POST'])
# def add():
# 	b_page_list = 10;
# 	pageNum = 1
# 	if request.method == 'POST':
# 		one_by_one = []
# 		title = request.form['insert_title']
# 		writer = request.form['insert_writer']
# 		content = request.form['insert_content']
# 		one_by_one.append(title)
# 		one_by_one.append(writer)
# 		one_by_one.append(content)
# 		total.append(one_by_one)
# 		#print total
# 		comment.append([])
# 	return render_template('add.html')

# @app.route('/view')
# def board_info():
# 	idx = request.args['id']
# 	num = int(idx)
# 	tem.append(num)
# 	finals = [dict(index = i,title = row[0], writer = row[1], content = row[2]) for i ,row in enumerate(total)]
# 	fynal = [dict(writer = row[0], content = row[1]) for row in comment[num]]
# 	#anws = [dict(title = ) for row in comment]
# 	#print fynal
# 	return render_template('view.html', total = finals[num], com = fynal)

# @app.route('/delete')
# def delete_board():
# 	del total[tem[-1]]
# 	del tem[:]
# 	return render_template('return.html')

# @app.route('/update')
# def update_board():
# 	return render_template('update.html')

# @app.route('/update_action', methods=['GET','POST'])
# def action():
# 	if request.method == 'POST':
# 		title = request.form['insert_title']
# 		content = request.form['insert_content']
# 		total[tem[-1]][0] = title
# 		total[tem[-1]][2] = content
# 	return render_template('return.html')

# @app.route('/comment')
# def comment_F():
# 	return render_template('comment.html')

# @app.route('/comment_action', methods=['GET', 'POST'])
# def comment_action():
# 	if request.method == 'POST':
# 		one_by_one = []
# 		c_writer = request.form['insert_writer']
# 		c_content = request.form['insert_content']
# 		one_by_one.append(c_writer)
# 		one_by_one.append(c_content)
# 		comment[tem[-1]].append(one_by_one)
# 	url = dict(index = tem[-1])
# 	return render_template('/action.html', index = url)







if __title__ == '__main__':
   db.create_all()
   app.run(debug = True)
