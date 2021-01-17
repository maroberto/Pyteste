n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro númeor inteiro: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, O produto é {} e a divisão é {:.2f}'.format(s, m, d), end=', ')
print('Divisão inteira {} e potência {}'.format(di, e))

