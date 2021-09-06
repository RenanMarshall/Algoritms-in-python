# Escreva um algoritmo que imprima na tela as horas no formato H:M:S dentro de um intervalo definido pelo usuário.
# O usuário deverá delimitar o intervalo de horas que deseja imprimir (por exemplo, das 7h até as 14h).
#
# Valide os dados de entrada para que seu programa só aceite valores válidos para hora (de 0 até 23h) e que a hora inicial digitada não seja maior que a final.
# Caso isso aconteça, o usuário deverá digitar o intervalo novamente.


h_inicial = int(input('Deseja iniciar em qual hora?'))
h_final = int(input('Deseja terminar em qual hora?'))
while h_inicial > h_final or h_inicial < 0 or h_inicial > 23 or h_final < 0 or h_final > 23:
    h_inicial = int(input('Deseja iniciar em qual hora ?'))
    h_final = int(input('Deseja terminar em qual hora?'))
for h in range(h_inicial, h_final + 1, 1):
    for m in range(0, 60, 1):
        for s in range(0, 60, 1):
            print(h, ':', m, ':', s, 'h')
