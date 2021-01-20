a = float(input('Qual é a sua altura? (ex. 1.75):  '))
p = float(input('Qual é o seu peso? '))

imc = p / (a * a)


peso = []
ideal = 24.9
while (p / (a * a) > ideal):
    p = (p - 1)
    peso.append(p)
print('Seu peso ideal é {:.0f}'.format(peso[-1]))
