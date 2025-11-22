import unittest
from Examen import MiClase

class TestMiClase(unittest.TestCase):
    def setUp(self):
        # Usando las variables REALES de tu clase
        self.objeto = MiClase(
            Valencia=5, 
            Tempo=120, 
            Tonos=12, 
            listaCanciones=["Canción 1", "Canción 2"], 
            listaBailabilidad=[0.8, 0.9]
        )

    # Pruebas para ObtieneMasBailable
    def test_ObtieneMasBailable_lista_normal(self):
        # Lista con números positivos
        resultado = self.objeto.ObtieneMasBailable([5, 2, 8, 1, 9])
        self.assertEqual(resultado, 9)

    def test_ObtieneMasBailable_lista_vacia(self):
        # Lista vacía
        resultado = self.objeto.ObtieneMasBailable([])
        self.assertIsNone(resultado)

    # Pruebas para VerificaListaCanciones
    def test_VerificaListaCanciones_sin_none(self):
        # Lista sin valores None
        resultado = self.objeto.VerificaListaCanciones(["song1", "song2", "song3"])
        self.assertTrue(resultado)

    def test_VerificaListaCanciones_con_none(self):
        # Lista con valores None
        resultado = self.objeto.VerificaListaCanciones(["song1", None, "song3"])
        self.assertFalse(resultado)
        
    #Prueba para Encuentra
    def test_Encuentra_elemento_ausente(self):
        # Elemento que NO está en la lista
        resultado = self.objeto.Encuentra([1, 2, 3, 4, 5], 6)
        self.assertFalse(resultado)
    
if __name__ == '__main__':
    unittest.main()

