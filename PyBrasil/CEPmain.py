from CEP import CEP

cep1 = CEP('09810620')
print(cep1.format())

print(cep1.request())
print(cep1.bairro, cep1.localidade, cep1.uf)