import requests

class Model:
    API_URL = 'http://127.0.0.1:5000/books'

    def get_books(self):
        response = requests.get(self.API_URL)
        return response.json()

    def add_book(self, title, author, year):
        data = {
            'title': title,
            'author': author,
            'year': int(year) if year else None
        }
        response = requests.post(self.API_URL, json=data)
        return response.status_code == 201

    def delete_book(self, book_id):
        response = requests.delete(f'{self.API_URL}/{book_id}')
        return response.status_code == 200
