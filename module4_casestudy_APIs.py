"""
A simple Flask-based CRUD API to manage books in memory. Utilizes an in-memory list.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# makeshift "database" of books from our notebook assignment (just a list of dictionaries).
books = [
    {
        "id": 1,
        "book_name": "The Weirdstone of Brisingamen",
        "author": "Alan Garner",
        "publisher": "Collins (1960)"
    },
    {
        "id": 2,
        "book_name": "Perdido Street Station",
        "author": "China Miéville",
        "publisher": "Macmillan (2000)"
    },
    {
        "id": 3,
        "book_name": "Thud!",
        "author": "Terry Pratchett",
        "publisher": "Doubleday (2005)"
    },
    {
        "id": 4,
        "book_name": "The Spellman Files",
        "author": "Lisa Lutz",
        "publisher": "Simon & Schuster (2007)"
    },
    {
        "id": 5,
        "book_name": "Small Gods",
        "author": "Terry Pratchett",
        "publisher": "Victor Gollancz (1992)"
    }
]

@app.route('/books', methods=['GET'])
def get_books():
    """
    Fetch all books from our in-memory list and return them as JSON.
    """
    return jsonify(books), 200

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    """
    Retrieve a single book by its numeric ID.
    """
    book = next((item for item in books if item["id"] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    
    return jsonify(book), 200

@app.route('/books', methods=['POST'])
def add_book():
    """
    Add a new book to the list. Expects 'id', 'book_name', 'author', and 'publisher'.
    """
    data = request.get_json()
    
    # Make sure all fields are present
    if not data or not all(k in data for k in ("id", "book_name", "author", "publisher")):
        return jsonify({"error": "Please provide 'id', 'book_name', 'author', and 'publisher'."}), 400

    # Check duplicate ID
    if any(book["id"] == data["id"] for book in books):
        return jsonify({"error": "A book with this ID already exists."}), 400
    
    new_book = {
        "id": data["id"],
        "book_name": data["book_name"],
        "author": data["author"],
        "publisher": data["publisher"]
    }
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    """
    Update the fields of an existing book by its ID.
    """
    data = request.get_json()
    book = next((item for item in books if item["id"] == book_id), None)
    
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    
    # Update the fields provided in the request
    book["book_name"] = data.get("book_name", book["book_name"])
    book["author"] = data.get("author", book["author"])
    book["publisher"] = data.get("publisher", book["publisher"])
    
    return jsonify(book), 200

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """
    Remove a book from the list by its ID.
    """
    global books
    book = next((item for item in books if item["id"] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    
    books = [item for item in books if item["id"] != book_id]
    return jsonify({"message": "Book deleted"}), 200

if __name__ == '__main__':
    # Running in debug mode
    app.run(debug=True)
