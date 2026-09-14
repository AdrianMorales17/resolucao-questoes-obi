produtos = {
    "1": {"nome": "Hamburguer", "preco": 15.0},
    "2": {"nome": "Batata frita", "preco": 8.0},
    "3": {"nome": "Refrigerante", "preco": 5.0},
    "4": {"nome": "Sobremesa", "preco": 7.5}
}

pedido = []
total = 0


def mostrar_produtos():
    print("=== PRODUTOS ===")
    for codigo in produtos:
        print(codigo, "-", produtos[codigo]["nome"], "- R$", produtos[codigo]["preco"])


def adicionar_item():
    global total

    codigo = input("Digite o codigo do produto: ")
    if codigo in produtos:
        quantidade = int(input("Digite a quantidade: "))
        if quantidade > 0:
            item = produtos[codigo]
            valor = item["preco"] * quantidade
            pedido.append([item["nome"], quantidade, valor])
            total = total + valor
            print("Item adicionado.")
        else:
            print("Quantidade invalida.")
    else:
        print("Produto nao encontrado.")


def mostrar_pedido():
    print("\n=== SEU PEDIDO ===")
    if len(pedido) == 0:
        print("Pedido vazio")
    else:
        i = 0
        while i < len(pedido):
            print(pedido[i][0], "-", pedido[i][1], "unidades - R$", pedido[i][2])
            i = i + 1
        print("Total parcial: R$", total)


def aplicar_desconto():
    global total
    resposta = input("Tem cupom de desconto? (s/n): ")

    if resposta == "s":
        cupom = input("Digite o cupom: ")
        if cupom == "DESCONTO10":
            total = total * 0.9
            print("Desconto aplicado.")
        elif cupom == "DESCONTO20":
            total = total * 0.8
            print("Desconto aplicado.")
        else:
            print("Cupom invalido.")


def finalizar():
    print("\n=== FINALIZANDO ===")
    mostrar_pedido()
    aplicar_desconto()
    print("Total final: R$", round(total, 2))
    print("Obrigado pela compra!")


def menu():
    opcao = ""
    while opcao != "0":
        print("\n1 - Mostrar produtos")
        print("2 - Adicionar item")
        print("3 - Mostrar pedido")
        print("4 - Finalizar compra")
        print("0 - Sair")
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            mostrar_produtos()
        elif opcao == "2":
            adicionar_item()
        elif opcao == "3":
            mostrar_pedido()
        elif opcao == "4":
            finalizar()
            break
        elif opcao == "0":
            print("Saindo...")
        else:
            print("Opcao invalida.")


menu()