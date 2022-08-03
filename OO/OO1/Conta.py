from cliente import Cliente
class Conta:
    cod = 1
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titula = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = '001'

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        return valor <= self.__saldo + self.__limite

    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            if self.__saldo < 0:
                self.__limite -= abs(self.__saldo)
                self.__saldo = 0
        else:
            print("Sem limite e sem saldo, não foi possivel completar o saque !")

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

    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self, valor):
        self.__limite += valor

    @staticmethod
    def codigo_banco():
        return f'{1:03}'
    cod2 = 2




cliente1 = Cliente("joao", 1)
print(cliente1.status)
cliente1.status = 2
print(cliente1.status)


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
c2.limite = 200
print(c2.limite)
c3 = Conta(55,'pedro', 500, 500)
c3.sacar(900)
c3.extrato()
print(Conta.codigo_banco())
print(Conta.cod, Conta.cod2)





