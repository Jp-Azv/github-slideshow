salario = float(input('Digite seu salário mensal: '))
emprestimo = float(input('Digite quanto o valor do seu empréstimo: '))

if emprestimo <= (salario*(2/10)):
    print('Seu empréstimo de valor:', emprestimo, 'foi aprovado')
else:
    print('Seu empréstimo não foi aprovado')