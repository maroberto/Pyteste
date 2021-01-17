from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'),sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha'),sg.Input(key='senha', password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
#janela
janela = sg.Window('Tela de Login', layout)

#Ler oa eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'marcos' and valores['senha'] == '123456':
            print('Bem-vindo a meu primeiro app!')
        else:
            print('Login ou Senha estão errados!')


