from random import randint # importar número aleatório
vitoria = 0 #contador de vitórias dentro do laço, contar quantas jogadas
print('=*' * 10)
print('PAR OU ÍMPAR')
print('=*' * 10)

while True:
    computador = randint(0, 10) # aleatório de 0 a 10
    jogador = int(input('Digite um valor: '))
    soma = jogador + computador
    parOuimpar = ' '
    while parOuimpar not in 'PI': #enquanto par ou impar NÃO ESTIVER EM PI
        parOuimpar = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {soma}')
    if soma % 2 == 0: #saber se é par ou ímpar
        print('DEU PAR')
    else:
        print('DEU ÍMPAR')
    if parOuimpar == 'P': #se for P executa
        if soma % 2 == 0:
            print('VOCÊ GANHOU')
            vitoria =+ 1
        else:
            print('VOCÊ PERDEU')
            break #quebra quando perde
    elif parOuimpar == 'I': #se for I executa
        if soma % 2 == 1:
            print('VOCÊ GANHOU')
            vitoria += 1
        else:
            print('VOCÊ PERDEU')
            break
    print('Vamos jogar de novo...')
print(f'GAME OVER! Você venceu {vitoria} vezes')




