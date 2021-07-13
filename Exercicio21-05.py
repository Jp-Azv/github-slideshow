print("Digite 'a' para soma")
print("Digite 'b' para subtração")
print("Digite 'c' para multiplicação")
print("Digite 'd' para divisão")

soma = 'a'
subtracao = 'b'
multiplicacao = 'c'
divisao = 'd'
operacao = input('Digite a operação desejada: ')

if operacao == str(soma):
    e = float(input('Digite seu primeiro número: '))
    f = float(input('Digite seu primeiro número: '))
    print(e+f)
if operacao == str(subtracao):
    g = float(input('Digite seu primeiro número: '))
    h = float(input('Digite seu segundo número: '))
    if g>h:
        print(g-h)
    else:
        print(h-g)
if operacao == str(multiplicacao):
    i = float(input('Digite seu primeiro número: '))
    j = float(input('Digite seu segundo número: '))
    print(i*j)
if operacao == str(divisao):
    k = float(input('Digite seu primeiro número: '))
    l = float(input('Digite seu segundo número: '))
    if l == 0:
        print('Não podemos dividir um número por zero')
    else:
        print(k/l)