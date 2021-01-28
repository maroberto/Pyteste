from time import sleep


# imputs do valor do imovel, salario e anos para pagar
saldo_devedor = float(input('\033[34mQual é o valor do imovel R$: \033[m'))
salario = float(input('\033[34mQual é a sua renda mensal? R$: \033[m'))
anos = int(input('\033[34mEm quantos anos você vai pagar? \033[m'))


# calculo de juros
juros_base = 0.0799
juros_anos = (anos * juros_base)
meses = (anos * 12)
juros_mes = (juros_anos / meses)
base_salario = (salario / 100) * 30
base_salario2 = (salario / 100 * 40)

print('Processando sua silmuação...\n')
sleep(3)

valor_primeira_prestacao = (
    saldo_devedor * juros_mes) + (saldo_devedor / meses)
# mostra valor da prestação
print('O valor da prestação é de R$:\033[34m {:.2f}\033[m'.format(
    valor_primeira_prestacao))
# mostra o valor de 30% do sálario
print('Você poderia pagar uma prestação de até R$: \033[34m{}\033[m'.format(
    base_salario))


# condição para até 30% do sálario(pode financiar)
if valor_primeira_prestacao <= base_salario:
    print('\033[32mParabéns seu financiamento está pré aprovado em parcelas decrescentes.\nA primeira tem o valor de R$: {:.2f} e são {} parcelas\033[m\n'.format(
        valor_primeira_prestacao, meses))
# condição para até 40% do sálario(para poder financiar)
elif valor_primeira_prestacao <= base_salario2:
    print('\033[33mFalta pouco, tente encrementar sua renda incluindo algum parente, sua renda precisa ir de {:.2f} para {:.2f}\033[m\n'.format(
        salario, salario + (salario/100) * 35))
# condição de quem não pode financiar
else:
    print(
        '\033[31mInfelizmente não podemos aprovar seu financiamento, tente novamente daqui a 3 meses!\033[m\n')


# condição para imprimir tabela
quer_imprimir = str(
    input('Quer imprimir a tabela de amortização(sim ou não)? '))


if quer_imprimir.title() == ('Sim'):
    print('Gerando relatório....\n')
    sleep(3)
    # tabela de amortização
    amortizacao = saldo_devedor / meses
    print('\033[34mSaldo devedor\033[m, \033[35mJuros\033[m, \033[35mAmortização\033[m, \033[36mParcela Mês\033[m\n')
    for parcela in range(meses):
        juros_pago = (saldo_devedor * juros_mes)
        saldo_devedor = (saldo_devedor - amortizacao)
        prestacao = (amortizacao + juros_pago)
        print(
            parcela, '\033[34m{:.2f}\033[m / \033[35m{:.2f}\033[m / \033[35m{:.2f}\033[m / \033[36m{:.2f}\033[m'.format(saldo_devedor, juros_pago, amortizacao, prestacao))
else:
    print('Obrigado por fazer sua simulação!')
