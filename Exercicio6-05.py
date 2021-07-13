numero_1 = input('Digite o primeiro número: ')
numero_2 = input('Digite o segundo número: ')

if numero_2 > numero_1:
    print(numero_2, 'é maior')
elif numero_2 == numero_1:
    print('Os dois números sao iguais')
else:
    print(numero_1, 'é maior')

print('A diferença entre ambos é: ', int(numero_1) - int(numero_2))
