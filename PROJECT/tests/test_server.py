import unittest
from server.app import app, db
from server.models import Book

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        with app.app_context():
            db.create_all()

    def test_add_and_get_book(self):
        response = self.app.post('/books', json={
            'title': '1984',
            'author': 'George Orwell',
            'year': 1949
        })
        self.assertEqual(response.status_code, 201)

        response = self.app.get('/books')
        data = response.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], '1984')

    def test_delete_book(self):
        self.app.post('/books', json={'title': 'Book', 'author': 'A', 'year': 2000})
        response = self.app.delete('/books/1')
        self.assertEqual(response.status_code, 200)

        response = self.app.get('/books')
        self.assertEqual(len(response.get_json()), 0)

if __name__ == '__main__':
    unittest.main()
