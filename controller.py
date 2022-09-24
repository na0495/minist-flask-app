from db import get_db


def insert_book(name, price, rate):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO books(name, price, rate) VALUES (?, ?, ?)"
    cursor.execute(statement, [name, price, rate])
    db.commit()
    return True


def update_book(id, name, price, rate):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE books SET name = ?, price = ?, rate = ? WHERE id = ?"
    cursor.execute(statement, [name, price, rate, id])
    db.commit()
    return True


def delete_book(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM books WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, name, price, rate FROM books WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_books():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, name, price, rate FROM books"
    cursor.execute(query)
    return cursor.fetchall()