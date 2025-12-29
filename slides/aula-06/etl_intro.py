"""
Versão introdutória de ETL com Pandas.
Objetivo: ler um arquivo Excel e mostrar um resumo simples.
"""

import pandas as pd


def main() -> None:
    caminho = input("Caminho do arquivo Excel (ex: vendas.xlsx): ").strip()

    try:
        df = pd.read_excel(caminho)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return

    print("\nPrimeiras linhas:")
    print(df.head())

    if "produto" in df.columns:
        print("\nProdutos distintos:")
        print(df["produto"].unique())


if __name__ == "__main__":
    main()


