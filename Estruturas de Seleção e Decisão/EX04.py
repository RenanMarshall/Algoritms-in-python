# Escreva um algoritmo que lê um valor inteiro qualquer.
# Após, verifique se este valor está contido dentro dos seguintes intervalos: -100 <= x <= -1 e 1 <= x <= 100.
# Imprima na tela uma mensagem caso ele esteja em um dos intervalos.


x = int(input('Digite um valor inteiro qualquer:'))
if x >= 1 and x <= 100 or x >= -100 and x <= -1:
    print('Ele esta dentro do intervalo!')