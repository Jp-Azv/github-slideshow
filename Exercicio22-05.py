idade = int(input('Digite a sua idade: '))
servico = int(input('Digite quantos anos você serviu: '))

if servico >= 30 :
    print('Parabéns, você pode se aposentar')
elif idade >= 65 and servico >= 25:
    print('Parabéns, você pode se aposentar')
else:
    print('Sinto muito, você nao pode se aposentar')
