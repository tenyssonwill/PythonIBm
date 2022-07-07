d = {'cpf': '298220858-85', 'nome': 'Daniel', 'sobrenome': 'Tiezzi'}

d1 ={}

d1['298220858-85'] = {'nome': 'Jose', 'sobrenome': 'Tiezzi', 'cc': '0002-1', 'saldo':20}

from contas import Conta

cc1 = Conta('123456789-00', 'Daniel', 'Tiezzi')

cc1.saldo = 500
print(cc1.saldo)

print(cc1.__dict__)

cc1.deposito(500)
print(cc1.getter())
cc1.saque(750)
print(cc1.getter())
print(cc1.__dict__)