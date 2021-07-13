a = float(input("Digite o valor de 'a': "))
b = float(input("Digite o valor de 'b': "))
c = float(input("Digite o valor de 'c': "))

discriminante = ((b**2)-4*a*c)
x_1 = (-(b)+(discriminante)**0.5)/2*a
x_2 = (-(b)-(discriminante)**0.5)/2*a

if discriminante <0:
    print('A equação não possui raízes reais')
if discriminante == 0:
    print('A equação possui apenas uma raíz real')
    print('')
    print(x_1)
if discriminante > 0:
    print('A equação possui duas raízes reais e distintas')
    print('')
    print(x_1, x_2)
