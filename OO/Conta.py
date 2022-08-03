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
            self.sacar(valor)
            conta.depositar(valor)
            print("Transferência efetuada com sucesso.")
        else:
            print("Não foi possivel realizar a transferencia.")
    def get_saldo(self):
        return self.__saldo
    def set_limite(self, valor):
        self.__limite += valor
    def get_limite(self):
        return self.__limite


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
c2.set_limite(500)
print(c2.get_limite())

x = c.get_saldo() + c2.get_saldo()



