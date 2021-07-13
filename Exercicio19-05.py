numero = int(input('Digite seu número: '))

if numero %5 == 0 and numero %3 == 0:
    print('Número inválido')
elif numero %3 == 0:
    print('O {} é divisível por 3'.format(numero))
elif numero %5 == 0:
    print('O {} é divisível por 5'.format(numero))

