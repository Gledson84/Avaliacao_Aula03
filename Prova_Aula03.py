numero = 7
contador = 1
while contador <= 3:
    palpite = int(input('Digite um número: '))
    if palpite != numero:
        print(f'Número {palpite} Incorreto, não desanime você consegue')
    else:
        print(f'Número {palpite}, Parabéns você acertou')
        break
    contador += 1