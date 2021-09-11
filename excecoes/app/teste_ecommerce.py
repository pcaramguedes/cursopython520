import unittest

from ecommerce import Produto, CarrinhoDeCompras

class TesteEcommerce(unittest.TestCase):

    def setUp(self): # preparacao do esperimento
        self.p1 = Produto('Camiseta', 9.90)
        self.p2 = Produto('Calça Jeans', 10.90)
        self.c1 = CarrinhoDeCompras()

    def adiciona_produtos_no_carrinho(self): # acao a ser validade 1
        self.c1.adicionaProduto(self.p1)
        self.c1.adicionaProduto(self.p2)

    def calcula_total_de_compras(self): # acao a ser validade 2
        self.total_de_compras = self.c1.calculaTotalDeCompras()

    def make_assertions(self): # checagem dos resultados
        self.assertEqual(2, len(self.c1.carrinho))
        self.assertEqual(self.p1.preco + self.p2.preco, self.total_de_compras)

    def teste_ecommerce(self): # Executa testes passo a passo
        self.adiciona_produtos_no_carrinho()
        self.calcula_total_de_compras()
        self.make_assertions()


