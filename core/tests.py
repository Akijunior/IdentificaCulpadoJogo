from django.test import TestCase

class InvestigacaoTestCase(TestCase):


    def test_caso_solucionado(self):
        """
        Soluciona o caso quando valores forem iguais
        """
        assassinoCerto = 2
        armaCerta = 2
        localCerto = 2

        self.assertEqual(assassinoCerto, assassinoCerto)
        self.assertEqual(armaCerta, armaCerta)
        self.assertEqual(localCerto, localCerto)


    def test_arma_errada(self):
        armaCerta = 2
        armaErrada = 1
        self.assertIsNot(armaErrada, armaCerta)

    def test_local_errado(self):
        localCerto = 2
        localErrado = 1
        self.assertIsNot(localCerto, localErrado)

    def test_suspeito_errado(self):
        assassinoCerto = 2
        assassinoErrado = 1
        self.assertIsNot(assassinoCerto, assassinoErrado)
