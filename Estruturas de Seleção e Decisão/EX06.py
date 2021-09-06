# Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário.
# Verifique se os valores formam um triângulo e classifique como:
# a) Equilátero (três lados iguais);
#
# b) Isósceles (dois lados iguais);
#
# c) Escaleno (três lados diferentes).


# Main
print('-' * 5, 'Verificacao de um triangulo', '-' * 5)
i = float(input('Digite o valor do primeiro lado:'))
j = float(input('Digite o valor do segundo lado'))
k = float(input('Digite o valor do terceiro lado'))
if i > 0 and j > 0 and k > 0:
    if (i + j < k) or (i + k < j) or (j + k < i):
        print('Nao e um triangulo')
    elif i == j and i == k:
        print('Equilatero')
    elif i == j or i == k or j == k:
        print('Isosceles')
    else:
        print('Escaleno')
