using System.Security.Cryptography.X509Certificates;

public class Animal
{
    public Animal()
    {
    }
    public double Fome { get; set; }
    public double Felicidade {get ; set; } 
    public double Vida {get ; set;}

    public double Sono {get ; set;}
    public int Filhos {get ; set ;}
    public bool Genero { get; set;}
// Genero = 1 true Macho
// Genero = 0 false Femea
    public void Comer(double kgAlimento)
    {
        double steps = 3;
        double tempoTotal = steps * kgAlimento;
        double aux = tempoTotal;

        for (int i = 0; i < tempoTotal; i++)
        {
            Fome -= 1;
            Console.WriteLine($"O animal comeu, e falta {aux} segundos para ele terminar de comer");
            Console.WriteLine($"Fome restante: {Fome}");
            aux -= 1;
        }
        Console.WriteLine($"O animal comeu {kgAlimento} kilos e tá com {Fome} pontos de fome");

    }

    public void Dorme(double horasDeSono)
    {
        Felicidade += horasDeSono;
        Fome += horasDeSono * 0.85;
        Console.WriteLine($"O Animal dormiu {horasDeSono} horas de sono\nSeus novos status:\nFome = {Fome}\nFelicidade = {Felicidade}");
    }

    public void Reproduzir(int nFilhos)
    {
        if (Genero == false) // cenario da femea
        {
            double taxa = 0.85 / nFilhos;
            Sono *= taxa;
        }
        Filhos += nFilhos;
        Felicidade += 30;
        Console.WriteLine("O animal reproduziu");
    }


    public override string ToString()
    {
        return $"Esse animal tem {Fome} pontos de Fome\nEle também {Felicidade} pontos de felicidade\nE tambéeeem ele tem {Vida} pontos de vida";
    }

}

// Funcionários

public class Funcionario()
{
    public Funcionario()
    {
    }
    public double Salario { get; set;}
    public DateTime dataNascimento {get ;set;}
}

// Maquinário 
// Plantação
// Construção