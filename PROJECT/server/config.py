import os

class Config:
    # URI для подключения к PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'postgresql://postgres:postgres@localhost:5432/library_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

