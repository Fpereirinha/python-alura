from collections import defaultdict, Counter
usuarios_data_science = {5, 4, 88, 9}
usuarios_machine_learning = {88, 225, 110, 524}
# Sets não assumem indices e não tem ordenação, não suportam repetição
# e tem um processamento rápido
# junções // e interseção de sets === ||| << &&&  <<<
# Utilizar o | para juntar conjuntos;
# Utilizar o & para juntar apenas números que estão no mesmo conjunto;
# Utilizar o - para remover números repetidos que estão no em dois conjuntos;
# O que é ou (^) exclusivo.
def x(x):
    print(x)
usuarios = {1, 5, 6, 7, 10, 29}
usuarios.add(22)
x(usuarios)
usuarios.add(22)
x(usuarios)
user_lock = frozenset(usuarios) # < conjunto travado !
x(user_lock)

text = "Bem vindo, meu nome é Pedro e tenho 21 anos de idade.Bem vindo, meu nome é Pedro e tenho 21 anos de idade." \
       "Bem vindo, meu nome é Pedro e tenho 21 anos de idade."
set_text = set(text.split())
x(set_text)
for c in set_text:
    print(f'{c}', end=' ')


# dicts para controle
aparicoes = {'Pedro' : 1, 'Joao' : 30, 'Jéssica' : 33, 'Bem' : 2}
x(aparicoes['Pedro'])
print(aparicoes.get('Joao', 'Não encontrado.'))
print(aparicoes.get('Joadso', 'Não encontrado.'))
aparicoes['Jonas'] = 1
x(aparicoes)
aparicoes['Jonas'] = 2
x(aparicoes)
del aparicoes['Jonas']
x(aparicoes)
print('Joao' in aparicoes)
print('Joaso' in aparicoes)
for key, valor in aparicoes.items():
    print(f'{key} = {valor}')

lista_keys = [f"Chave: {chave}" for chave in aparicoes.keys()]
print(lista_keys)
# O que é um dicionário;
# Verificar se o elemento está dentro do dicionário;
# Utilizar o get para verificação;
# Criar um dicionário a partir do dict;
# Adicionar um elemento no dicionário;
# Remover um elemento do dicionário;
# Mostrar os elementos dentro do dicionário;
# Usar a função keys para pegar as chaves;
# Usar a função values para pegar os valores;
# Percorrer linha a linha com a função items.
lower_text = text.lower().split()
aparicoes2 = {}
for palavra in lower_text:
    count = aparicoes2.get(palavra, 0)
    aparicoes2[palavra] = count + 1
print(aparicoes2)
aparicoes3 = defaultdict(int)
for palavra in lower_text:
    aparicoes3[palavra] += 1

print(aparicoes3)
aparicoes4 = Counter(lower_text)
print(aparicoes4)
### Testar letras separadas ///

texto1 = '''A vida de João de Deus (João para seus amigos) é uma história fascinante de dedicação, filosofia e inovação. 
Quando João ainda era muito jovem, ele elaborou um plano para salvar a vida do maior número possível de pessoas de afo
gamento. Ele construiria um barco de madeira e o comandaria para resgatar pessoas que se afogavam. O plano funcionou e 
salvou muitas vidas. Ele se tornou um famoso jovem capitão, que também escreveu vários livros. Eventualmente, ele se 
apos
entou de seu trabalho para dedicar todo o seu tempo às suas crenças. Suas famosas últimas palavras foram “ora soma” 
– “agora eu sou” – expressando a ideia de que ele havia feito o suficiente em sua vida para salvar o maior número po
ssível de pessoas do afogamento.

Em 1628, João de Deus publicou seu livro “Os Mecaayres [sic] de Nomachaes, ou Nova Astronomia”. Ao combinar ideias gr
egas c
om teorias astronômicas árabes mais antigas, João de Deus projetou uma nova maneira de pensar a astronomia que ficou c
onhec
ida como mecânica newtoniana. Este sistema tornou mais fácil para engenheiros de treinamento e outros profissionais rea
lizare
m seus trabalhos sem treinamento por décadas. Também levou à invenção da engenharia e tecnologia modernas, aplicando a m
ecâni
ca newtoniana para criar trens, relógios e outras máquinas. Além de aplicar seu sistema de pensamento no campo da ciên
cia, J
oão também aplicou esse sistema em questões religiosas. Tornou-se padre jesuíta e pregou que devemos amar tanto nos
sos se
melhantes que daríamos nossas vidas por eles, se necessário. livro que publicou aos 40 anos. Ele descreveu como os n
úmero
s poderiam ser usados ​​na multiplicação ou divisão em vez de serem tratados separadamente como os antigos egípcios
 sempre fizeram. Sendo ele próprio um matemático, João de Deus estava muito interessado em aplicar a matemática na v
 ida qu
 otidiana e não apenas no trabalho académico. Ao fazer isso, no entanto, ele observou que a matemática poderia ter uso
 s pr
 áticos se suas aplicações fossem pensadas primeiro. Pensar em tais aplicativos exigia tempo — tempo tanto para analisar 
 as situações minuciosamente quanto para implementar o que foi encontrado durante a análise na vida diária com o mínimo
  de interrupção. João fez exatamente isso com seu algoritmo para encontrar raízes quadradas sem erros compostos ou it
  erações - algo em que os computadores modernos ainda se baseiam mais de 250 anos depois! Sua aplicação para este c
  onceito foi tão revolucionária que mudou não apenas como, mas também o que os matemáticos pensavam ao longo da hi
  stória! Na verdade, esse conceito ainda é ensinado hoje em escolas secundárias em todo o mundo usando seu nome mo
  derno: algoritmo de Euclides (que não é exatamente um algoritmo). Como um aparte, um uso atual do algoritmo de 
  Euclides é criar provas digitais usando computadores – algo com o qual muitas pessoas estão familiarizadas g
  raças a filmes como O Código Da Vinci!'''
texto2 = '''Compreender o mundo ao nosso redor tornou-se mais fácil do que nunca. Graças ao avanço da tecnologia, podem
os aprender e adquirir conhecimento mais rápido do que nunca. A programação é um tipo de programação de software que
 torna isso possível. Na era do computador, muitos empregadores preferem contratar pessoas que aprenderam a usar sof
 tware e programação em todo o seu potencial. É por isso que é crucial que os estudantes universitários aprendam a 
 programar para Pedro se quiserem uma carreira nessa área.

Muitas pessoas consideram a programação uma habilidade difícil de dominar. No entanto, essa atitude é normal durante o
 início da idade adulta. A essa luz, faz sentido que muitos jovens adultos optem por não aprender a programar neste 
 momento de suas vidas. Em vez disso, eles deixariam a complacência assumir o controle e limitar suas escolhas de c
 arreira como resultado. Aqueles que decidem aprender a programar ainda jovens são tipicamente pessimistas que acred
 itam que não terão sucesso de qualquer maneira. Eles podem desistir durante os estágios iniciais de sua educação, m
 as mais tarde encontrarão sucesso por meio da programação, graças ao esforço desde o início. Graças aos cursos univ
 ersitários que ensinam programação, os futuros programadores não precisam mais evitar a complacência e se limitar 
 a esse campo de estudo. Em vez disso, esses cursos universitários ensinam habilidades de resolução de problemas qu
 e lhes renderão uma boa carreira depois de se formarem na faculdade. A maioria dos cursos universitários de progra
 mação são projetados dessa forma para que os alunos possam adquirir as habilidades necessárias para o sucesso sem 
 ter que trabalhar duro primeiro. Aprendendo a programar para Pedro desde cedo, os jovens adultos podem evitar a co
 mplacência e se limitar mais tarde, quando decidem não aprender. Essa abordagem funciona bem no início, pois limit
 a as oportunidades de carreira dos alunos No entanto, uma vez que os alunos aprendem a programar para Pedro, eles 
 podem começar a se limitar, pois aprenderam as habilidades de resolução de problemas necessárias para o sucesso. 
 É importante não se limitar por meio do aprendizado, pois isso limita o potencial de ganhos no futuro – mas isso 
 não significa que não se possa limitar suas ambições o suficiente para ter sucesso na vida. Ao limitar suas ambi
 ções o suficiente para evitar a complacência ao aprender a programar, esses jovens adultos evitarão se limitar 
 ao optar por não aprender. Essa abordagem funciona bem no início, pois limita as oportunidades de carreira dos a
 lunos'''
def aparicoes_no_texto(texto):
    letras = Counter(texto.lower())
    total_de_aparicao = sum(letras.values())
    frequencia = [(letra, float((aparicao/total_de_aparicao) * 100)) for letra, aparicao in letras.items()]
    frequencia = Counter(dict(frequencia))
    mais_comuns = frequencia.most_common(10)
    for chave, valor in mais_comuns:
        print(f'{chave} = {valor:.2f}%')
aparicoes_no_texto(texto1)
print('\n' * 2)
aparicoes_no_texto(texto2)

