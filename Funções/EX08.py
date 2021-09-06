# Suponha que você é um colecionador de jogos de videogames. Escreva um algoritmo que permite cadastrar esses
# jogos informando o nome e qual video ele pertence. Para isso, crie um menu de opções contendo cadastrar
# novo item, listar tudo que foi cadastro e sair.


def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criacao do arquivo.')
    else:
        print(f'Arquivo {nomeArquivo} foi criado com sucesso')


def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while x < min or x > max:
        x = int(input(pergunta))
    return x


def exibir_menu():
    print('Escolha uma opção\n1. Cadastrar um jogo\n2. Listar itens\n3. Sair')


def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        a.write(f'{nomeJogo};{nomeVideogame}\n')
    finally:
        a.close()


def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        print(a.read())
    finally:
        a.close()


# Main
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo Localizado!')
else:
    print('Arquivo inexistente..')
    criaArquivo(arquivo)

while True:
    exibir_menu()
    op = valida_int('Escolha a opcao desejada: ', 1, 3)

    if op == 1:
        print('Cadastro selecionado...\n')
        nomeJogo = input('Nome do jogo:')
        nomeVideogame = input('Nome do Videogame:')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
    elif op == 2:
        print('Listagem selecionada...\n')
        listarArquivo(arquivo)
    elif op == 3:
        print('Encerrando o programa...')
        break
