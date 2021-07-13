venda = float(input('Digite a sua venda mensal: '))

if venda >= 100000:
    comis = 700 + (venda*1.16)
    print('A sua comissão é de: ', comis)
if venda < 100000 and venda >= 80000:
    comis = 650 + (venda*1.14)
    print('A sua comissão é de: ', comis)
if venda < 80000 and venda >= 60000:
    comis = 600 + (venda*1.14)
    print('A sua comissão é de: ', comis)
if venda < 60000 and venda >= 40000:
    comis = 550 + (venda*1.14)
    print('A sua comissão é de: ', comis)
if venda < 40000 and venda >= 20000:
    comis = 500 + (venda*1.14)
    print('A sua comissão é de: ', comis)
else:
    comis = 400 + (venda*1.14)
    print('A sua comissão é de: ', comis)