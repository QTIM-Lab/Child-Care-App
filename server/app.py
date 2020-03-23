# Base
import uuid

# Flask
from flask import Flask, jsonify, request
from flask_cors import CORS

# DB
from tinydb import TinyDB, Query

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

db = TinyDB('./database.json')

# Main app route
@app.route('/requests', methods=['GET', 'POST'])
def all_requests():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        for i in post_data:
            print(post_data.get(i))
        db.insert({
            'id': uuid.uuid4().hex,
            'name': post_data.get('name'),
            'email': post_data.get('email'),
            'address': post_data.get('address'),
            'lat': post_data.get('lat'),
            'long': post_data.get('long'),
            'request': post_data.get('request'),
            'needHelp': post_data.get('needHelp'),
            'canHelp': post_data.get('canHelp')
        })
        response_object['message'] = 'Response added!'
    else:
        response_object['requests'] = db.all()
    return jsonify(response_object)

# Delete\Update api handler
@app.route('/requests/<request_id>', methods=['PUT', 'DELETE'])
def single_request(request_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_request(request_id)
        print("id: ")
        print("name: {}".format(post_data.get('name')))
        print("email: {}".format(post_data.get('email')))
        print("address: {}".format(post_data.get('address')))
        print("lat: {}".format(post_data.get('lat')))
        print("long: {}".format(post_data.get('long')))
        print("request: {}".format(post_data.get('request')))
        print("needHelp: {}".format(post_data.get('needHelp')))
        print("canHelp: {}".format(post_data.get('canHelp')))
        db.insert({
            'id': uuid.uuid4().hex,
            'name': post_data.get('name'),
            'email': post_data.get('email'),
            'address': post_data.get('address'),
            'lat': post_data.get('lat'),
            'long': post_data.get('long'),
            'request': post_data.get('request'),
            'needHelp': post_data.get('needHelp'),
            'canHelp': post_data.get('canHelp')
        })
        response_object['message'] = 'Response updated!'
    if request.method == 'DELETE':
        remove_request(request_id)
        response_object['message'] = 'Response removed!'
    return jsonify(response_object)

# Helper for the update api
def remove_request(request_id):
    for request in db:
        if request['id'] == request_id:
            db.remove(Query().id == request_id)
            return True
    return False

# Helper for clearing and reloading the db
def recreate_db():
    # Base
    import uuid

    # Flask
    from flask import Flask, jsonify, request
    from flask_cors import CORS

    # DB
    from tinydb import TinyDB, Query

    db = TinyDB('./database.json')
    db.purge()
    db.insert_multiple([
        {
            'id': uuid.uuid4().hex,
            'name': 'Jack Kerouac',
            'email': 'test@gmail.com',
            'address': 'Park Drive,Boston, MA',
            'lat': 42.341590,
            'long': -71.097740,
            'request': 'Lack of diapers in my area, can anyone help?',
            'needHelp': False,
            'canHelp': False,
        },
        {
            'id': uuid.uuid4().hex,
            'name': 'J. K. Rowling',
            'email': 'test@gmail.com',
            'address': '23 Aldie St., Allston, MA 02134',
            'lat': 42.358960,
            'long': -71.135920,
            'request': 'Can someone watch my kid from 2-3pm tomorrow?',
            'needHelp': False,
            'canHelp': False

        },
        {
            'id': uuid.uuid4().hex,
            'name': 'Ben B',
            'email': 'test@gmail.com',
            'address': '1000 Commonwealth Ave., Boston, MA 02135',
            'lat': 42.349420,
            'long': -71.132920,
            'request': 'I need a baby sitter this Friday (3/20/2020) from 1-2pm/ Is anyone available?',
            'needHelp': False,
            'canHelp': False
        }
    ])



# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')



if __name__ == '__main__':
    app.run(host='0.0.0.0')
