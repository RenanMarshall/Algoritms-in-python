# O algoritmo mais simples de se buscar um dado em uma estrutura de dados é chamada de busca sequencial.
# A busca sequencial é uma varredura simples do primeiro ao último elemento da estrutura,
# verificando se o dado desejado se encontra presente.
#
# Escreva uma função em Python que receba como parâmetro uma lista e um dado.
# Verifique se o dado está presente na lista e retorne da função o seu índice,
# caso ele esteja presente, caso contrário, retorne -1.


def sequential_search(dlist, x):
    for i in range(len(dlist)):
        if dlist[i] == x:
            return i
    return -1



# Main
teste = [3,7,9,1,0,7,5,12]

dado = int(input('Digite um valor inteiro:'))
res = sequential_search(teste, dado)
if res >= 0:
    print(f'Posicao que {dado} foi encontrado: {res + 1}')
else:
    print('Dado nao localizado...')