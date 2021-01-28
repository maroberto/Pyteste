valor_carro = float(input('Digite o valor do veículo ex.: 48.500 R$:  '))
numero_parcelas = int(input('Digite o número de parcelas: '))

juros_mes = 0.013428083
juros_total = (numero_parcelas * juros_mes * valor_carro)

valor_total = (valor_carro + juros_total)
valor_parcelas = (valor_total / numero_parcelas)

print('O veículo de R$ {:.3f} em {} de {:.3f} sai no total por {:.3f}!'.format(valor_carro, numero_parcelas, valor_parcelas, valor_total))
print('O juros total pago nesse financiamento será de {:.3f}'.format(juros_total))
