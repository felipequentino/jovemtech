"""
Versão introdutória da modelagem de e-commerce em Python.
Objetivo: mostrar classes básicas e como criar instâncias.
"""


class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco


class Cliente:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email


def exemplo():
    produto = Produto("Teclado", 150.0)
    cliente = Cliente("Ana", "ana@example.com")

    print("Produto:", produto.nome, "- R$", produto.preco)
    print("Cliente:", cliente.nome, "-", cliente.email)


if __name__ == "__main__":
    exemplo()


