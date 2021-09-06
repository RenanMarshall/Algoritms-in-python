# Escreva um algoritmo em Python que crie uma lista vazia e vá adicionando valores referentes às notas de um
# aluno nesta lista. Quando o usuário desejar parar de digitar notas (digitando um valor negativo, por exemplo)
# calcule a média das notas digitadas.

# Além disso, faça um tratamento para a exceção de divisão por zero (ZeroDivisionError).
# Essa exceção poderá ocorrer caso o usuário não digite nenhuma nota válida.

try:
    notas = []
    x = float(input('Digite as notas:'))
    while x >= 0:
        notas.append(x)
        x = float(input('Digite uma nota:'))
    soma = 0
    for i in notas:
        soma += i
    media = soma/len(notas)
    print(notas)
    print(f'Media das notas digitadas {media}')
except ValueError:
    print('Invalido tente novamente')
except ZeroDivisionError:
    print('Notas invalidas, tente novamente')