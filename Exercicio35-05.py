dia = int(input('Digite o dia: '))
mes = int(input('Digite mês: '))
ano = int(input('Digite o ano:'))

while mes > 12 or mes < 1:
    print('Data inválida')
    break

while dia > 31 or dia < 1:
    print('Data inválida')
    break

while ano < 1:
    if mes == 2:
        if ano % 400 == 0:
            if dia >= 1 and dia <= 29:
                print('Ano: ', ano*(-1), 'a.C',  ' Mês: ', mes, 'Dia: ', dia)
                break
            else:
                print('Data inválida')
                break
        if ano % 4 == 0 and ano % 100 != 0:
            if dia >= 1 and dia <= 29:
                print('Ano: ', ano*(-1), 'a.C',  ' Mês: ', mes, 'Dia: ', dia)
                break
            else:
                print('Data inválida')
                break
        else:
            if dia <= 28:
                print('Ano: ', ano*(-1), 'a.C',  ' Mês: ', mes, 'Dia: ', dia)
                break
            else:
                print('Data inválida')
                break
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia > 30:
            print('Data inválida')
            break
        else:
            print('Ano: ', ano*(-1), 'a.C',  ' Mês: ', mes, 'Dia: ', dia)
            break
    else:
        print('Ano: ', ano*(-1), 'a.C',  ' Mês: ', mes, 'Dia: ', dia)
        break

while ano > 1:
    if mes == 2:
        if ano % 400 == 0:
            if dia >= 1 and dia <= 29:
                print('Ano:', ano,'d.C', ' Mês:', mes, 'Dia:', dia)
                break
            else:
                print('Data inválida')
                break
        if ano % 4 == 0 and ano % 100 != 0:
            if dia >= 1 and dia <= 29:
                print('Ano:', ano,'d.C', ' Mês:', mes, 'Dia:', dia)
                break
            else:
                print('Data inválida')
                break
        else:
            if dia <= 28:
                print('Ano:', ano,'d.C', ' Mês:', mes, 'Dia:', dia)
                break
            else:
                print('Data inválida')
                break
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia > 30:
            print('Data inválida')
            break
        else:
            print('Ano:', ano, 'd.C', ' Mês:', mes, 'Dia:', dia)
            break
    else:
         print('Ano:', ano, 'd.C', ' Mês:', mes, 'Dia:', dia)
         break

