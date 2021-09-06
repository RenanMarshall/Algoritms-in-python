# Escreva uma rotina que recebe três valores como parâmetro e coloque-os em ordem crescente, ou seja, o menor ao maior. Imprima na tela os três valores.
# Dica: para realizar o print sem quebrar a linha, utilize um parâmetro opcional end='' da função print. Exemplo: print(x, end='').
# Utilize condicionais de múltipla escolha e composta.

def crescente(a, b ,c):
    if a <= b and a <= c:
        if b <= c:
            print(f'Ordem crescente {a}, {b}, {c}')
        else:
            print(f'Ordem crescente {a}, {c}, {b}')
    elif b <= a and b <= c:
        if a <= c:
            print(f'Ordem crescente {b}, {a}, {c}')
        else:
            print(f'ordem crescente {b}, {c}, {a}')
    else:
        if a <= b:
            print(f'ordem crecente {c}, {a}, {b}')
        else:
            print(f'ordem crescente {c}, {b}, {a}')


x = int(input('Digite um numero'))
y = int(input('Digite um numero'))
z = int(input('Digite um numero'))
crescente(x, y, z)