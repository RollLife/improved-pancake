from flask import request

with app.test_request_context('/hello', method='POST'):
	assert request.path == 'hello'
	assert request.method == 'POST'