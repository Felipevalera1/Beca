n1 = int(input('Digite o operador 1: '))
n2 = int(input('Digite o operar 2: '))
opção = (input('''
Escolha sua opção:
1 Adição
2 Subtração
3 Multiplicação
4 Divisão
'''))

if opção == 1:
    resultado = n1 + n2
elif opção == 2:
    resultado = n1 - n2
elif opção == 3:
    resultado = n1 * n2
elif opção == 4:
    resultado = n1 / n2
else:
    print('''
    Opção invalida.
    Digite Novamente sua Opção.
    '''
    )    