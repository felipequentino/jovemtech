// Versão introdutória do sistema de estoque em C#.
// Objetivo: mostrar uma lista de produtos e um menu simples no console.

using System;
using System.Collections.Generic;

namespace Aula02EstoqueIntro
{
    public class Produto
    {
        public string Nome { get; set; } = string.Empty;
        public decimal Preco { get; set; }
        public int Quantidade { get; set; }
    }

    public class Program
    {
        private static readonly List<Produto> Estoque = new();

        public static void Main()
        {
            while (true)
            {
                Console.WriteLine("\n=== Estoque (versão simples) ===");
                Console.WriteLine("1 - Adicionar produto");
                Console.WriteLine("2 - Listar produtos");
                Console.WriteLine("0 - Sair");
                Console.Write("Opção: ");

                var opcao = Console.ReadLine();

                if (opcao == "1")
                {
                    AdicionarProduto();
                }
                else if (opcao == "2")
                {
                    ListarProdutos();
                }
                else if (opcao == "0")
                {
                    break;
                }
                else
                {
                    Console.WriteLine("Opção inválida.");
                }
            }
        }

        private static void AdicionarProduto()
        {
            Console.Write("Nome do produto: ");
            var nome = Console.ReadLine() ?? string.Empty;

            Console.Write("Preço: ");
            var precoStr = Console.ReadLine() ?? "0";
            decimal.TryParse(precoStr.Replace(',', '.'), out var preco);

            Console.Write("Quantidade: ");
            var qtdStr = Console.ReadLine() ?? "0";
            int.TryParse(qtdStr, out var quantidade);

            Estoque.Add(new Produto
            {
                Nome = nome,
                Preco = preco,
                Quantidade = quantidade
            });
        }

        private static void ListarProdutos()
        {
            if (Estoque.Count == 0)
            {
                Console.WriteLine("Nenhum produto cadastrado.");
                return;
            }

            foreach (var p in Estoque)
            {
                Console.WriteLine($"- {p.Nome} | R$ {p.Preco} | Qtd: {p.Quantidade}");
            }
        }
    }
}


