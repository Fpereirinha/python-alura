class Programa:
    def __init__(self, nome, ano):
        self._like = 0
        self._nome = nome.title()
        self._ano = ano

    @property
    def like(self):
        return self._like

    def dar_like(self, qtt=1):
        self._like += qtt

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


class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self.__programas = programas

    def __getitem__(self, item):
        return self.programas[item]


    @property
    def programas(self):
        return self.__programas

    def __len__(self):
        return len(self.programas)





s1 = Serie("Gotham", 2019, 2)
f2 = Filme('Filme2', 2022, 322)
f1 = Filme("Filme1", 2022, 233)
f3 = Filme("Todo mundo em panico", 1999, 100)
s2 = Serie("Demolidor", 2016, 5)
s2.dar_like(22)

filmes_e_series = [f2, f1, s1, s2, f3]
pl_fim_de_semana = Playlist("Fim de Semana", filmes_e_series)

for count, programa in enumerate(pl_fim_de_semana):
    print(f'{pl_fim_de_semana.nome} {count+1}° {programa}')