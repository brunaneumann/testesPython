while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    if n < 0:
        break
    print('=' * 15)
    for c in range (1, 11): #for ignora o último termo
        print(f'{n} x {c} = {n * c}')
    print('=' * 15)
print('Fim do programa.')