from random import randint


def jogo_forca():
    'nome = ["Pedro", "Joao", "Lucas", "Sabrina"]'
    arquivo = open("palavras.txt", "r")
    nomes = [linha.strip() for linha in arquivo]
    arquivo.close()
    indice = randint(0, len(nomes) - 1)
    palavra_secreta = nomes[indice].upper()
    print(nomes)
    chances = 5
    letras_acertadas = ["_" for letra in palavra_secreta]
    resp = ""
    '''for letra in nome[indice]:
        palavra_secreta.append(letra.upper())
        letras_acertadas.append("_")'''
    print(palavra_secreta)
    print(letras_acertadas)
    print('*'*20)
    print('Jogo da Forca')
    print('*'*20)
    print(f'O nome começa com a letra {palavra_secreta[0].upper()} e termin'
          f'a com a letra {palavra_secreta[len(palavra_secreta)-1].upper()} '
          f'e possui {len(palavra_secreta)} letras.')
    print("Você possui 5 chances para acertar !")
    for x in range(chances):
        if resp == palavra_secreta or letras_acertadas.count("_") == 0:
            break
        print(f"Tentativa {x+1} de {chances}")
        resp = input("Digite uma letra para tentar acertar, ou a palavra completa: ").upper().strip()
        if resp == palavra_secreta:
            print("Parabens, você acertou !!!")
            break
        elif resp in palavra_secreta and resp not in letras_acertadas:
            print("Letra dentro da palavra !! Parabéns !")
            for c, letra in enumerate(palavra_secreta):
                if letra == resp:
                    letras_acertadas[c] = letra
            for letra in letras_acertadas:
                print(f'{letra}  ', end='')
            print('')
            while True:
                if resp == palavra_secreta or letras_acertadas.count("_") == 0:
                    print("Parabens você venceu !")
                    break
                resp = input("Digite mais uma letra, sem disperdiçar chances: ").upper().strip()
                if resp in palavra_secreta and resp not in letras_acertadas:
                    for c, letra in enumerate(palavra_secreta):
                        if letra == resp:
                            letras_acertadas[c] = letra
                    for letra in letras_acertadas:
                        print(f'{letra}  ', end='')
                    print('')
                else:
                    print("letra ja na lista ou errada !")
                    break
        else:
            print("letra não encontrada ou já na lista !")
    if resp != palavra_secreta and letras_acertadas.count("_"):
        print("Você perdeu, obrigado por jogar !")


if __name__ == '__main__':
    jogo_forca()
