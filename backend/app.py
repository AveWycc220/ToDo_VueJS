""" Module for Flask Application. """
from flask import Flask, jsonify, request, make_response, abort
from src.json_parser import JSONParser

app = Flask(__name__)
json_parser = JSONParser()
app.config['JSON_AS_ASCII'] = False
config = {
    'DEBUG': True,
    'PORT': 8080,
}


@app.route('/login/<name>', methods=['GET'])
def login(name):
    """ Method for getting json for todo"""
    response = make_response(jsonify(json_parser.get_json(name)))
    response.set_cookie('name', name, secure=True, httponly=True, samesite='Strict')
    return response


@app.route('/update/', methods=['POST'])
def update():
    """ Method for upload new information on server """
    new_json = request.json
    name = request.cookies.get('name')
    if not name:
        abort(401, description='Unauthorized')
    else:
        json_parser.update_json(name, new_json)
        return jsonify({'status': 200})


if __name__ == '__main__':
    app.run(port=config['PORT'], debug=config['DEBUG'])
