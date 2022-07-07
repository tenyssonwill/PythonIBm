import sqlite3

def dbconnect(bd):
    conn = sqlite3.connect(bd)
    if conn:
        print('Conectado')
        return conn
    else:
        print('Erro')

def create(conn, sql):
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def update(conn, sql):
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def update(conn, sql):
    cur = conn.cursor()
    cur.execute(sql)
    res = cur.fetchall()
    print(res)
