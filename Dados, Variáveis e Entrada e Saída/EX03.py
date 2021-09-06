# Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele.
# Calcule e exiba o valor do desconto e o preço final do produto.



# Main

price = float(input('Digite o preço do produto:'))
discount = int(input('O percentual a ser aplicado:'))
x = price * (discount / 100)
res = price - discount
print(f'O preço do produto é {price}. Desconto de {discount}%')
print(f'Valor final é {res}')
