import os

from modules.crude import *
from modules.sql import meusql
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()

user = os.getenv('USERNAME')
passwd = os.getenv('PASSWORD')
port = os.getenv('PORT')
database = os.getenv('DB')

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
# conn = dbconnect('contas.db')
# sql = '''
# INSERT INTO user (cpf,nome,sobrenome)
# VALUES ('283671068-30','Tenysson', 'Will')
# '''
#
# sql = '''
# INSERT INTO contas (num,cpf,saldo)
# VALUES ('0001-1','277835208-20', 532.45)
# '''
# for s in meusql():
#     create(conn, s)
# sql = '''
# UPDATE contas SET saldo = 550 WHERE num = '0001-1'
# '''

# sql = '''
# SELECT * FROM contas
# '''
# # create(conn, sql)
# update(conn, sql)
# conn.close()
