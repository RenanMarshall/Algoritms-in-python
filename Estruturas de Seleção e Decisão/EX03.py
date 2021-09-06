# Um aluno, para passar de ano, precisa estar aprovado em todas as matérias que ele está cursando.
# Assuma que a média para aprovação é a partir de 7, e que o aluno cursa 3 matérias, somente.
# Escreva um algoritmo que leia a nota final do aluno em cada matéria, e informe na tela se ele passou de ano ou não.




# Main
notas = 0

for i in range(3):
    nota = float(input('Digite até 3 notas para o cauculo:'))
    notas += nota

notas /= 3
if nota >= 7:
    print(f'Parábens Você passou de ano!\nA média é 7.0\nA sua média foi de {notas}')
else:
    print('O aluno não atingiu a média necessária.')

