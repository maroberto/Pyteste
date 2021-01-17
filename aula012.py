nome = str.title(input('Qual é se nome ? \n'))
if nome == 'Marcos':
    print('que no bonito!')
elif nome == 'Maria' or nome == 'João' or nome == 'Silva':
    print('Seu nome é bem comum no brasil,')  
else:
    print('Seu nome é bem normal,')    
print('tenha um bom dia {} !'.format(nome))   
