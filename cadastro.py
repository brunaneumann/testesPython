print('==' * 10)
print('CADASTRE UM USUÁRIO')
print('==' * 10)
continuar = 'SsNn'
mais18 = homens = mulheres = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('QUER CONTINUAR? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'{mais18} pessoas com mais de 18 anos.')
print(f'{homens} homens cadastrados')
print(f'{mulheres} mulheres com menos de 20 anos')