# Escreva um programa em Python que leia o nome de um aluno e três notas. Armazene em um dicionário o nome e a média aritmética da nota. Ainda, armazene no dicionário a situação do aluno:
#
#     Média >= 7, aprovado.
#     Média < 7 e >= 5, em exame.
#     Média < 5, reprovado.
#
# Apresente tudo na tela ao final do programa em um formato organizado.

aluno = {}
aluno['nome'] = input('Qual o nome do aluno?')
n1 = float(input('Qual a primeira nota?'))
n2 = float(input('Qual a segunda nota ?'))
n3 = float(input('Qual a terceira nota?'))
aluno['media'] = (n1 + n2 + n3) / 3
if aluno['media'] >= 7:
    aluno['status'] = 'A'
elif aluno['media'] >= 5 and aluno['media'] < 7:
    aluno['status'] = 'E'
else:
    aluno['status'] = 'R'

for i, j in aluno.items():
    print(f'{i} = {j}')
print(aluno)