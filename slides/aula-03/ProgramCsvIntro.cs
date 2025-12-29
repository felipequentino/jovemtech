// Versão introdutória da prática de leitura de CSV em C#.
// Objetivo: abrir um arquivo, ler as linhas e exibir no console.

using System;
using System.IO;

namespace Aula03CsvIntro
{
    public class Program
    {
        public static void Main()
        {
            while (true)
            {
                Console.WriteLine("\n=== Leitor de CSV (simples) ===");
                Console.WriteLine("1 - Ler arquivo");
                Console.WriteLine("0 - Sair");
                Console.Write("Opção: ");

                var opcao = Console.ReadLine();

                if (opcao == "1")
                {
                    LerArquivo();
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

        private static void LerArquivo()
        {
            Console.Write("Nome do arquivo CSV (ex: vendas.csv): ");
            var nomeArquivo = Console.ReadLine() ?? string.Empty;

            if (!File.Exists(nomeArquivo))
            {
                Console.WriteLine("Arquivo não encontrado.");
                return;
            }

            var linhas = File.ReadAllLines(nomeArquivo);

            foreach (var linha in linhas)
            {
                Console.WriteLine(linha);
            }
        }
    }
}


