# Escreva um algoritmo que leia o nome, altura e peso de pessoas e armazene as informações em uma lista. O programa deve ir cadastrando um número indeterminado de dados e armazenar dentro da lista também o IMC da pessoa. Ao final do programa, imprima a lista completa e também:
#
#     O total de cadastros
#     A pessoa com o maior IMC
#     A pessoa com o menor IMC
#
# O cálculo do IMC deve ser realizado empregando uma função lambda e é dado como: IMC = peso / (altura²).
#
# Em que a massa é dada em quilograma e a altura em metros.

lista = []
imc = lambda peso, altura: peso / (altura * altura)

while True:
    nome = input('Digite seu nome:')
    altura = float(input('Digite sua altura'))
    peso = int(input('Digite seu peso'))
    x = imc(peso, altura)
    lista.append([nome, altura, peso, x])
    res = input('Desejar fazer mais um cadastro? [S/N]')
    if res in 'Nn':
        break
print('Cadastros: ', lista)
print('Total de cadastros:', len(lista))
maior = 0
menor = 99
for i in range(0, len(lista), 1):
    if lista[i][3] > maior:
        maior = lista[i][3]
    if lista[i][3] < menor:
        menor = lista[i][3]
print('Maior IMC:', maior)
print('Menor IMC:', menor)