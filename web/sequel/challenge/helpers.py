# create clubs db
import sqlite3
import string
import random
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
    tmp1 = ''.join(random.choice(string.ascii_lowercase) for i in range(30))
    tmp2 = ''.join(random.choice(string.ascii_lowercase) for i in range(30))
    c.execute('''CREATE TABLE IF NOT EXISTS '''+tmp1 +
              '''(id INTEGER PRIMARY KEY, '''+tmp2+''' TEXT)''')
    conn.commit()
    conn.close()
    conn = sqlite3.connect('clubs.db')
    c = conn.cursor()
    c.execute('''INSERT INTO '''+tmp1+''' ('''+tmp2 +
              ''') VALUES ("'''+FLAG+'''")''')
    conn.commit()
    conn.close()
def search_for_product(search):
    try:
        conn = sqlite3.connect('clubs.db')
        c = conn.cursor()
        c.execute("SELECT * FROM clubs WHERE name LIKE '%"+search+"%'")
        result = c.fetchall()
        conn.commit()
        conn.close()
        if result:
            return result
    except Exception as e:
        print(e)
        return False
    return False
# add product
def add_product(name, UCL_WON):
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
    add_product('REAL MADRID', 15)
    add_product('AC MILAN', 7)
    add_product('CHELSEA', 2)
    add_product('BAYERN MUNICH', 6)
    add_product('INTER MILAN', 3)
    add_product('FC BARCELONA', 5)
    add_product('MANCHESTER UNITED', 3)
    add_product('LIVERPOOL', 6)