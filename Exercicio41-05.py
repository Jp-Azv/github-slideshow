peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso/(altura**2)

if imc <= 18.5:
    print('Você está abaixo do peso')

if imc > 18.5 and imc <= 25.0:
    print('Você está saudável')

if imc > 25.0 and imc <= 30.0:
    print('Você está com excesso de peso')

if imc > 30.0 and imc <= 35.0:
    print('Você está com obesidade grau 1')

if imc > 35.0 and imc <= 40.0:
    print('Você está com obesidade grau 2')

if imc > 40:
    print('Você está com obesidade grau 3')