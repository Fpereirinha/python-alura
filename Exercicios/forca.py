from random import randint


def jogo_forca():
    nome = ["Pedro", "Joao", "Lucas", "Sabrina"]
    indice = randint(0, len(nome)-1)
    palavra_secreta = nome[indice].upper()
    letras_separadas = []
    chances = 5
    letras_acertadas = []
    resp = ""
    for letra in nome[indice]:
        letras_separadas.append(letra.upper())
        letras_acertadas.append("_")
    print(letras_separadas)
    print(letras_acertadas)
    print('*'*20)
    print('Jogo da Forca')
    print('*'*20)
    print(f'O nome começa com a letra {letras_separadas[0].upper()} e termin'
          f'a com a letra {letras_separadas[len(letras_separadas)-1].upper()} '
          f'e possui {len(letras_separadas)} letras.')
    print("Você possui 5 chances para acertar !")
    for x in range(chances):
        if resp == palavra_secreta or letras_acertadas.count("_") == 0:
            break
        print(f"Tentativa {x+1} de {chances}")
        resp = input("Digite uma letra para tentar acertar, ou a palavra completa: ").upper().strip()
        if resp == palavra_secreta:
            print("Parabens, você acertou !!!")
            break
        elif resp in letras_separadas:
            print("Letra dentro da palavra !! Parabéns !")
            for c, letra in enumerate(letras_separadas):
                if letra == resp:
                    letras_acertadas[c] = letra
            for letra in letras_acertadas:
                print(f'{letra}  ', end='')
            print('')
            while True:
                if resp == palavra_secreta or letras_acertadas.count("_") == 0:
                    print("Parabens você venceu !")
                    break
                resp = input("Digite mais uma letra, sem disperdiçar a chances: ").upper().strip()
                if resp in letras_separadas and resp not in letras_acertadas:
                    for c, letra in enumerate(letras_separadas):
                        if letra == resp:
                            letras_acertadas[c] = letra
                    for letra in letras_acertadas:
                        print(f'{letra}  ', end='')
                    print('')
                else:
                    print("letra ja na lista ou errada !")
                    break
        else:
            print("letra não encontrada.")
    if resp != palavra_secreta and letras_acertadas.count("_"):
        print("Você perdeu, obrigado por jogar !")


if __name__ == '__main__':
    jogo_forca()
