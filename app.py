from flask import Flask, jsonify, request
import controller
from db import create_tables

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"


@app.route('/books', methods=["GET"])
def get_books():
    books = controller.get_books()
    return jsonify(books)


@app.route("/create/book", methods=["POST"])
def insert_book():
    book_details = request.get_json()
    name = book_details["name"]
    price = book_details["price"]
    rate = book_details["rate"]
    result = controller.insert_book(name, price, rate)
    return jsonify(result)


@app.route("/update/book", methods=["PUT"])
def update_book():
    book_details = request.get_json()
    id = book_details["id"]
    name = book_details["name"]
    price = book_details["price"]
    rate = book_details["rate"]
    result = controller.update_book(id, name, price, rate)
    return jsonify(result)


@app.route("/delete/book/<id>", methods=["DELETE"])
def delete_book(id):
    result = controller.delete_book(id)
    return jsonify(result)

@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response

if __name__ == "__main__":
    create_tables()
    app.run(host="0.0.0.0", port=5000, debug=True)