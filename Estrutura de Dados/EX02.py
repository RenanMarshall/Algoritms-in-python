# Escreva uma função que contenha dois parâmetros. Essa função recebe como parâmetro uma string com uma mensagem
# a ser impressa na tela e outro parâmetro como sendo uma quantidade arbitrária de números empacotados.
# Dentro da função, encontre o maior entre todos os números recebidos e escreva na tela, dentro da função, a mensagem
# e o maior valor.

def maior(msg, *num):
    maior = 0
    for i in range(0, len(num), 1):
        if num[i] > maior:
            maior = num[i]
    print(msg, maior)

# main
maior('Maior: ', 9953,43,23,12,5,67,3,2)


