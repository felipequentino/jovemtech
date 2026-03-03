"""
Versão introdutória de ETL com Pandas.
Objetivo: ler um arquivo CSV e mostrar um resumo simples.
"""

import pandas as pd


def main() -> None:
    caminho = input("Caminho do arquivo CSV (ex: vendas.csv): ").strip()

    try:
        df = pd.read_csv(caminho)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return

    print("\nPrimeiras linhas:")
    print(df.head())

    if "nome" in df.columns: # if "produto" existe no array ["nome", "produto", "preco_x", ...]
        print("\nNomes distintos:")
        print(df["nome"].unique())


if __name__ == "__main__":
    main()


