#!/usr/bin/env python3

from flask import Flask
from flask import jsonify
from flask import request
from methods.create_user import *
from methods.login import *
from methods.aylien_call import *

app = Flask(__name__)


@app.route('/news_analyser', methods=['GET'])
def news_analyser():
    data = request.form
    response = get_news_info(data['url'])
    print(response)
    return jsonify(response)

@app.route('/login', methods=['GET'])
def get_row_id():
    data = request.form
    response = login(data)
    return jsonify(response)

@app.route('/register', methods=['POST'])
def post_row():
    data = request.form
    response = create_user(data)
    return jsonify(response)

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)