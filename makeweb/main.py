from __future__ import with_statement
from contextlib import closing

from flask import Flask, render_template, url_for, request

from math import ceil
from collections import OrderedDict

app = Flask(__name__)

total = []
comment = []
tem = []
count = [0]
list_num = 3.0
page_num = 4.0
page = []

@app.route('/', methods = ['GET'])
@app.route('/index')
def show_board():
	finals = [dict(index = i,title = row[0], writer = row[1], content = row[2]) for i ,row in enumerate(total)] #total[::-1]
	
	total_page = int(ceil(len(total)/list_num))
	block_page = float(ceil(len(total)/list_num))


	# if not total:
	# 	pass
	# else:
	# 	page.append(total_page)
	# 	try:
	# 		if page[-1] == page[-2]:
	# 			del page[-1]
	# 	except:
	# 		pass

	# for i in range(len(total)):
	# 	if i % 3 ==0:
	# 		if i == 0 or i == 1:
	# 			pass
	# 		else:
	# 			count.append(count[-1]+1)

	# 	total[i].append(page[count[-1]])
	# 	print total

	# except:
	# 	pass

	total_block = int(ceil(block_page/page_num))

	# print "count", count
	# print "length",len(total)
	# print "page",page
	# print 'page',page[::3]
	# print 'total',total
	# print 'total_page',total_page
	# print 'block_page',total_block

	return render_template('index.html', finals = finals, t = page)

@app.route('/list')
def list_link():
	finals = [dict(index = i,title = row[0], writer = row[1], content = row[2]) for i ,row in enumerate(total)] #total[::-1]
	
	total_page = int(ceil(len(total)/list_num))
	block_page = float(ceil(len(total)/list_num))


	# try:
	# 	if page[-1] == page[-2]:
	# 		pass
	# 	else:

	if not total:
		pass
	else:
		page.append(total_page)
		try:
			if page[-1] == page[-2]:
				del page[-1]
		except:
			pass

	# except:
	# 	pass

	total_block = int(ceil(block_page/page_num))
#	block = ceil(page/page_num)
	
	return render_template('list.html', finals = finals, page = page)

@app.route('/insert')
def insert_form():
	return render_template('insert.html')

@app.route('/add', methods=['GET','POST'])
def add():
	if request.method == 'POST':
		one_by_one = []
		title = request.form['insert_title']
		writer = request.form['insert_writer']
		content = request.form['insert_content']
		one_by_one.append(title)
		one_by_one.append(writer)
		one_by_one.append(content)
		total.append(one_by_one)
		#print total
		comment.append([])
	return render_template('add.html')

@app.route('/view')
def board_info():
	idx = request.args['id']
	num = int(idx)
	tem.append(num)
	finals = [dict(index = i,title = row[0], writer = row[1], content = row[2]) for i ,row in enumerate(total)]
	fynal = [dict(writer = row[0], content = row[1]) for row in comment[num]]
	#anws = [dict(title = ) for row in comment]
	#print fynal
	return render_template('view.html', total = finals[num], com = fynal)

@app.route('/delete')
def delete_board():
	del total[tem[-1]]
	del tem[:]
	return render_template('return.html')

@app.route('/update')
def update_board():
	return render_template('update.html')

@app.route('/update_action', methods=['GET','POST'])
def action():
	if request.method == 'POST':
		title = request.form['insert_title']
		content = request.form['insert_content']
		total[tem[-1]][0] = title
		total[tem[-1]][2] = content
	return render_template('return.html')

@app.route('/comment')
def comment_F():
	return render_template('comment.html')

@app.route('/comment_action', methods=['GET', 'POST'])
def comment_action():
	if request.method == 'POST':
		one_by_one = []
		c_writer = request.form['insert_writer']
		c_content = request.form['insert_content']
		one_by_one.append(c_writer)
		one_by_one.append(c_content)
		comment[tem[-1]].append(one_by_one)
	url = dict(index = tem[-1])
	return render_template('/action.html', index = url)

if __name__ == '__main__':
	app.run(debug = True)



