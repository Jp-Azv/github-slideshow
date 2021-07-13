p1 = 100
p2 = 101
p3 = 102
conta = 0
quantidade = int(input('Quantos produtos você deseja pedir ?'))
i = 0

while quantidade > i:
    print('Qual o código do {} produto ?'.format(i+1))
    produto = (int(input('')))
    if produto == p1:
        conta += 1.20
    if produto == p2:
        conta += 1.30
    if produto == p3:
        conta += 1.50
    i += 1


print('A sua conta totaliza:')
print(conta)

