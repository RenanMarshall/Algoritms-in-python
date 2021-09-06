# Visite o site que contém o ranking das linguagens de programação mais amadas no ano de 2020: <https://insights.stackoverflow.com/survey/2020#technology-most-loved-dreaded-and-wanted-languages-loved>.
#
# Crie uma tupla com as 10 primeiras linguagens de programação mais amadas. Em seguida, faça:
#
#     Apresente na tela o ranking numerado com uma palavra em cada linha.
#     Apresente na tela somente o top 3 de linguagens.
#     Apresenta na tela as últimas 5 do ranking.
#     Em que posição está a linguagem Python? Mostre na tela.

languages = ('Rust', 'Typescript', 'Python', 'Kotlin', 'Go', 'Julia', 'Dart', 'C#', 'Swift', 'JavaScript')
print('Ranking das Linguagens mais amadas de 2020!')

index = 0
while index<len(languages):
    print(f'{index + 1} - {languages[index]}')
    index += 1

index = 0
print('\nAs top 3 linguagens mais amadas!')
while index < 3:
    print(f'{index + 1} - {languages[index]}')
    index += 1
print('\nAs ultimas 5 do ranking!\n',languages[-5:])

index = 0
while languages[index] != 'Python':
    index += 1
print(f'Python encontrado na posicao Nº{index + 1}')


# Exercicio exemplo do professor
# linguagens = ('Rust', 'Typescript', 'Python', 'Kotlin', 'Go', 'Julia', 'Dart', 'C#', 'Swift', 'JavaScript')
# print('Top 10 Linguagens de programacao mais amadas de 2020:\nSegundo stackoverflow!')
# for i in range(0, len(linguagens), 1):
#     print(i + 1, ' - ', linguagens[i])
#
# print('\nTop 3:', linguagens[:3])
# print('Ultimos 5:', linguagens[-5:])
# i = 0
# while linguagens[i] != 'Python':
#     i += 1
# print(f'Encontramos python na posicao {i + 1}')








