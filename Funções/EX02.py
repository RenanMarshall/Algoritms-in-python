# Escreva uma rotina que crie um laço de repetição que faz uma contagem e imprime esta contagem na tela
# em uma só linha. Porém, como parâmetro, a função deve receber o valor inicial da contagem, o final,
# e o passo da iteração. Deixe os parâmetros inicial e de passo como opcionais.
# Você pode fazer o laço com for ou com while.

def contador(last, inicio=0, count=1):
    for i in range(inicio, last, count):
        print(f'{i}', end=' ')
    print('\n')

def contador2(last, inicio=0, count=1):
    while inicio < last:
        print(f'{inicio}', end=' ')
        inicio += count
    print('\n')

contador(20, 10, 2)
contador(12)
contador2(20, 10, 2)
contador2(12)