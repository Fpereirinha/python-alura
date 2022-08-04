import re


class ExtractorUrl:
    def __init__(self, url):
        self.url = url.strip() if type(url) == str else ''
        self.valida_url()

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f'Url parametros: {self.url_parametros}\n' \
               f'Url completa: {self.url_base}'

    def __eq__(self, other):
        return self.url == other.url

    def valida_url(self):
        if not self.url:
            raise ValueError("Url vazia.")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("Url inválida")

    def conversor(self):
        cotacao = 0
        quantidade = self.buscar_parametro('quantidade')
        origem = self.buscar_parametro('moedaOrigem').title()
        destino = self.buscar_parametro('moedaDestino').title()
        if origem == 'Dolar':
            cotacao = 5.5
        elif origem == 'Euro':
            cotacao = 6
        elif origem == 'Bitcoin':
            cotacao = 100000
        else:
            raise ValueError("Não reconheço essa moeda.")
        return f'O valor convertido de {quantidade} {origem} para {destino} é R${float(quantidade) * cotacao:.2f}.'

    @property
    def url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    @property
    def url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def buscar_parametro(self, parametro_busca):
        # Busca o valor de um parâmetro
        indice_parametro = self.url_parametros.find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.url_parametros.find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.url_parametros[indice_valor:]
        else:
            valor = self.url_parametros[indice_valor:indice_e_comercial]
        return valor


site1 = ExtractorUrl('www.bytebank.com/cambio?quantidade=100&moedaOrigem=euro&moedaDestino=real')
site2 = ExtractorUrl('www.bytebank.com/cambio?quantidade=500&moedaOrigem=dolar&moedaDestino=real')
print(len(site1))
print(site1)
print(site1 == site2)
print(site1.conversor())
