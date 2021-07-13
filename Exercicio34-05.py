nota = float(input('Digite a sua nota: '))
faltas = int(input('Digite a quantidade de faltas:'))


if nota  >= 0 and nota < 4:
    print('Conceito E')

if nota >= 4 and nota < 5:
    if faltas <= 20:
        print('Conceito D')
    else:
        print('Conceito E')

if nota >= 5 and nota < 7.5:
    if faltas <= 20:
        print('Conceito C')
    else:
        print('Conceito D')

if nota >= 7.5 and nota < 9.0:
    if faltas <= 20:
        print('Conceito B')
    else:
        print('Conceito C')

if nota >= 9 and nota < 10:
    if faltas <= 20:
        print('Conceito A')
    else:
        print('Conceito B')

