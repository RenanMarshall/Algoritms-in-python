# Main Program
print('Inicio do programa!')
while True:
  # Uso do try para lidar com as excessões em geral.
  try:
    x = input('Deseja inserir dados?\t[S/N]')
    if x.lower() in 'n':
      break
    if x.lower() not in 's':
      print('Digite S para continuar. Ou N para encerrar o programa!')
      continue
    nome = input('Nome do aluno: ')
    nota = float(input('Nota final: '))
    # Sequencia de condicionais encadeadas, cada condição sera verificada em ordem. Se a primeira for falsa, a proxima é verificada, e assim por diante.
    if (nota >= 0 and nota <= 2.9):
      print(f'O aluno {nome} tirou nota %.1f e se enquadra no conceito E' % nota)
    elif (nota >= 3 and nota <= 4.9):
      print(f'O aluno {nome} tirou nota %.1f e se enquadra no conceito D' % nota)
    elif (nota >= 5 and nota <= 6.9):
      print(f'O aluno {nome} tirou nota %.1f e se enquadra no conceito C' % nota)
    elif (nota >= 7 and nota <= 8.9):
      print(f'O aluno {nome} tirou nota %.1f e se enquadra no conceito B' % nota)
    elif (nota >= 9 and nota <= 10):
      print(f'O aluno {nome} tirou nota %.1f e se enquadra no conceito A' % nota)
    else:
      print('A nota final deve ter valores de 0 até 10.')
  except:
    print('Dados incorretos! tente novamente...')
print('Programa Encerrando...')