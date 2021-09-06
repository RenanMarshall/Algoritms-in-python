# Escreva um algoritmo que calcule a média dos números pares de 1 até 100 (1 e 100 inclusos). Implemente o laço usando for.

# Main
soma = 0
qtd = 0
for i in range(1, 101):
    if i % 2 == 0:
        qtd += 1
        soma += i
media = soma / qtd
print(f'A media de pares de 0 ate 100 = {media}')