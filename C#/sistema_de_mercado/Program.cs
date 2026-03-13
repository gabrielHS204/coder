using System;
using System.Xml.Linq;
namespace Mercado
{
    public class Produto
    {
        public string Marca { get; set; }
        public string Nome { get; set; }
        public double Preco { get; set; }
        public int Quantidade { get; set; }
        public bool Estoque { get; set; }

        public Produto()
        {
            Marca = "";
            Nome = "";
            Preco = 0;
            Quantidade = 0;
            Estoque = false;
        }
        public class Adiciona
        {


        }


    }

}
class Program
{

    public static void Main(string[] args)
    {


        do
        {
            Console.Clear();
            Console.WriteLine("");
            Console.WriteLine("========== MENU DO SISTEMA ==========");
            Console.WriteLine("1 - Adicionar produto");
            Console.WriteLine("2 - Mostrar produtos");
            Console.WriteLine("3 - Remover produtos");
            Console.WriteLine("4 - Alterar preço");
            if (op)




            switch (op)
            {
                case 1:
                case 2:
                case 3:
            }
        } while (!9);

    }
}
