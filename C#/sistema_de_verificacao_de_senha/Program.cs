using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("🔐 Verificador de Força de Senha\n");

        Console.Write("Digite uma senha: ");
        string senha = Console.ReadLine();

        int forca = CalcularForca(senha);

        Console.WriteLine("\nForça da senha:");

        ExibirBarra(forca);
        ExibirNivel(forca);

        Console.ReadKey();
    }

    static int CalcularForca(string senha)
    {
        int pontos = 0;

        if (senha.Length >= 8) pontos++;
        if (senha.Any(char.IsUpper)) pontos++;
        if (senha.Any(char.IsLower)) pontos++;
        if (senha.Any(char.IsDigit)) pontos++;
        if (senha.Any(ch => "!@#$%&*".Contains(ch))) pontos++;

        return pontos;
    }

    static void ExibirBarra(int forca)
    {
        Console.Write("[");
        for (int i = 0; i < 5; i++)
        {
            if (i < forca)
                Console.Write("#");
            else
                Console.Write("-");
        }
        Console.WriteLine("]");
    }

    static void ExibirNivel(int forca)
    {
        if (forca <= 2)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Senha Fraca 🔴");
        }
        else if (forca <= 4)
        {
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("Senha Média 🟡");
        }
        else
        {
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("Senha Forte 🟢");
        }

        Console.ResetColor();
    }
}