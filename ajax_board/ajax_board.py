from flask import Flask, render_template, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

ajax = []

# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/', methods = ['GET','POST'])
def index():
	# if request.method == 'POST':
	# 	obo = []
	# 	name = request.form['name']
	# 	writer = request.form['writer']
	# 	content = request.form['content']
	# 	obo.append[]
    return render_template('index.html')

# Route that will process the AJAX request, sum up two
# integer numbers (defaulted to zero) and return the
# result as a proper JSON response (Content-Type, etc.)
@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("80"),
        debug=True
    )



