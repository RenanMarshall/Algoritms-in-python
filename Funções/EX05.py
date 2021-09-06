# Considerando a breve explicação sobre fatorial, escreva uma função que calcule o fatorial de um numero
# recebido como parâmetro e retorne o seu resultado. Faça uma validação dos dados por meio de outra função,
# permitindo que somente valores positivos sejam aceitos.

def valid_int(question, min, max):
    x = int(input(question))
    while ((x < min) or (x > max)):
        x = int(input(question))
        return x

def factorial(num):
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num+1, 1):
        fat *= i
    return fat

x = valid_int('Digite um valor para caucular a fatorial: ', 0, 99999)
print('{}!  {}.'.format(x, factorial(x)))