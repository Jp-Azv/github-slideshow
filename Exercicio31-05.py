altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))

while altura <= 1.20:
    if peso <= 60:
        print('Seu tipo é o H')
    if peso > 60 and peso <= 90:
        print('Seu tipo é o D')
    else:
        print('Seu tipo é o G')
    break
while altura > 1.20 and altura <= 1.70:
    if peso <= 60:
        print('Seu tipo é o B')
    if peso > 60 and peso <= 90:
        print('Seu tipo é o E')
    else:
        print('Seu tipo é o H')
    break
while altura > 1.70:
    if peso <= 60:
        print('Seu tipo é o C')
    if peso > 60 and peso <= 90:
        print('Seu tipo é o F')
    else:
        print('Seu tipo é o I')
    break

