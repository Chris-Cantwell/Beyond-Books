import csv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

def main():
    #engine = create_engine(os.getenv("DATABASE URI"))
    engine = create_engine("postgres://stiokmkmdgvyic:e8274ce1c7b53022d220733bb48bab121b4afecfaacde94697f7f360a35e6957@ec2-54-225-237-84.compute-1.amazonaws.com:5432/dfbcvns96ond71")
    db = scoped_session(sessionmaker(bind=engine))

    f = open("books.csv")
    reader = csv.reader(f)

    authorList = set()
    bookList = []

    for isbn, title, author, year in reader:
        authorList.add(author)

        book = {
            "isbn": isbn,
            "title": title,
            "author": author,
            "year": year
            }
        bookList.append(book)

    for author in authorList:
        db.execute('INSERT INTO authors (name) VALUES (:name)', {"name": author})

    db.commit()
    print("Authors added to database")

    for book in bookList:
        author_id = db.execute('SELECT id FROM authors WHERE name=:author', {"author": book['author']}).fetchone()

        db.execute('INSERT INTO books (author_id, isbn, title, year) VALUES'
                   ' (:author_id, :isbn, :title, :year)', {"author_id": author_id.id,
                   "isbn": book['isbn'], "title": book['title'], "year": book['year']})

    db.commit()
    print("Books added to database")

if __name__ == "__main__":
	main()
