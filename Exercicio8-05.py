nota_de_matematica = float(input('Digite sua nota de matemática: '))
nota_de_portugues = float(input('Digite sua nota de português: '))

if (nota_de_matematica)>=0 and (nota_de_matematica)<=10:
    print('')
else:
    print('')
    print('Nota de matemática inválida')

if (nota_de_portugues)>=0 and (nota_de_portugues)<=10:
   print('')
else:
    print('')
    print('Nota de português inválida')

if (nota_de_portugues)>=0 and (nota_de_portugues)<=10 and (nota_de_matematica)>=0 and (nota_de_matematica)<=10:
    media = (nota_de_matematica+nota_de_portugues)/2
    print('A sua média entre as notas foi: ', media)
