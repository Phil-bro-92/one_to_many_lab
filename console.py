import pdb

from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("Harper", "Lee")
author_repository.save(author_1)
author_2 = Author("Steven", "King")
author_repository.save(author_2)


author_repository.select_all

book_1 = Book("To Kill a Mockingbird", "Southern Gothic", 320, author_1, True)
book_repository.save(book_1)
book_2 = Book("It", "Horror", 290, author_2)
book_repository.save(book_2)
book_3 = Book("Misery", "Horror", 430, author_2)
book_repository.save(book_3)


pdb.set_trace()
