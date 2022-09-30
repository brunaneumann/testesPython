from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA 
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 10)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 10)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('OPÇÃO INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('OPÇÃO INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('OPÇÃO INVÁLIDA')


