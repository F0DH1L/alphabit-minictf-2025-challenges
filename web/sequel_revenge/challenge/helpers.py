# create clubs db
import sqlite3
from flag import FLAG


def create_db():
    conn = sqlite3.connect('clubs.db')
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS clubs')
    conn.commit()
    conn.close()
    conn = sqlite3.connect('clubs.db')
    c = conn.cursor()
    c.execute(
        '''CREATE TABLE IF NOT EXISTS clubs(id INTEGER PRIMARY KEY, name TEXT, UCL_WON INTEGER)''')
    conn.commit()
    conn.close()
    conn = sqlite3.connect('clubs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS flags_table(id INTEGER PRIMARY KEY, flag TEXT)''')
    conn.commit()
    conn.close()
    conn = sqlite3.connect('clubs.db')
    c = conn.cursor()
    c.execute('''INSERT INTO flags_table (flag) VALUES ("'''+FLAG+'''")''')
    conn.commit()
    conn.close()


# sort clubs

def sort_clubs(order_by='UCL_WON'):
    try:
        conn = sqlite3.connect('clubs.db')
        c = conn.cursor()
        c.execute(f"SELECT * FROM clubs ORDER BY {order_by} DESC")
        result = c.fetchall()
        conn.commit()
        conn.close()
        if result:
            return result
    except Exception as e:
        print(e)
        return False
    return False



def add_clubs(name, UCL_WON):
    try:
        conn = sqlite3.connect('clubs.db')
        c = conn.cursor()
        c.execute("INSERT INTO clubs (name, UCL_WON) VALUES (?, ?)",
                  (name, UCL_WON))
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
        return False
    return True

# insert items


def fill():
    add_clubs('REAL MADRID', 15)
    add_clubs('AC MILAN', 7)
    add_clubs('CHELSEA', 2)
    add_clubs('BAYERN MUNICH', 6)
    add_clubs('INTER MILAN', 3)
    add_clubs('FC BARCELONA', 5)
    add_clubs('MANCHESTER UNITED', 3)
    add_clubs('LIVERPOOL', 6)