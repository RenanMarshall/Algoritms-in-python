# Escreva um algoritmo que leia números inteiros via teclado. Somente valores positivos devem ser aceitos pelo programa
# O programa deve receber números até que o usuário digite zero. Ao final da execução, informe a média dos valores digitados.
# Realize a implementação com as instruções break e continue e trabalhe com operações lógicas Truthy e Falsey.

soma = 0
qtd_num = 0

while True:
    x = int(input('Digite um valor inteiro:'))
    if x < 0:
        continue
    if not x:
        break
    soma += x
    qtd_num += 1
media = soma / qtd_num
print(f'A media de valores digitados e {media}')
