def max_value(list):
    max_num = 0
    for i in list:
        if i > max_num:
            max_num = i
    return max_num

def sum_of_list(list):
    sum_of_list = 0
    count = 0
    for nota in notas:
        sum_of_list += nota
        count += 1
    return sum_of_list / count

# Main
notas = [9,7,7,10,3,9,6,6,2]

print('O numero de notas 7 encontradas = ', notas.count(7))
print('A maior nota e:', max_value(notas))
print('A media das notas:', sum_of_list(notas))
notas.sort()
print('Notas Ordenadas de forma crescente', notas)
