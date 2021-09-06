# Desenvolva um algoritmo que solicite ao usuário uma quantidade de dias, de horas, de minutos e de segundos. Calcule o total de segundos resultante e imprima na tela para o usuário.


# Main
dias = int(input('Digite a quantidade de dias:'))
horas = int(input('As horas:'))
min = int(input('Os minutos:'))
seg = int(input('Os segundos:'))

total = seg + (min * 60) + (horas * 60 * 60) + (dias * 24 * 60 * 60)
print(f'Total de segundos calculados = {total}')