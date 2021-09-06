# uma empresa concedeu um bônus de 20% para todos seus funcionários com mais de 5 anos de empresa.
# Todos os outros que não se enquadram nessa categoria receberam uma bonificação de 10%, somente.
# Escreva um algoritmo que leia o salário do funcionário e seu tempo de empresa, e apresente a bonificação de cada funcionário na tela.


# Main
salary = float(input('Digite o valor do seu salário:'))
time = int(input('O seu tempo de empresa:'))

if time > 5:
    bonus = salary * 0.2
else:
    bonus = salary * 0.1
print(f'Você tem {time} anos de empresa\nSeu salário é {salary}\nSua bonificação é {bonus}\nSalário final = {bonus + salary}')