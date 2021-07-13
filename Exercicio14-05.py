nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
nota3 = float(input('Digite a sua terceira nota: '))


if nota1 >= 0 and nota1<=10 and nota2 >= 0 and nota2<=10 and nota3 >= 0 and nota3<=10:
    media= ((nota1*2)+(nota2*3)+(nota3*5))/10
    if media < 3:
        print('Você foi reprovado')
    elif media > 3 and media < 5:
        print('Você ficou de recuperação')
    else:
        print('Você foi aprovado')





