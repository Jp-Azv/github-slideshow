salario = float(input('Digite o seu slário: '))
servico = int(input('Digite o seu tempo de serviço: '))

while salario <= 500:
    if servico < 1:
        print('Seu novo salário é:', salario*1.25)
    if 1 < servico <= 3:
        print('Seu novo salário é: ', (salario*1.25)+100)
    if 3 < servico <= 6:
        print('Seu novo salário é: ', (salario*1.25)+200)
    if 6 < servico <= 10:
        print('Seu novo salário é: ', (salario*1.25)+300)
    if servico > 10:
        print('Seu novo salário é: ', (salario*1.25)+500)
    break

while 500 < salario <= 1000:
    if servico < 1:
        print('Seu novo salário é:', salario*1.2)
    if 1 < servico <= 3:
        print('Seu novo salário é: ', (salario*1.2)+100)
    if 3 < servico <= 6:
        print('Seu novo salário é: ', (salario*1.2)+200)
    if 6 < servico <= 10:
        print('Seu novo salário é: ', (salario*1.2)+300)
    if servico > 10:
        print('Seu novo salário é: ', (salario*1.2)+500)
    break

while 1000 < salario <= 1500:
    if servico < 1:
        print('Seu novo salário é:', salario*1.15)
    if 1 < servico <= 3:
        print('Seu novo salário é: ', (salario*1.15)+100)
    if 3 < servico <= 6:
        print('Seu novo salário é: ', (salario*1.15)+200)
    if 6 < servico <= 10:
        print('Seu novo salário é: ', (salario*1.15)+300)
    if servico > 10:
        print('Seu novo salário é: ', (salario*1.15)+500)
    break

while 1500 < salario <= 2000:
    if servico < 1:
        print('Seu novo salário é:', salario*1.2)
    if 1 < servico <= 3:
        print('Seu novo salário é: ', (salario*1.1)+100)
    if 3 < servico <= 6:
        print('Seu novo salário é: ', (salario*1.1)+200)
    if 6 < servico <= 10:
        print('Seu novo salário é: ', (salario*1.1)+300)
    if servico > 10:
        print('Seu novo salário é: ', (salario*1.1)+500)
    break

while salario > 2000:
    if servico < 1:
        print('Você não receberá reajuste')
    if 1 < servico <= 3:
        print('Seu novo salário é: ', salario+100)
    if 3 < servico <= 6:
        print('Seu novo salário é: ', salario+200)
    if 6 < servico <= 10:
        print('Seu novo salário é: ', salario+300)
    if servico > 10:
        print('Seu novo salário é: ', salario+500)
    break

