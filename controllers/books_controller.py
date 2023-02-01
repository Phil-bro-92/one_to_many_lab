from flask import Flask, render_template, redirect, request
from repositories import author_repository
from repositories import book_repository
from models.book import Book
from flask import Blueprint

books_blueprint = Blueprint("books", __name__)


@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", books=books)


# NEW
# GET '/books/new'
@books_blueprint.route("/books/new")
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", authors=authors)


# CREATE
# POST '/books'
@books_blueprint.route('/books', methods=['POST'])
def create_book():
    title = request.form['title']
    genre = request.form['genre']
    pages = request.form['pages']
    author_id = request.form['author_id']
    read = request.form['read']
    author = author_repository.select(author_id)
    new_book = Book(title, genre, pages, author, read)
    book_repository.save(new_book)
    return redirect('/books')

# SHOW
# GET 'books/<id>'
@books_blueprint.route("/books/<id>")
def show_book(id):
    book = book_repository.select(id)
    return render_template("books/show.html", book=book)


# EDIT
# GET '/books/<id>/edit'
@books_blueprint.route("/books/<id>/edit")
def edit_book(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template("books/edit.html", book=book, authors=authors)


# UPDATE
# PUT 'books/<id>'
@books_blueprint.route("/books/<id>", methods=["POST"])
def update_book(id):
    title = request.form["title"]
    genre = request.form["genre"]
    pages = request.form["pages"]
    author_id = request.form["author_id"]
    read = request.form["read"]
    author = author_repository.select(author_id)
    book = Book(title, genre, pages, author, read, id)
    book_repository.update(book)
    return redirect("/books")


# DELETE
# DELETE 'books/<id>'
@books_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")
