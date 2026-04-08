using System;
using System.Threading;

class Program
{
    static void Main()
    {
        Console.WriteLine("Detector de Mentira\n");

        while (true)
        {
            Console.Write("Faça uma pergunta (ou 'sair'): ");
            string pergunta = Console.ReadLine();

            if (pergunta.ToLower() == "sair")
                break;

            Analisar(pergunta);
            Resultado();
        }
    }

    static void Analisar(string pergunta)
    {
        Console.Write("Analisando");
        for (int i = 0; i < 3; i++)
        {
            Thread.Sleep(500);
            Console.Write(".");
        }
        Console.WriteLine();

        if (pergunta.Contains("eu"))
        {
            Console.WriteLine("Detectando resposta pessoal...");
            Thread.Sleep(500);
        }

        if (pergunta.Contains("sempre") || pergunta.Contains("nunca"))
        {
            Console.WriteLine("Detectando possível exagero...");
            Thread.Sleep(500);
        }
    }

    static void Resultado()
    {
        Random rand = new Random();
        int resultado = rand.Next(3);

        if (resultado == 0)
        {
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("VERDADE\n");
        }
        else if (resultado == 1)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("MENTIRA\n");
        }
        else
        {
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("INCONCLUSIVO\n");
        }

        Console.ResetColor();
    }
}