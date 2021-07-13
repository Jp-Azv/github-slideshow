print("Digite 'a' para média geométrica")
print("Digite 'b' para média ponderada")
print("Digite 'c' para média harmônica")
print("Digite 'd' para média aritmética")

media_geometrica = 'a'
media_ponderada = 'b'
media_harmonica = 'c'
media_aritmetica  = 'd'

media_escolhida = input('Digite a média escolhida: ')

if media_escolhida == 'a':
    num1 = int(input('Digite seu 1º número: '))
    num2 = int(input('Digite seu 2º número: '))
    num3 = int(input('Digite seu 3º número: '))
    resultado1 = (num1*num2*num3)**(1/3)
    print("O valor da média harmônica entre {}, {} e {} é {}".format(num1,num2,num3,resultado1))

if media_escolhida == 'b':
    num1 = int(input('Digite seu 1º número: '))
    num2 = int(input('Digite seu 2º número: '))
    num3 = int(input('Digite seu 3º número: '))
    resultado1 = (num1 + 2*(num2) + 3*(num3))/6
    print("O valor da média ponderada entre {}, {} e {} é {}".format(num1, num2, num3, resultado1))

if media_escolhida == 'c':
    num1 = int(input('Digite seu 1º número: '))
    num2 = int(input('Digite seu 2º número: '))
    num3 = int(input('Digite seu 3º número: '))
    resultado1 = 1/((1/num1)+(1/num2)+(1/num3))
    print("O valor da média harmônica entre {}, {} e {} é {}".format(num1, num2, num3, resultado1))

if media_escolhida == 'd':
    num1 = int(input('Digite seu 1º número: '))
    num2 = int(input('Digite seu 2º número: '))
    num3 = int(input('Digite seu 3º número: '))
    resultado1 = (num1+num2+num3)/3
    print("O valor da média aritmética entre {}, {} e {} é {}".format(num1, num2, num3, resultado1))






