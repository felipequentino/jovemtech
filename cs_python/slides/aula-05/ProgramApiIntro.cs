// Versão introdutória do consumo de API em C#.
// Objetivo: fazer uma chamada HTTP simples e exibir o resultado.

using System;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;

namespace Aula05ApiIntro
{
    public class Program
    {
        public static async Task Main()
        {
            Console.Write("Digite um CEP (somente numeros): ");
            var cep = Console.ReadLine() ?? string.Empty;

            await BuscarCepAsync(cep);
        }

        private static async Task BuscarCepAsync(string cep)
        {
            using var client = new HttpClient();
            var url = $"https://viacep.com.br/ws/{cep}/json/";

            var resposta = await client.GetAsync(url);
            if (!resposta.IsSuccessStatusCode)
            {
                Console.WriteLine("Erro ao buscar CEP.");
                return;
            }

            var json = await resposta.Content.ReadAsStringAsync();
            using var doc = JsonDocument.Parse(json);
            var raiz = doc.RootElement;

            Console.WriteLine("CEP: " + cep);
            Console.WriteLine("Logradouro: " + raiz.GetProperty("logradouro").GetString());
            Console.WriteLine("Cidade: " + raiz.GetProperty("localidade").GetString());
        }
    }
}


