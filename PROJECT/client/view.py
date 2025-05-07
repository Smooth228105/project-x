import tkinter as tk
from tkinter import messagebox, ttk

class View(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("📚 Библиотека")
        self.geometry("500x400")

        self.title_entry = tk.Entry(self)
        self.title_entry.pack()
        self.title_entry.insert(0, "Название книги")

        self.author_entry = tk.Entry(self)
        self.author_entry.pack()
        self.author_entry.insert(0, "Автор")

        self.year_entry = tk.Entry(self)
        self.year_entry.pack()
        self.year_entry.insert(0, "Год издания")

        self.add_btn = tk.Button(self, text="Добавить книгу", command=self.controller.add_book)
        self.add_btn.pack(pady=5)

        self.tree = ttk.Treeview(self, columns=("ID", "Название", "Автор", "Год"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Название", text="Название")
        self.tree.heading("Автор", text="Автор")
        self.tree.heading("Год", text="Год")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.delete_btn = tk.Button(self, text="Удалить выбранную книгу", command=self.controller.delete_book)
        self.delete_btn.pack(pady=5)

    def get_input(self):
        return (
            self.title_entry.get(),
            self.author_entry.get(),
            self.year_entry.get()
        )

    def insert_books(self, books):
        self.tree.delete(*self.tree.get_children())
        for book in books:
            self.tree.insert("", "end", values=(book['id'], book['title'], book['author'], book['year']))

    def get_selected_book_id(self):
        selected = self.tree.selection()
        if selected:
            return int(self.tree.item(selected[0])['values'][0])
        return None

    def show_message(self, text):
        messagebox.showinfo("Сообщение", text)

    def show_error(self, text):
        messagebox.showerror("Ошибка", text)
