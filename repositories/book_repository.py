from db.run_sql import run_sql

from models.book import Book

import repositories.author_repository as author_repository


def save(book):
    sql = "INSERT INTO books (title, genre, pages, author_id, read) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [book.title, book.genre, book.pages, book.author.id, book.read]
    results = run_sql(sql, values)
    id = results[0]["id"]
    book.id = id

    return book


def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row["author_id"])
        book = Book(
            row["title"], row["genre"], row["pages"], author, row["read"], row["id"]
        )
        books.append(book)
    return books


def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = author_repository.select(result["author_id"])
        book = Book(
            result["title"],
            result["genre"],
            result["pages"],
            result["read"],
            author,
            result["id"],
        )
    return book


def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)


def update(book):
    sql = (
        "UPDATE books SET (title, genre, pages, read) = (%s, %s, %s, %s) WHERE id = %s"
    )
    values = [book.title, book.genre, book.pages, book.read, book.id]
    run_sql(sql, values)
