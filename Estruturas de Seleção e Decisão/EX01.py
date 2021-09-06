# desenvolva um algoritmo que solicite o seu ano de nascimento e o ano atual. Calcule a sua idade e apresente na tela.

# Para fins de simplificação, despreze o dia e o mês do ano. Após o cálculo, verifique se a idade é maior ou igual a 18 anos e apresente na tela uma mensagem informando que já é possível tirar a carteira de motorista caso seja de maior.


# Main
year = int(input('Digite seu ano de nascimento:'))
actual_year = int(input('Digite o ano atual:'))
res = actual_year - year
majority = 18 - res

if res >= 18:
    print(f'Parabéns você já tem {res}, e já pode tirar sua carteira de habilitação')
else:
    print(f'Falta {majority} anos, para que você possa tirar habilitação')