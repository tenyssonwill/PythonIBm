class Conta:

    def __init__(self, cpf, nome, sobrenome) -> None:
        self._cpf = cpf
        self.nome = nome
        self.sobrenome = sobrenome
        self.__saldo = 0

    def getter(self):
        return self.__saldo

    def deposito(self, val):
        self.__saldo += val

    # def saque(self, val):
    #     if self.__saldo >= val:
    #         print('Permitido')
    #         self.__saldo -= val
    #     else:
    #         print('Negado')
    #         self.__saldo

    def saque(self, val):
        self.__saldo = self.__saldo - val if self.__saldo >= val else self.__saldo

class Pf(Conta):

    def __init__(self, num, cpf, nome, sobrenome) -> None:
        super().__init__(num)
        self.cpf = cpf
        self.nome = nome
        self.sobrenome = sobrenome


class Pj(Conta):

    def __init__(self, num, cnpj, nome) -> None:
        super().__init__()