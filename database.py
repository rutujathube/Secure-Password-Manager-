import sqlite3


def connect():
    return sqlite3.connect("passwords.db")


def create_tables():

    con = connect()
    cur = con.cursor()


    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
    )
    """)


    cur.execute("""
    CREATE TABLE IF NOT EXISTS passwords(
    id INTEGER PRIMARY KEY,
    website TEXT,
    username TEXT,
    password TEXT
    )
    """)


    con.commit()
    con.close()



def add_user(username,password):

    con=connect()
    cur=con.cursor()

    cur.execute(
    "INSERT INTO users(username,password) VALUES (?,?)",
    (username,password)
    )

    con.commit()
    con.close()



def check_user(username):

    con=connect()
    cur=con.cursor()

    cur.execute(
    "SELECT password FROM users WHERE username=?",
    (username,)
    )

    result=cur.fetchone()

    con.close()

    return result



def save_password(site,user,password):

    con=connect()
    cur=con.cursor()


    cur.execute(
    "INSERT INTO passwords VALUES(NULL,?,?,?)",
    (site,user,password)
    )


    con.commit()
    con.close()



def get_passwords():

    con=connect()
    cur=con.cursor()


    cur.execute(
    "SELECT * FROM passwords"
    )


    data=cur.fetchall()

    con.close()

    return data