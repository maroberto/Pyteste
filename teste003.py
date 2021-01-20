a = float(input('Qual é a sua altura? (ex. 1.75):  '))
p = float(input('Qual é o seu peso? '))

imc = p / (a * a)

'''
def peso_ideal():
    peso = []
    ideal = 24.9
    while (p / (a * a) > ideal):
        p = (p - 1)
        peso.append(p)
    print('Seu peso ideal é {:.0f}'.format(peso[-1]))
'''

if (imc < 16.9):
    print('O seu IMC é {:.2f}, você está muito abaixo do peso ideal!'.format(imc))
    # Verifica o peso ideal
    peso = []
    ideal = 24.9
    while (p / (a * a) < ideal):
        p = (p + 1)
        peso.append(p)
    print('Seu peso ideal é {:.0f}'.format(peso[-1]))
elif (imc < 18.6):
    print('O seu IMC é {:.2f}, você está abaixo do peso ideal!'.format(imc))
    # Verifica o peso ideal
    peso = []
    ideal = 24.9
    while (p / (a * a) < ideal):
        p = (p + 1)
        peso.append(p)
    print('Seu peso ideal é {:.0f}'.format(peso[-1]))
elif (imc < 24.9):
    print('O seu IMC é {:.2f}, você está no peso normal!'.format(imc))
elif (imc < 29.9):
    print('O seu imc é {:.2f}, você está acima do peso!'.format(imc))
    # Verifica o peso ideal
    peso = []
    ideal = 24.9
    while (p / (a * a) > ideal):
        p = (p - 1)
        peso.append(p)
    print('Seu peso ideal é {:.0f}'.format(peso[-1]))
elif (imc < 34.9):
    print('O seu IMC é {:.2f}, Você tem obesidade grau I!'.format(imc))
    # Verifica o peso ideal
    peso = []
    ideal = 24.9
    while (p / (a * a) > ideal):
        p = (p - 1)
        peso.append(p)
    print('Seu peso ideal é {:.0f}'.format(peso[-1]))
elif (imc < 40):
    print('O seu IMC é {:.2f}, você tem obesidade grau II!'.format(imc))
    # Verifica o peso ideal
    peso = []
    ideal = 24.9
    while (p / (a * a) > ideal):
        p = (p - 1)
        peso.append(p)
    print('Seu peso ideal é {:.0f}'.format(peso[-1]))
else:
    print('O seu IMC é {:.2f}, você tem obesidade grau III! '.format(imc))
    # Verifica o peso ideal
    peso = []
    ideal = 24.9
    while (p / (a * a) > ideal):
        p = (p - 1)
        peso.append(p)
    print('Seu peso ideal é {:.0f}'.format(peso[-1]))
