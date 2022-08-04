class ExtractorUrl:
    def __init__(self, url):
        self.url = url.strip() if type(url) == str else ''
        self.valida_url()

    def valida_url(self):
        if not self.url:
            raise ValueError("Url vazia.")
        if not self.url.startswith('www') and not self.url.startswith('https'):
            raise ValueError("url inválida")

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


site1 = ExtractorUrl('www.bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar')


print(site1.buscar_parametro('quantidade'))


