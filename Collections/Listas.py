from abc import abstractmethod, ABCMeta


class Conta(metaclass=ABCMeta):
    def __init__(self, conta):
        self.conta = conta
        self.saldo = 0

    @abstractmethod
    def passa_o_mes(self):
        pass

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f'[Código: {self.conta} Saldo: {self.saldo}]'


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self.saldo -= 3


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self.saldo *= 1.01
        self.saldo -= 3


class ContaInvestimento(Conta):
    pass


class ContaSalario:
    def __init__(self, codigo):
        self.conta = codigo
        self.saldo = 0

    def __str__(self):
        return f'[Codigo: {self.conta} Saldo: {self.saldo}]'

    def deposita(self, valor):
        self.saldo += valor

    def __eq__(self, other):
        return self.saldo == other.saldo and self.conta == other.conta


def deposita_all(lista_de_contas, valor):
    for conta in lista_de_contas:
        if type(conta) == ContaCorrente or type(conta) == ContaPoupanca:
            conta.deposita(valor)


c1 = ContaPoupanca(548)
c1.deposita(200)
c2 = ContaCorrente(321)
lc = [c1, c2]
lc.insert(0, 76)
for c in lc:
    print(c)
deposita_all(lc, 5222)

for c in lc:
    if type(c) == ContaCorrente or type(c) == ContaPoupanca:
        c.passa_o_mes()
        print(c)

ContaTeste = ContaSalario(22)
ContaTeste2 = ContaSalario(22)
ContaTeste3 = ContaCorrente(22)
x = [ContaTeste]
print(ContaTeste2 and c1 in x)
print(ContaTeste2 in x)
print(ContaTeste == ContaTeste2)
print(ContaTeste == ContaTeste3)
