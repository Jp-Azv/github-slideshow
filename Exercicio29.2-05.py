import random
gab = []
acertos = 0
i = 0
ques = 1
while i < 5:
    a=random.randrange(1,101)
    b=random.randrange(1,101)
    print('Questão {}:'.format(ques))
    print('')
    print('Quanto é {} + {}'.format(a,b))
    soma = a+b
    resp = int(input())
    if resp == soma:
        gab.append('Você acertou a questão {}'.format(ques))
        acertos+=1
    else:
         gab.append('Você errou a questão {}'.format(ques))
    i+=1
    ques += 1
for r in gab:
    print(r)
print('Numéro de acertos: ')
print(acertos)