preco_antigo = float(input('Digite o preço do produto: '))

while preco_antigo <= 50:
    preco_novo = preco_antigo*1.05
    if preco_novo <= 80:
        print('Barato')
    if preco_novo >80 and preco_novo <= 120:
        print('Normal')
    if preco_novo >120 and preco_novo <= 200:
        print('Caro')
    else:
        print('Muito caro')
    break

while preco_antigo > 50 and preco_antigo <= 100:
    preco_novo = preco_antigo*1.10
    if preco_novo <= 80:
        print('Barato')
    if preco_novo >80 and preco_novo <= 120:
        print('Normal')
    if preco_novo >120 and preco_novo <= 200:
        print('Caro')
    else:
        print('Muito caro')
    break

while preco_antigo > 100:
    preco_novo = preco_antigo*1.15
    if preco_novo <= 80:
        print('Barato')
    if preco_novo >80 and preco_novo <= 120:
        print('Normal')
    if preco_novo >120 and preco_novo <= 200:
        print('Caro')
    else:
        print('Muito caro')

    break

