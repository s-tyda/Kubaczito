from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

Base = declarative_base()


class Borrower(Base):
    __tablename__ = 'borrowers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    is_borrowed = Column(Boolean)

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False


class Borrowing(Base):
    __tablename__ = 'borrowings'
    id = Column(Integer, primary_key=True)
    borrower_id = Column(Integer, ForeignKey("Borrowers.id"))
    book_id = Column(Integer, ForeignKey("Books.id"))
    is_returned = Column(Boolean)

    def __init__(self, borrower_id, book_id):
        self.borrower_id = borrower_id
        self.book_id = book_id
        self.is_returned = False


class Library(Base):
    def __init__(self, name):
        self.name = name
        self.engine = create_engine(f'sqlite:///{self.name}.db', echo=True)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def add_user(self, borrower):
        self.session.add(borrower)
        self.session.commit()

    def add_book(self, book):
        self.session.add(book)
        self.session.commit()

    def borrow_book(self, borrower_id, book_id):
        client = self.session.query(Borrower).filter(Borrower.id == borrower_id).first()
        if not client:
            print("There is no such borrower")
            return False
        book = self.session.query(Book).filter(Book.id == book_id).first()
        if not book:
            return "There is no such book"
        if book.is_borrowed:
            return "This book is already borrowed"
        book.is_borrowed = True
        borrowing = Borrowing(borrower_id, book_id)
        self.session.add(borrowing)
        self.session.commit()
        return True


if __name__ == "__main__":
    library = Library("Bibloteka")
    yeti = Borrower("Paweł", "Nowak")
    library.add_user(yeti)
    book = Book("Robinson Crusoe", "Daniel Defoe")
    library.add_book(book)
    if library.borrow_book(1, 1):
        print("Book was succesfully borrowed")
