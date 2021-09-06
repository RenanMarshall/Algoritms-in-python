# Escreva uma função para validar uma string. Essa função recebe como parâmetro a string, o número mínimo e
# máximo de caracteres. Retorne verdadeiro se o tamanho da string estiver entre os valores de mínimo e máximo,
# e falso, caso contrário

def valid_str(str, min, max):
    size = len(str)
    if size < min or size > max:
        return False
    else:
        return True

texto = input('Digite um string (3-15 caracters):')
while valid_str(texto, 3, 15):
    texto = input('Digite uma string (3-15 caracters):')
print(texto)

