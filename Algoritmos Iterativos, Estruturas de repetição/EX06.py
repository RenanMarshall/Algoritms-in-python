# Escreva um algoritmo que repetidamente pergunte ao usuário qual sua idade e seu sexo (M ou F).
# Para cada resposta o programa deve responder imprimir a mensagem: “Boa noite, Senhor.
# Sua idade é <IDADE>” no caso gênero de masculino e “Boa noite, Senhora. Sua idade é <IDADE>” no caso de gênero feminino.
# O programa deve encerrar quando o usuário digitar uma idade negativa.

# Main
while True:
    idade = int(input('Qual a sua idade:'))
    if idade <= 0:
        break
    genero = input('''Digite qual o seu sexo
[M] - Masculino
[F] - Feminino''' )
    if genero.lower() in 'm':
        print(f'Boa noite, Senhor. Sua idade e {idade}')
    else:
        if genero.lower() in 'f':
            print(f'Boa noite, Senhora. Sua idade {idade}')
