from datetime import datetime


class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []
        self.desconto = 0

    def adicionar_item(self, produto, quantidade):
        if quantidade > produto.estoque:
            print("Estoque insuficiente de", produto.nome)
            return

        self.itens.append((produto, quantidade))

    def aplicar_desconto(self, desconto):
        self.desconto = desconto

    def total(self):
        total = 0

        for produto, qtd in self.itens:
            total += produto.preco * qtd

        desconto = total * (self.desconto / 100)
        return total - desconto

    def mostrar(self):
        print("\nPEDIDO")
        print("Cliente:", self.cliente)

        for produto, qtd in self.itens:
            print(produto.nome, "-", qtd, "x", produto.preco)

        print("Total:", round(self.total(), 2))


class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar(self, produto):
        self.produtos[produto.nome] = produto

    def pegar(self, nome):
        return self.produtos[nome]

    def baixar(self, nome, qtd):
        produto = self.produtos[nome]
        produto.estoque -= qtd


        if produto.estoque == 0:
            del self.produtos[nome]

estoque = Estoque()

estoque.adicionar(Produto("Hamburguer", 18.9, 20))
estoque.adicionar(Produto("Batata", 9.5, 15))
estoque.adicionar(Produto("Refri", 6.0, 30))

pedido = Pedido("Ana")

pedido.adicionar_item(estoque.pegar("Hamburguer"), 2)
pedido.adicionar_item(estoque.pegar("Batata"), 1)
pedido.adicionar_item(estoque.pegar("Refri"), 2)

pedido.aplicar_desconto(10)

for produto, qtd in pedido.itens:
    estoque.baixar(produto.nome, qtd)

pedido.mostrar()

print("\nESTOQUE")
for nome in estoque.produtos:
    print(nome, estoque.produtos[nome].estoque)