import random

def valid_int(question, min, max):
    x = int(input(question))
    while ((x < min) or (x > max)):
        x = int(input(question))
        return x

def vencedor(j1, j2):
    global empate, v1, v2
    if j1 == 1:       # Pedra
        if j2 == 1:
            empate += 1
        elif j2 == 2:
            v2 += 1
        elif j2 == 3:
            v1 += 1
    elif j1 == 2:     # Papel
        if j2 == 1:
            v1 += 1
        elif j2 == 2:
            empate += 1
        elif j2 == 3:
            v2 += 1
    elif j1 == 3:     # Tesoura
        if j2 == 1:
            v2 += 1
        elif j2 == 2:
            v1 += 1
        elif j2 == 3:
            empate += 1
    resultados = [v1, v2, empate]
    return resultados

# Main
print('JOKENPO')
print('''Escolha uma opcao para se jogar:

[1] Pedra
[2] Papel
[3] Tesoura
''')

resultados = []
jogadas = []
v1 = 0
v2 = 0
empate = 0

while True:
    j1 = valid_int('Escolha sua jogada: ', 0, 3)
    if not j1:
        break
    j2 = random.randint(1, 3)
    jogadas.append([j1, j2])
    resultados = vencedor(j1, j2)

print('Numero de vitorias do jogador 1:'.format(resultados))