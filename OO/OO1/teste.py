def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta


def depositar(conta, valor):
    conta["saldo"] += valor


def saque(conta, valor):
    conta["saldo"] -= valor

c2 = cria_conta(122, "joao", 555, 1000)
print(c2["saldo"])
depositar(c2, 1000)
print(c2["saldo"])
saque(c2,200)
print(c2["saldo"])

