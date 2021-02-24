'''
# Ranger normal
for i in range(0, 5):
    print('Oi')
print('Fim de soma')

print(10 * '--')

for i in range(5, 0, -1):
    print(i)
print('Fim de soma')

print(10 * '--')

for i in range(0, 10, 2):
    print(i)
print('Fim de soma')

print(10 * '--')

n = (int(input('Digite um número: ')))
for i in range(0, n + 1):
    print(i)
print('Fim')

print(10 * '--')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for i in range(i, f + 1, p):
    print(i)
print('Fim')
'''
print(10 * '--')

s = 0
for i in range(0, 4):
    n = int(input('Digite um número: '))
    s += n
print('A somatoria de todos os números é {}!'.format(s))
