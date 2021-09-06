# Escreva um algoritmo em Python em que o usuário escolhe se ele quer comprar maçãs, laranjas ou bananas.
# Deverá ser apresentado na tela um menu com a opção 1 para maçã, 2 para laranja e 3 para banana.
# Após escolhida a fruta, deve-se digitar quantas unidades se quer comprar.
# O algoritmo deve calcular o preço total a pagar do produto escolhido e mostrá-lo na tela.
# Considere que uma maçã custa R$ 2,30, uma laranja R$ 3,60 e uma banana 1,85.


# Main
maca = 2.30
laranja = 3.60
banana = 1.85

print('-' * 5, 'Opcoes de compra', '-' * 5)
print('''Selecione uma destas opcoes
1 - Maca
2 - Laranja
3 - Banana''')
option = int(input('Digite qual opcao deseja'))
qtd = int(input('Quantas deseja comprar:'))

if option == 1:
    maca *= qtd
    print(f'A opcao escolhida foi Maca\nA quantidade foi {qtd}\nO valor total = {maca}')

elif option == 2:
    laranja *= qtd
    print(f'A opcao escolhida foi Laranja\nA Quantidade foi {qtd}\nO valor total = {laranja}')
else:
    if option == 3:
        banana *= qtd
        print(f'A opcao escolhida foi Banana\nA quantidade foi {qtd}\nO valor total = {banana}')

