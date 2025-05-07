# Открой pgAdmin и выполни этот SQL

CREATE DATABASE library;

\c library;

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    year INTEGER,
    created_at TIMESTAMP DEFAULT NOW()
);

