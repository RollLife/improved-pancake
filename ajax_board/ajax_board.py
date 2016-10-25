from flask import Flask, render_template, request, jsonify, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

ajax = []
comment_Array = []

# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/', methods = ['GET','POST'])
def index():
	print ajax
	return render_template('index.html')

@app.route('/insert')
def insert_form():
	return render_template('insert.html')

@app.route('/add', methods=['POST'])
def ajax_add():
	comment_Array.append([])

	one_by_one = []

	title = request.form['title']
	writer = request.form['writer']
	content = request.form['content']

	one_by_one.append(title)
	one_by_one.append(writer)
	one_by_one.append(content)
	ajax.append(one_by_one)
	if title and writer and content:
		return jsonify({'title' : title,'writer':writer,'content':content})

	return jsonify({'error' : 'Missing data!'})


@app.route('/get_list', methods=['GET'])
def ajax_show():
	print ajax
	if ajax is None:
		title = ""
		writer = ""
		content = ""
	else:
		title = ajax[0][0]
		writer = ajax[0][1]
		content = ajax[0][2]
	return jsonify({'title' : title,'writer':writer,'content':content,'array':ajax})

@app.route('/example')
def example():
	return render_template('example.html')

# Route that will process the AJAX request, sum up two
# integer numbers (defaulted to zero) and return the
# result as a proper JSON response (Content-Type, etc.)

@app.route('/view', methods=['GET'])
def show_detail():
	return render_template('view.html')


@app.route('/view_list')
def detail_option():
	return jsonify({'array':ajax,'comment_Array':comment_Array})

@app.route('/delete')
def delete_detail():
	num = int(request.args['id'])
	del ajax[num]
	print num
	return jsonify({})

@app.route('/update')
def update_insert():
	return render_template('update.html')

@app.route('/action', methods=['GET'])
def update_detail():
	print "ss"
	print ajax
	num = int(str(request.args['id']))
	print type(num)
	title = request.args['title']
	content = request.args['content']

	ajax[num][0] = title
	ajax[num][2] = content
	return jsonify({})


@app.route('/comment', methods=['GET'])
def comment_insert():
	print "test text"
	num = int(str(request.args['id']))
	title = request.args['title']
	content = request.args['content']
	one_by_one = []
	one_by_one.append(title)
	one_by_one.append(content)
	comment_Array[num].append(one_by_one)


	# if request.method == 'POST':
	# 	title = request.form['comment_title']
	# 	content = request.form['comment_content']
	# comment_Array.append(title)
	# comment_Array.append(content)

	print comment_Array
	return jsonify({'click_comment':comment_Array})

if __name__ == '__main__':
    app.run(debug=True)



