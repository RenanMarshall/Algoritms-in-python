# Uma loja de departamentos está oferecendo diferentes formas de pagamento, conforme opções listadas a seguir.
# Faça um algoritmo que leia o valor total de uma compra e calcule o valor do pagamento final de acordo com a opção escolhida.
#
# Se a escolha for por pagamento parcelado, calcule também o valor de cada parcela. Ao final, apresente o valor total da compra e o valor das parcelas:
#
#     Pagamento à vista – conceder desconto de 5%;
#     Pagamento em 3x – o valor não sofre alterações;
#     Pagamento em 5x – acréscimo de 2%;
#     Pagamento em 10x – acréscimo 8%.


# Main

print('-' * 5, 'Cauculo de Compras', '-' * 5)
while True:
    valor_produto = float(input('Insira o valor do produto:'))
    opcao = input(''' Escolha a forma de pagamento desejada!
[0] - Sair
[1] - A Vista
[3] - Em 3x 
[5] - Em 5x
[10] - Em 10x''')
    if opcao in '0':
        break
    try:
        if opcao in '1':                              # Desconto de 5%
            valor_final = valor_produto
            valor_final -= valor_final * 0.05
            print(f'Produto comprado a vista total a pagar:{valor_final}.')
        elif opcao in '3':
            valor_final = valor_produto
            parcela = valor_final / 3
            print(f'Produto parcelado em 3x\tTotal a pagar:{valor_final}\tValor da parcela:{parcela}')
        elif opcao in '5':
            valor_final = valor_produto * 1.02
            parcela = valor_final / 5
            print(f'Produto parcelado em 5x\tTotal a pagar:{valor_final}\tValor da parcela:{parcela}')
        elif opcao in '10':
            valor_final = valor_produto * 1.08
            parcela = valor_final / 10
            print(f'Produto parcelado em 10x\tTotal a pagar:{valor_final}\tValor da parcela:{parcela}')
    except:
        print('teste')