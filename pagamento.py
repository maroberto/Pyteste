class Funcionario():
    def __init__(self, salario, opcao):
        self.salario = int(salario)
        self.opcao = int(opcao)

    def Descontos(self):
        add_noturno = (self.salario * 0.20)
        inss = (self.salario * 0.08)
        vt = (self.salario * 0.06)
        medico = 100
        odonto = 17
        total_descontos = (inss + vt + medico + odonto)
        if self.opcao == 1:
            pagamento = self.salario - total_descontos
            print(f'\nSeu Pagamento com descontos R$: {pagamento:.2f}')
        elif self.opcao == 2:
            pagamento = (self.salario - total_descontos) + add_noturno
            print(f'\nSeu Pagamento com descontos R$: {pagamento:.2f}')

        agua = float(input('\nDigite o valor da àgua: '))
        luz = float(input('Digite o valor da Luz: '))
        internet = float(input('Digite o valor da Internet: '))
        faculdade = float(input('Digite o valor da Faculdade: '))
        total_despesas = (agua + luz + internet + faculdade)
        saldo_receber = (pagamento - total_despesas)
        print(f'\nO Total de despesas é R$: {total_despesas:.2f}')
        print(f'\nSeu saldo de pagamento é R$: {saldo_receber:.2f}')
    
    def Beneficios(self):
        escala_seis = 26
        escala_doze = 15
        vr_dia = 21
        vt_dia = 18.48
        if self.opcao == 1:
            total_horas = escala_seis * 8
            valor_vr = escala_seis * vr_dia
            valor_vt = escala_seis * vt_dia
            print(
                f'\nSua escala é 6x1 com um total de {total_horas}h, receberá de VT: {valor_vt} e VR: {valor_vr:.2f}')
        elif self.opcao == 2:
            total_horas = escala_doze * 12
            valor_vr = escala_doze * vr_dia
            valor_vt = escala_doze * vt_dia
            print(
                f'\nSua escala é 12x36 com um total de {total_horas}h, receberá de VT: {valor_vt} e VR: {valor_vr:.2f}')


func1 = Funcionario(input('\nDigite o valor do seu salário R$: '), input(
    'Digite a sua escala [1= 6x1 | 2= 12X36]: '))
func1.Descontos()
func1.Beneficios()
