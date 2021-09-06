# Função para concatenação, recebe 2 parametros nome e sobrenome. Concatena somente o primeiro indice da string nome e sobrenome com a string contida em email
def concatenate(nome, sobrenome):
  email = '@algoritmos.com'
  return nome[0] + sobrenome[0] + email

# Main Program
x = input('Digite seu nome:')
y = input('Digite seu sobrenome:')
print(f'Sr/Sra {x} {y}, seu email é: {concatenate(x, y)}') # O exercício não pede um teste da função, mesmo assim eu deixei-lo aqui.

# Concatenação do meu nome e sobrenome os dois ultimos digitos do meu RU.
teste = x + y + '12'
print(f'{teste}')

