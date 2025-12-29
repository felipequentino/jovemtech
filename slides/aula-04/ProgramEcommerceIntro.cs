// Versão introdutória da modelagem de e-commerce em C#.
// Objetivo: mostrar classes básicas e como criar instâncias.

using System;

namespace Aula04EcommerceIntro
{
    public class Produto
    {
        public string Nome { get; set; } = string.Empty;
        public decimal Preco { get; set; }
    }

    public class Cliente
    {
        public string Nome { get; set; } = string.Empty;
        public string Email { get; set; } = string.Empty;
    }

    public class Program
    {
        public static void Main()
        {
            var produto = new Produto { Nome = "Teclado", Preco = 150.0m };
            var cliente = new Cliente { Nome = "Ana", Email = "ana@example.com" };

            Console.WriteLine($"Produto: {produto.Nome} - R$ {produto.Preco}");
            Console.WriteLine($"Cliente: {cliente.Nome} - {cliente.Email}");
        }
    }
}


