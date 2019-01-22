import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

def main():
    #engine = create_engine(os.getenv("DATABASE URI"))
    engine = create_engine("postgres://stiokmkmdgvyic:e8274ce1c7b53022d220733bb48bab121b4afecfaacde94697f7f360a35e6957@ec2-54-225-237-84.compute-1.amazonaws.com:5432/dfbcvns96ond71")
    db = scoped_session(sessionmaker(bind=engine))

    f = open("books.csv")
    reader = csv.reader(f)
    count = 0

    for isbn, title, author, year in reader:
        try:
            db.execute('INSERT INTO authors (name) VALUES (:name)', {"name": author})
        except:
            count+= 1
            print(f"Duplicate Author {count} Detected")
    db.commit()
    print("Authors added to database")

    for isbn, title, author, year in reader:
        author_id = db.execute('SELECT id FROM authors WHERE name=:author)', {"author": author})

        db.execute('INSERT INTO books (author_id, isbn, title, year) VALUES'
                   ' (:author_id, :isbn, :title, :year)', {"author_id": author_id["id"],
                   "isbn": isbn, "title": title, "year": year})
    db.commit()
    print("Books added to database")

if __name__ == "__main__":
	main()
