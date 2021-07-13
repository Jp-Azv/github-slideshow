km_rodados = float(input('Digite a quantidade de km rodados: '))
litros_consumidos = float(input('Digite a quantidade de litros consumidos no percurso: '))

if km_rodados/litros_consumidos <8:
    print('Venda o carro.')
elif km_rodados/litros_consumidos >8 and km_rodados/litros_consumidos <14:
    print('Seu carro é econômico.')
else:
    print('Seu carro é super econômico.')
