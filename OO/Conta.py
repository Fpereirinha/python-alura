class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titula = titular
        self.__saldo = saldo
        self.__limite = limite

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def extrato(self):
        print(f'Conta: {self.__numero} Titular: {self.__titula} Saldo: {self.__saldo} Limite: {self.__limite}')

    def transferir(self, conta, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            conta.__saldo += valor
        else:
            print("Não foi possivel realizar a transferencia.")


c = Conta(123,"pedro", 20, 1000)
c2 = Conta(222,"joao", 300, 1000)
c2.extrato()
c.extrato()
c.depositar(2000)
c.extrato()
c.sacar(1500)
c.extrato()
c.transferir(c2, 300)
c.extrato()
c2.extrato()
c2.sacar(22)




