from modules.crude import *
from modules.sql import meusql

conn = dbconnect('contas.db')
sql = '''
INSERT INTO user (cpf,nome,sobrenome)
VALUES ('283671068-30','Tenysson', 'Will')
'''
# for s in meusql():
#     create(conn, s)
create(conn, sql)
conn.close()


