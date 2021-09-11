from random import randint
import unittest
import calculadora

class TesteCalculadora(unittest.TestCase):
    def test_soma(self):
        n1= randint(0,999)
        n2= randint(0,999)
        soma = n1 + n2
        self.assertEqual(soma, calculadora.soma(n1,n2))

    def test_divisao_esperada(self):
        n1= randint(0,999)
        n2= randint(1,999)
        divisao = n1 / n2
        self.assertEqual(divisao, calculadora.divisao(n1,n2))

    def test_divisao_por_zero(self):
        n1 = randint(0,999)
        n2 = 0
        divzero = 'Nao dividirás por zero'
        self.assertEqual(divzero, calculadora.divisao(n1,n2))



#if __name__ == '__main__':
 #   unittest.main()
