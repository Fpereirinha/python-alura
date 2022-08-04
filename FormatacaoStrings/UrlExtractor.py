'''url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(url[0:url.index('?')])
print(url.find('real'))
x = url[url.find('real') + len('real')+1:]
print(url[url.index('?')+1:])
url = url[url.index(':') +3 :]
print(x)
p1 = x[:x.index('&')]
print(p1)
p2 = x[x.index('&') +1:]
print(p2)
print(url.index('moeda'))'''

#url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
url = '     '
if len(url.strip()) == 0:
    raise ValueError("Vazio !")
else:
    # Separa base e parâmetros
    indice_interrogacao = url.find('?')
    url_base = url[:indice_interrogacao]
    url_parametros = url[indice_interrogacao+1:]
    print(url_parametros)

    # Busca o valor de um parâmetro
    parametro_busca = 'quantidade'
    indice_parametro = url_parametros.find(parametro_busca)
    indice_valor = indice_parametro + len(parametro_busca) + 1
    indice_e_comercial = url_parametros.find('&', indice_valor)
    if indice_e_comercial == -1:
        valor = url_parametros[indice_valor:]
    else:
        valor = url_parametros[indice_valor:indice_e_comercial]

    print(valor)