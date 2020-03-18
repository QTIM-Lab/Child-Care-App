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

# Database (Mock)
# BOOKS = [
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'On the Road',
#         'author': 'Jack Kerouac',
#         'read': True
#     },
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'Harry Potter and the Philosopher\'s Stone',
#         'author': 'J. K. Rowling',
#         'read': False
#     },
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'Green Eggs and Ham',
#         'author': 'Dr. Seuss',
#         'read': True
#     }
# ]

db = TinyDB('./database.json')
# db.insert_multiple([
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'On the Road',
#         'author': 'Jack Kerouac',
#         'read': True
#     },
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'Harry Potter and the Philosopher\'s Stone',
#         'author': 'J. K. Rowling',
#         'read': False
#     },
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'Green Eggs and Ham',
#         'author': 'Dr. Seuss',
#         'read': True
#     }
# ])

# Main app route
@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        # BOOKS.append({
        #     'id': uuid.uuid4().hex,
        #     'title': post_data.get('title'),
        #     'author': post_data.get('author'),
        #     'read': post_data.get('read')
        # })
        db.insert({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        # response_object['books'] = BOOKS
        response_object['books'] = db.all()
    return jsonify(response_object)

# Delete\Update api handler
@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        # BOOKS.append({
        #     'id': uuid.uuid4().hex,
        #     'title': post_data.get('title'),
        #     'author': post_data.get('author'),
        #     'read': post_data.get('read')
        # })
        db.insert({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)

# Helper for the update api
def remove_book(book_id):
    # for book in BOOKS:
    #     if book['id'] == book_id:
    #         BOOKS.remove(book)
    #         return True
    for book in db:
        if book['id'] == book_id:
            db.remove(Query().id == book_id)
            return True
    return False

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()
