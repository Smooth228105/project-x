# реализация сервера — REST API на Flask, подключённый к PostgreSQL через SQLAlchemy.
# этот файл должен ледать на строне сервера >
from flask import Blueprint, request, jsonify
from server.models import Book
from server.app import db

api_bp = Blueprint('api', __name__)

@api_bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{
        'id': b.id,
        'title': b.title,
        'author': b.author,
        'year': b.year
    } for b in books])

@api_bp.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(
        title=data['title'],
        author=data['author'],
        year=data.get('year')
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added'}), 201

@api_bp.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'error': 'Not found'}), 404
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted'})
