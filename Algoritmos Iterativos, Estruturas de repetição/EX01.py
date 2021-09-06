# Escreva um algoritmo que leia dois valores e imprima na tela o resultado da multiplicação de ambos.
# Entretanto, para calcular a multiplicação, utilize somente operações de soma e subtração

n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero:'))
count = 1
multi = 0
while count <= n1:
    multi += n2
    count += 1
    print(f'Resultado da multiplicação {n1}x{n2} = {multi}')