def meusql():
    return ['''
    CREATE TABLE user(
        cpf CHAR(36) NOT NULL PRIMARY KEY,
        nome CHAR(36),
        sobrenome CHAR(36)
    );''', '''
    CREATE TABLE contas(
        num CHAR(10) NOT NULL PRIMARY KEY,
        cpf CHAR(12),
        saldo NUMERIC,
        FOREIGN KEY (cpf) REFERENCES user(cpf)
    );''']
