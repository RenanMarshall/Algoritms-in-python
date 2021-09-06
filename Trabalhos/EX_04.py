from operator import itemgetter

lista = []
dicionario = {}

print('Inicio do programa!')
print('-' * 8, 'Tabela de cadastro de produtos.', '-' * 8)
while True:
    try:
        dicionario['codigo'] = int(input('Digite o código do produto:'))
        if dicionario['codigo'] == 0:
            break
        dicionario['estoque'] = int(input('Digite a quantidade atual do estoque:'))
        dicionario['minimo'] = int(input('Digite a quantidade minima do estoque:'))
        lista.append(dicionario.copy())

        while True: # Utilizei mais um loop, porque precisava repetir este bloco de códigos sem que ele volta-se para o começo do primeiro loop.
            try:
                encerrar = input('''Deseja inserir mais dados?
[1] - Para Inserir 
[0] - Para Encerrar: ''')
                if encerrar in '0' or encerrar in '1':
                    break
                if encerrar not in '1':
                    print('Digite 1 para continuar, ou 0 para encerrar o programa!')
                    continue
            except:
                print('Dados invalidos, tente novamente...')
        if encerrar in '0': # Esta condição garante os dois loop se encerrem "juntos", porém só irá encerrar se input for 0, se ele for 1 voltará pro começo do 1 loop.
            break

    except ValueError:
        print('Dados incorretos, Somente valores númericos inteiros são aceito!')

lista_Ordenada = sorted(lista, key=itemgetter('codigo'))
print('\n', '-' * 5, 'Lista Ordenada de forma crescente', '-' * 5)
print(lista_Ordenada)
