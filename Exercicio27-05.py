idade = int(input('Digite a sua idade:'))

if idade < 5:
    print('Você não está em nenhuma das categorias')
if idade >= 5 and idade <= 7:
    print('Você está na categoria Infantil A')
if idade > 7 and idade <= 10:
    print('Você está na categoria Infantil B')
if idade > 10 and idade <= 13:
    print('Você está na categoria Juvenil A')
if idade > 13 and idade <= 17:
    print('Você está na categoria Juvenil B')
elif idade >= 18:
    print('Você está na categoria Sênior')