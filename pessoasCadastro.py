somaIdade = 0 # contador
mediaIdade = 0 # contador
maiorIdadeH = 0 # homem mais velho
nomeHvelho = '' # string vazia
totmulher20 = 0 # contador
for p in range (1, 5):
    print('-- {}ª PESSOA --'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): '))
    somaIdade += idade # soma todas as idades
    if p == 1 and sexo in 'Mm': # se for a 1ª pessoa e o sexo for Mm
        maiorIdadeH = idade # recebe a 1ª idade digitada
        nomeHvelho = nome # recebe o 1º nome digitado
    if sexo in 'Mm' and idade > maiorIdadeH: # se for Mm e a idade for maior que p == 1 então
        maiorIdadeH = idade # idade digitada substitui o 1º valor
        nomeHvelho = nome # substitui pelo nome do que tiver maior idade
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaIdade = somaIdade / 4 # cálculo da media de idade
print('A média de idade do grupo é {} anos'.format(mediaIdade))
print('O homem mais velho se chama {} e tem {} anos'.format(nomeHvelho, maiorIdadeH))
print('{} mulher(es) tem menos de 20 anos'.format(totmulher20))




