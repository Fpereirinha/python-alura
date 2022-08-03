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
    def ano(self):
        return self._ano

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao

    @property
    def duracao(self):
        return self.__duracao

    def __str__(self):
        return f'{self.nome} {self.ano} {self.duracao} {self.like}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.__temporadas = temporadas

    @property
    def temporadas(self):
        return self.__temporadas

    def __str__(self):
        return f'{self.nome} {self.ano} {self.temporadas} {self.like}'


s1 = Serie("Gotham", 2019, 2)
f2 = Filme('Filme2', 2022, 322)
f1 = Filme("Filme1", 2022, 233)


filmes_e_series = [f2, f1, s1]

for programa in filmes_e_series:
    print(programa)
