class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titula = titular
        self.saldo = saldo
        self.limite = limite
c = Conta(123,"pedro", 20, 1000)
print(c.saldo, c.limite, c.numero, c.titula)
