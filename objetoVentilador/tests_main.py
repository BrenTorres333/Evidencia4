import unittest
from main import Ventilador 

class TestVentilador(unittest.TestCase):

    def setUp(self):
        self.ventilador = Ventilador() 

    def test_estado_inicial(self):
        self.assertEqual(str(self.ventilador), 'El ventilador se encuentra apagado')

    def test_encender(self):
        self.ventilador.encender()
        self.assertEqual(str(self.ventilador), 'El ventilador se encendio y esta funcionando a una velocidad baja')

    def test_cambiar_velocidad(self):
        self.ventilador.cambiar_velocidad(3)
        self.assertEqual(str(self.ventilador), 'Velocidad Alta')

    def test_consumo_energia(self):
        resultado_esperado = "Consumo de energia en velocidad 3 durante 2 horas: 150 W"
        self.assertEqual(self.ventilador.consumo_energia(3, 2), resultado_esperado)

if __name__ == '__main__':
    unittest.main()
