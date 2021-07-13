ano = int(input('Digite o ano analisado: '))

if ano % 400 == 0:
    print('O ano de {} é bissexto'.format(ano))
elif ano % 4 == 0 and ano % 100>0:
    print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))