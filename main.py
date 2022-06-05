#Davi Leal - 04092547
#Débora Gimenes -



import queue

prod_lista = []

q = queue.Queue()
cliente_registro = []
while not q.empty():
    for c in cliente_registro:
        q.put(c)

print('================ Materiais de contrução Takamassa Nomuro ================')
print("--------Escolha abaixo qual opção você deseja acessar: ")
opcao = 0
while opcao != 5:
    print('''    [1] LISTAR PRODUTOS NO ESTOQUE
    [2] INSERIR PRODUTO NO ESTOQUE
    [3] REMOVER DO ESTOQUE
    [4] REGISTRAR CLIENTE E COMPRA
    [5] FECHAR PROGRAMA''')
    print("===========================================")
    opcao = int(input('Digite aqui a sua opção: '))
    if opcao == 1:
        print('LISTAR')
        print(prod_lista)

    elif opcao == 2:
     print('INSERIR')
     codigo = input('Digite o código do produto: ')
     nome = input('Digite o nome do produto: ')
     preco = float(input('Digite o preço do produto: '))
     quantidade1 = int(input('Digite a quantidade: '))
     lista = {codigo: [nome, preco, quantidade1]}
     prod_lista.append(lista)
     print("========== Seu item foi INSERIDO ==========")

    elif opcao == 3:
         print('REMOVER')
         cdpd = input('Digite o código do produto: ')
         if (codigo == cdpd):
            print('Item removido')
            prod_lista.pop(codigo == cdpd)



    elif opcao == 4:
        print('REGISTRAR')
        cliente = input('Digite o nome do cliente: ')
        item = input('Digite o código do produto escolhido: ')
        quantidade = int((input('Digite a quantidade: ')))
        registro = {cliente: [item, quantidade]}
        cliente_registro.append(registro)
        print("========= O cliente foi REGISTRADO =========")
        if (codigo == item):
            lista[quantidade1] = [quantidade1 - quantidade]

        if (quantidade > quantidade1):
            print("A quantidade desejada não será possível devido a falta do produto no estoque")
        elif (item != codigo) :
            print('''Não há esse produto em estoque no momento, desejaria outra coisa?''')


    if opcao == 5:
        print('FINALIZANDO')

    else:
        print('Opção inválida! Tente novamente')







