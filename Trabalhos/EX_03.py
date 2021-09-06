import random

Lista_Sorteio = []
print('Inicio do Programa')
print('-' * 10, 'Cadastro na lista do Sorteio!', '-' * 10)
while True:
    try:
        nome = input('Digite o nome da pessoa:')
        if nome and (not nome.isspace()): # Tratativa de erro, para não aceitar uma string só de whitespace e nem vazia.
            valor = float(input('Digite o valor doado:'))
            if valor <= 0:  # Tratativa de erro, para barrar valores negativos.
                continue
            tickets = valor // 10  # Com a divisão inteira do valor por 10, eu consigo saber quantos tickets a pessoa irá ter.
            while tickets != 0: # Loop que irá adicionar o nome da pessoa na lista, conforme a sua quantidade de tickets.
                Lista_Sorteio.append(nome)
                tickets -= 1
            terminar = input('''Deseja realizar mais um cadastro?
[1] - Para Sim 
[0] - Para Nao: ''')
            if terminar in '0':
                break
            if terminar not in '1':
                print('Digite 1 para continuar, ou 0 para encerrar o programa!')
                continue
    except:
        print('Dados incorretos, tente novamente...')
        continue

try:  # Usei mais um try só para lidar alguns erros que não consegui resolver.
    Lista_Sorteio.sort()
    print('-' * 8, 'Lista do Sorteio em ordem alfabética.', '-' * 8)
    for i in range(0, len(Lista_Sorteio), 1):
        print(Lista_Sorteio[i], end=', ')

    random.shuffle(Lista_Sorteio)
    print('\n\n', '-' * 8, 'Lista do Sorteio embaralhada.', '-' * 8)
    for i in range(0, len(Lista_Sorteio), 1):
        print(Lista_Sorteio[i], end=', ')

    sorteado = random.choice(Lista_Sorteio)
    print('\n', 'E o ganhador é:', sorteado)
except:
    print('Algum erro foi encontrado. Inicie o programa e tente novamente!')
