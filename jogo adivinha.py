import random
print('***JOGO DE ADIVINHA***')
nome = input('Nome de Usuário: ')
tent = 0
acertos = 0
r = 1
ra = []
loop = True
while loop:
    print("- - - - - - - - - -")
    print("RODADA", r)
    num = random.sample(range(10), 1)
    print("NÚMERO SORTEADO...")

    for i in range(1, 4):
        palpite = int(input("Palpite: "))
        if palpite == num[0]:
            print("\nVocê acertou!")
            print("Tentativas:", i)
            tent += 1
            acertos += 1
            ra.append(r)
            break
        if palpite > num[0]:
            print('Chute um valor menor')
            tent += 1
        else:
            print("Chute um valor maior")
            tent += 1

    print("\nNúmero sorteado:", num)
    print("- - - - - - - - - -")
    op = input("Continuar? S - Sim / N - Não: ")
    if op == 'n':
        loop = False
        print('\n- - - - - - - - - -')
        print(f'{nome} acertou nas rodadas: {ra}')
        print(f'De {tent} tentativas {nome} acertou {acertos} palpites e errou {(tent - acertos)}.')
        print("Fechando o jogo...")
        print("- - - - - - - - - -")
    r += 1
