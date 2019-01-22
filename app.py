from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

def main():
    #engine = create_engine(os.getenv("DATABASE URI"))
    engine = create_engine("postgres://stiokmkmdgvyic:e8274ce1c7b53022d220733bb48bab121b4afecfaacde94697f7f360a35e6957@ec2-54-225-237-84.compute-1.amazonaws.com:5432/dfbcvns96ond71")
    db = scoped_session(sessionmaker(bind=engine))

    f = open("books.csv")
	reader = csv.reader(f)

    for author in reader:
        db.execute('INSERT INTO authors (name) VALUES (:name) {"name": author}')
    db.commit()

    for isbn, title, author, year in reader:
        author_id = db.execute('SELECT id FROM authors WHERE name=:author){"author": author}')
        db.execute('INSERT INTO books (author_id, isbn, title, year) VALUES'
                   ' (:author_id, :isbn, :title, :year) {"author_id": author_id,'
                   ' "isbn": isbn, "title": title, "year": year')
    db.commit()

if __name__ == “__main__”:
	main()
