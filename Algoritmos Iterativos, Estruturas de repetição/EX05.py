# Escreva um algoritmo que calcule e exiba a tabuada de um número escolhido e digitado pelo usuário.
# A tabuada deve ser calculada até um determinado número n, também fornecido pelo usuário. Implemente o laço usando for.

# Main
tabuada = int(input('Digite o valor que deseja caucular a tabuada:'))
n = int(input('Digite ate qual numero deseja caucular:'))
for i in range(1, n + 1, 1):
    print(f'{tabuada}x{i}={tabuada * i}')
