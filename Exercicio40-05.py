custo_fabrica = float(input('Digite o custo de fábrica: '))

if custo_fabrica <= 12000:
    novo= custo_fabrica*1.05
    print('O preço é: ', novo)

if custo_fabrica > 12000 and custo_fabrica <=25000:
    novo = (custo_fabrica * 1.10) + (custo_fabrica*0.15)
    print('O preço é: ', novo)

if custo_fabrica > 25000:
    novo = (custo_fabrica*1.15)+(custo_fabrica*0.20)
    print('O preço é: ', novo)