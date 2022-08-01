from random import randint


def jogo_adivinha():
    tentativas = n1 = nf = resp = 0
    print('*'*20)
    print('Jogo da adivinhação')
    print('*'*20)
    dificuldade = int(input("Qual o nivel de dificuldade que deseja ? 1- facil 2- normal 3- dificil"))
    if dificuldade == 1:
        tentativas = 3
        n1 = randint(0, 10)
        nf = 10
    elif dificuldade == 2:
        tentativas = 10
        n1 = randint(0, 100)
        nf = 100
    elif dificuldade == 3:
        tentativas = 50
        n1 = randint(0, 1000)
        nf = 1000
    for c in range(tentativas):
        print(f'Tentativa {c+1} de {tentativas}.')
        resp = int(input(f"Digite um numero de 0 a {nf} para tentar acertar."))
        while resp < 0 or resp > nf:
            print("Valor digitado fora do intervalo, digite novamente.")
            resp = int(input("Digite um numero de 0 a 10 para tentar acertar."))
        if resp == n1:
            print("Parabéns, você acertou !")
            break
        else:
            if n1 > resp:
                print("Mais alto !")
            else:
                print("Mais baixo !")
        if c < 2:
            print(f"Resposta errada, tente mais uma vez.")
    if resp != n1:
        print("Você perdeu.")


if __name__ == '__main__':
    jogo_adivinha()
