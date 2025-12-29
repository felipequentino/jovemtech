"""
Versão introdutória do sistema de estoque em Python.
Objetivo: mostrar a ideia de guardar produtos em uma lista e exibir no terminal.
"""

estoque = []


def adicionar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço: ").replace(",", "."))
    quantidade = int(input("Quantidade: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade,
    }

    estoque.append(produto)


def listar_produtos():
    if not estoque:
        print("Nenhum produto cadastrado.")
        return

    for produto in estoque:
        print(f"- {produto['nome']} | R$ {produto['preco']} | Qtd: {produto['quantidade']}")


def menu():
    while True:
        print("\n=== Estoque (versão simples) ===")
        print("1 - Adicionar produto")
        print("2 - Listar produtos")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()


