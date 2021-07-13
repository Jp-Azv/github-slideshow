import random

x = random.randrange(1,101)
y = random.randrange(1,101)
z = random.randrange(1,101)
soma1 = x+y+z
print('QUESTÃO 1')
print('')
resposta1 = int(input('Quanto é {}+{}+{} ?'.format(x,y,z)))
acertos = 0
if resposta1 == soma1:
    acertos += 1

a = random.randrange(1,101)
b = random.randrange(1,101)
c = random.randrange(1,101)
soma2 = a+b+c
print('')
print('QUESTÃO 2')
print('')
resposta2 = int(input('Quanto é {}+{}+{} ?'.format(a,b,c)))
if resposta2 == soma2:
    acertos +=  1
print('')
print('Você acertou {} questôes'.format(acertos))
print('')
print('CORREÇÃO')
print('')
if resposta1 == soma1:
    print('Você acertou a 1º questão')
if resposta2 == soma2:
    print('Você acertou a 2º questão')
if resposta1!=soma1 and resposta2!=soma2:
    print('Você não acertou nenhuma questão')