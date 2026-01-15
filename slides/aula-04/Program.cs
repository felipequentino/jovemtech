namespace Fazenda
{
    class Program
    {
        static void Main(string[] args) 
        {
           // Animal vaca = new Animal(0, 100, 100);

            Animal porco = new Animal();
            int Trigo = 10;
            int Cenoura = 20;
            double Soneca = 5.5;
            porco.Fome = 50;
            porco.Vida = 20;
            porco.Felicidade = 5;
            porco.Genero = true;
            porco.Sono = 50;

            porco.Comer(Cenoura);

        }
    }
}