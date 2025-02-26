import base64
import json
import time

import redis
from flask import Flask, Response, request

app = Flask(__name__)

conn = redis.Redis('redis', port=6379)

@app.route('/')
def hello_world():
	return 'Hey, we have Flask in a Docker container!'


@app.route('/shorten/<url>', methods=['POST'])
def gen_code(url):
	# Generate short URL
	current_time = time.strftime("%H%M%S", time.localtime(time.time()))
	concatenated_str=url+current_time
	encoded_str = base64.b64encode(bytes(concatenated_str, encoding='utf8'))
	sub_encoded_str=encoded_str[:6]
	conn.set(url, sub_encoded_str)
	return sub_encoded_str


@app.route('/expand/<url>', methods=['GET'])
def validate(url):
	# Get long URL
	keys = conn.keys()
	for key in keys:
		if conn.get(key.decode("utf-8")).decode("utf-8") == url:
			return key
	return "Invalid URL"


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8000, debug=True, threaded=True)
