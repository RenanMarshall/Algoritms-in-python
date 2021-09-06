def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num // len(num)
    return 2021 - avg

cadastro = {'nome':[],'sexo':[],'ano':[]}
total = 0
i = 0

while True:
    terminar = input('Deseja realizar mais um cadastro ? [S/N]:')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite S para sim ou N para nao')
        continue

    nome = input('Qual e seu nome?')
    sexo = input('Qual e seu sexo? [M/F]:')
    ano = int(input('Qual seu ano de nascimento:'))
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)
    total += 1

print('Idade media das pessoas cadastradas', cal_average(cadastro['ano']))
print(cadastro, f'\nNumero de cadastros = {total}')