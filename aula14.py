c = 1
while c < 10:
    print(c, end=' - ')
    c += 1
print('Fim')

# flake Condicao de parada
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')
# sim ou não 
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Que continuar? [S/N] ')).upper()
print('Fim')
# par ou impar
n = 1 
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: # elimina o zero como par
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares!')