# Crie um programa em Python para controle de estoque de produtos de um estabelecimento que vende produtos de hortifruti. Para o estoque, armazene tudo dentro de um dicionário contendo listas. A chave deverá ser o nome de cada produto e dentro de cada lista teremos o preço e a quantidade disponível no estoque. O estoque pode estar pré-cadastrado no sistema com quantos itens desejar.
#
# Simule uma compra. Peça ao usuário para digitar o nome do produto e a quantidade que deseja até que ele decida encerrar a compra. Ao final, apresente tudo na tela em um formato organizado, mostrando o total a ser pago por produto e o total final do pedido.
#
# Ainda, dê baixa no sistema descontado o que foi comprado do total. Imprima na tela o estoque restante.


loja = {'tomate':[100, 0.99],
            'cebola':[200, 1.99],
            'alface':[40, 1.00],
            'alho':[96, 3.25],
            'maca':[75, 4.20]}

pedido = []
while True:
    item_nome = input('Digite o nome do item que deseja comprar:')
    item_qtd = int(input('Digite a quantidade que deseja:'))
    pedido.append([item_nome, item_qtd])
    res = input('Deseja adicionar outro item? [S/N]')
    if res in 'Nn':
        break
total = 0
print('\nVendas:')
for item in pedido:
    produto = item[0]
    qtd = item[1]
    preco = loja[produto][1]
    valor_produto = preco * qtd
    print(f'{produto}: {qtd} x {preco} = {valor_produto}')
    loja[produto][0] -= qtd
    total += valor_produto
print(f'Custo total: {total}\n')
print('Estoque:')
for i, j in loja.items():
    print('Descricao', i)
    print('Quantidade', j[0])
    print(f'Preco: {j[1]}\n')
