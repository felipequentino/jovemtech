import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def main():
    arquivo = input("Digite o caminho do arquivo CSV de imoveis: ").strip()
    
    try:
        df = pd.read_csv(arquivo)
        print(f"\nDataset carregado: {len(df)} registros")
        print(df.head())
        
        X = df[["area", "quartos", "idade"]]
        y = df["preco"]
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        modelo = LinearRegression()
        modelo.fit(X_train, y_train)
        
        print("\nModelo treinado com sucesso!")
        print(f"Total de exemplos de treino: {len(X_train)}")
        print(f"Total de exemplos de teste: {len(X_test)}")
        
    except FileNotFoundError:
        print("Arquivo nao encontrado.")
    except KeyError as e:
        print(f"Coluna esperada nao encontrada: {e}")


if __name__ == "__main__":
    main()

