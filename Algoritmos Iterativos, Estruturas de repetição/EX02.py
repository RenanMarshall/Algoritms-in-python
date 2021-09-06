# Escreva um algoritmo que obtenha do usuário um valor inicial e um valor final.
# Para este intervalo especificado pelo usuário, calcule e mostre na tela
# a) A quantidade de números inteiros e positivos;
# b) A quantidade de números pares;
# c) A quantidade de números ímpares;
# d) A respectiva média de cada um dos itens anteriores.


begin = int(input('Digite um valor inicial:'))
end = int(input('Digite o valor final:'))
par = 0
impar = 0
count_int = 0
while begin < end:
    if begin % 2 == 0:
        par += 1
    else:
        impar += 1
    count_int += 1
    begin += 1
print(f'Quantidade de Nº pares:{par}')
print(f'Quantidade de Nº impares:{impar}\nQuantidade de Nº inteiros na contagem: {count_int}')



