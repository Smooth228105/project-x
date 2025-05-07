from client.model import Model
from client.view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def run(self):
        self.refresh_books()
        self.view.mainloop()

    def refresh_books(self):
        books = self.model.get_books()
        self.view.insert_books(books)

    def add_book(self):
        title, author, year = self.view.get_input()
        if not title or not author:
            self.view.show_error("Название и автор обязательны")
            return
        success = self.model.add_book(title, author, year)
        if success:
            self.view.show_message("Книга добавлена")
            self.refresh_books()
        else:
            self.view.show_error("Ошибка добавления")

    def delete_book(self):
        book_id = self.view.get_selected_book_id()
        if not book_id:
            self.view.show_error("Выберите книгу для удаления")
            return
        success = self.model.delete_book(book_id)
        if success:
            self.view.show_message("Книга удалена")
            self.refresh_books()
        else:
            self.view.show_error("Ошибка удаления")
