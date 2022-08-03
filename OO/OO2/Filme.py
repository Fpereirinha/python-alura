class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.__ano = ano
        self.__duracao = duracao
        self.__like = 0

    @property
    def like(self):
        return self.__like

    def dar_like(self):
        self.__like += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__like = 0
        self.__nome = nome.title()
        self.__ano = ano
        self.__temporadas = temporadas

    @property
    def like(self):
        return self.__like

    def dar_like(self):
        self.__like += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()


f1 = Filme("astro nauta", 22, 2)
print(f1.nome)
