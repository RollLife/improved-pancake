from flask import Flask, render_template, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

ajax = []

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
	return jsonify({'array':ajax})


if __name__ == '__main__':
    app.run(debug=True)



