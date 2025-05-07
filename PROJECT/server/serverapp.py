# реализация сервера — REST API на Flask, подключённый к PostgreSQL через SQLAlchemy.
# этот файл должен лежать на стороне сервера
from flask import Flask
from server.routes import api_bp
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
from config import Config
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# импорт моделей для создания таблиц
from server import models

# инициализация API
app.register_blueprint(api_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # создать таблицы, если не существуют
    app.run(debug=True)
