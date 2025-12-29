"""
Versão introdutória do consumo de API em Python.
Objetivo: fazer uma chamada HTTP simples e exibir o resultado.
"""

import requests


def buscar_cep(cep: str) -> None:
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url, timeout=10)

    if resposta.status_code != 200:
        print("Erro ao buscar CEP.")
        return

    dados = resposta.json()
    print("CEP:", cep)
    print("Logradouro:", dados.get("logradouro"))
    print("Cidade:", dados.get("localidade"))


def main() -> None:
    cep = input("Digite um CEP (somente numeros): ").strip()
    buscar_cep(cep)


if __name__ == "__main__":
    main()


