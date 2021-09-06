def ft_factorial(n):
    """
    Caucula a fatorial de um número
    :param n: Número a ser cauculado
    :return: Retorna a fatorial deste número
    """
    fact = 1
    if n == 0:
        return fact
    for i in range(1, n + 1):
        fact = fact * i
    return fact


def int_validation(question, min, max):
    x = int(input(question))
    while ((x < min) or (x > max)):
        x = int(input(question))
    return x


x = int_validation('Digite um valor para caucular a fatorial: ', 0, 9999)
print(f'{x}! = {ft_factorial(x)}')
