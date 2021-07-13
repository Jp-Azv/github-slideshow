lado_a = float(input('Digite o lado 1: '))
lado_b = float(input('Digite o lado 2: '))
lado_c = float(input('Digite o lado 3: '))

if (lado_a + lado_b)>lado_c and (lado_a+lado_c)>lado_b and (lado_b+lado_c)>lado_a:
    print('O triângulo é válido')

print('')

if lado_a == lado_b and lado_a == lado_c:
    print('O triângulo é equilátero')
elif lado_a == lado_b or lado_b == lado_c:
    print('O triângulo é isósceles')
else:
    print('O triângulo é escaleno')
