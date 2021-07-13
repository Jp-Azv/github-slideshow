numero1 = float(input('Digite o 1º número: '))
numero2 = float(input('Digite o 2º número: '))

if numero1 % numero2 == 0:
    print('O {} é divisível por {}'.format(numero1, numero2))
else:
    print('O {} não é divisível por {}'.format(numero1, numero2))
