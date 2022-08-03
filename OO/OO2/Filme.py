class Programa:
    def __init__(self, nome, ano):
        self._like = 0
        self._nome = nome.title()
        self._ano = ano

    @property
    def like(self):
        return self._like

    def dar_like(self):
        self._like += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

class Filme(Programa):
    def __init__(self,nome,ano,duracao):
        super().__init__(nome,ano)
        self._duracao = duracao






class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self._temporadas = temporadas


f2 = Filme('Jonas', 22, 3)
f1 = Filme("astro nauta", 22, 2)
print(f1.nome)
f1.nome = 'joao doido'
print(f1.nome)