n = 3
lista_falta = list(range(n))
listaProduto = ['banana', 'laranja', 'melao']
listaEstoque = [10, 20, 50]
listaPedido = [5, 30, 50]

text = ' '
for produto, estoque, pedido, falta in zip(listaProduto, listaEstoque, listaPedido, lista_falta):
    text += '\nO produto {} tem {} de estoque e um pedido de {}'.format(produto, estoque, pedido)
print(text)
print(lista_falta)
falta = estoque - pedido
if estoque < pedido:
    print(f'{produto}, falta {falta}')
    print(produto, estoque, pedido)
