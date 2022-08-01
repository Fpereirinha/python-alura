from adivinhacao import jogo_adivinha
from forca import jogo_forca
while True:
    print('*'*20)
    print('Escolha seu Jogo')
    print('*'*20)
    resp = int(input("Qual jogo deseja jogar ? [1] Adivinhação   [2] Forca"))
    if resp == 1:
        print("Jogo escolhido ADIVINHAÇÃO.")
        jogo_adivinha()
    elif resp == 2:
        print("Jogo escolhido FORCA.")
        jogo_forca()
    continuar = input("Deseja continuar ? [Sim] / [Não]").upper().strip()[0]
    if continuar == 'N':
        print("Saindo da aplição, obrigado por jogar.")
        break
