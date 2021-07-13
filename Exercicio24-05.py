produto = float(input('Digite o valor do produto: '))
print('Opções de estados disponíveis para a venda do produto:')
print('MG')
print('SP')
print('RJ')
print('MS')

estado1 = input('Digite o estado para o qual você venderá seu produto: ')

if estado1 == 'MG':
    print(produto*1.07)
if estado1 == 'SP':
    print(produto*1.12)
if estado1 == 'RJ':
    print(produto*1.15)
if estado1 == 'MS':
    print(produto*1.08)
if estado1 != 'MS' and estado1 != 'RJ' and estado1 != 'SP' and estado1 != 'MG':
    print('Estado não disponível para venda')

