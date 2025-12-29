"""
Versão introdutória da prática de leitura de CSV em Python.
Objetivo: abrir um arquivo, ler as linhas e exibir no terminal.
"""


def ler_arquivo():
    nome_arquivo = input("Nome do arquivo CSV (ex: vendas.csv): ")

    try:
        with open(nome_arquivo, encoding="utf-8") as arquivo:
            for linha in arquivo:
                print(linha.strip())
    except FileNotFoundError:
        print("Arquivo não encontrado.")


def menu():
    while True:
        print("\n=== Leitor de CSV (simples) ===")
        print("1 - Ler arquivo")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            ler_arquivo()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()


