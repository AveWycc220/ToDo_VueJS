""" Module for Flask Application. """
from flask import Flask, jsonify, request, make_response, abort
from src.json_parser import JSONParser
import os
from dotenv import load_dotenv, find_dotenv

app = Flask(__name__)
json_parser = JSONParser()
app.config['JSON_AS_ASCII'] = False
config = {
    'DEBUG': True,
    'PORT': 8080,
}
load_dotenv(find_dotenv())


@app.route('/login/<name>', methods=['GET'])
def login(name):
    """ Method for getting json for todo"""
    check_authorization()
    response = make_response(jsonify(json_parser.get_json(name)))
    response.set_cookie('name', name, max_age=604800, secure=False, httponly=True, samesite='Strict')
    response.set_cookie('auth', '1', max_age=604800)
    return response


@app.route('/update/', methods=['POST'])
def update():
    """ Method for upload new information on server """
    check_authorization()
    new_json = request.json
    name = request.cookies.get('name')
    auth = request.cookies.get('auth')
    if name and auth == '1':
        json_parser.update_json(name, new_json)
        return jsonify({'status': 200})
    else:
        return abort(401, description='Cookie is empty. You mast login.')


def check_authorization():
    if 'Authorization' in request.headers.keys():
        if request.headers['Authorization'] != 'Bearer ' + os.environ.get('TOKEN'):
            return abort(401, description='Wrong token')
    else:
        return abort(400, description='Authorization is empty')


if __name__ == '__main__':
    app.run(port=config['PORT'], debug=config['DEBUG'])
