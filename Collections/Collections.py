from abc import abstractmethod, ABCMeta
from operator import attrgetter
from functools import total_ordering


@total_ordering
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

    def __lt__(self, other):
        if self.saldo == other.saldo:
            return self.conta < other.conta
        return self.saldo < other.saldo


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self.saldo -= 3


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self.saldo *= 1.01
        self.saldo -= 3


class ContaInvestimento(Conta):
    pass


@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self.conta = codigo
        self.saldo = 0

    def __str__(self):
        return f'[Codigo: {self.conta} Saldo: {self.saldo}]'

    def deposita(self, valor):
        self.saldo += valor

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False
        return self.saldo == other.saldo and self.conta == other.conta

    def __lt__(self, other):
        if self.saldo == other.saldo:
            return self.conta < other.conta
        return self.saldo < other.saldo


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
ContaTeste.deposita(20)
print(ContaTeste == ContaTeste2)
'Instance of !!!! <<< Metodo importante em EQ'
x = [1, 88, 7, 2, 69, 54, 2, 5, 1, 51, 52]
print(sorted(x))
for v in sorted(x):
    print(v)

lc2 = [c, c1, c2, ContaTeste, ContaTeste2, ContaTeste3]
'''for conta in sorted(lc2, key=attrgetter('saldo')):   // key=attrgetter(primeiro_parametro, segundo_parametro) // sald
o / codigo
    print(conta)'''
for conta in sorted(lc2):
    print(conta)

print('*'*50)
for conta in sorted(lc2, reverse=True):
    print(conta)
