import sqlite3
import os

conn = sqlite3.connect(f'{os.getcwd()}//db_repo//notes.db', check_same_thread = False)
cur = conn.cursor()

def get_books():
    query = f"""
        SELECT DISTINCT liter FROM notes
        """
    cur.execute(query)
    conn.commit()

    return [x[0] for x in cur.fetchall() if x[0] != None]

def get_cat():
    query = f"""
        SELECT DISTINCT category FROM notes
        """
    cur.execute(query)
    conn.commit()

    return [x[0] for x in cur.fetchall() if x[0] != None]

def add2db(table, columns, values):
    q_marks = str(tuple('?' for i in values)).replace("'", "")
    query = f"""
            INSERT INTO {table} {str(columns)} VALUES {q_marks}
            """
    cur.execute(query, values)
    conn.commit()