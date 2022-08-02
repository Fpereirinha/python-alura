class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titula = titular
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def extrato(self):
        print(f'Conta: {self.numero} Titular: {self.titula} Saldo: {self.saldo} Limite: {self.limite}')

    def transferir(self, conta, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            conta.saldo += valor
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



