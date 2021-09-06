# Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja realizar: adição (+), subtração (-), multiplicação (*) ou divisão (/).
# Exiba na tela o resultado da operação desejada.


# Main
print('-' * 5, 'Calculadora', '-' * 5)
while True:
    op = input('''Selecione qual opcao deseja
0 - Encerrar    
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão:''')
    if op in '0':
        break
    try:
        n1 = int(input('Digite o primeiro numero:'))
        n2 = int(input('Digite o segundo numero:'))
        if op in '1':
            sum = n1 + n2
            print(f'O resultado da soma entre {n1} + {n2} = {sum}')
        elif op in '2':
            sum = n1 - n2
            print(f'O resultado da subtração entre {n1} - {n2} = {sum}')
        elif op in '3':
            sum = n1 * n2
            print(f'O resultado da multiplicação entre {n1} * {n2} = {sum}')
        elif op in '4':
            sum = n1 / n2
            print(f'O resultado da divisão entre {n1} / {n2} = {sum}')
    except:
        print('Verifique as informações inseridas, tente novamente!')
