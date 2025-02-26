import unittest
from unittest.mock import patch, MagicMock
import os
import sys
import matplotlib
matplotlib.use('Agg')  # Usar backend no interactivo para pruebas

# Importamos el módulo a testear
# Nota: Asegúrate de que graficar.py esté en el mismo directorio
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import graficar

class TestGraficar(unittest.TestCase):
    
    @patch('graficar.buscar_carpeta')
    @patch('graficar.os.listdir')
    @patch('graficar.os.path.join')
    @patch('graficar.ET.parse')
    @patch('graficar.plt.show')
    def test_graficar_figures(self, mock_show, mock_parse, mock_join, 
                            mock_listdir, mock_buscar_carpeta):
        # Configurar los mocks
        mock_buscar_carpeta.return_value = '/ruta/a/salida'
        mock_listdir.return_value = ['archivo1.xml', 'archivo2.txt', 'archivo3.xml']
        mock_join.side_effect = lambda *args: '/'.join(args)
        
        # Crear mocks para los árboles XML y sus raíces
        mock_root1 = MagicMock()
        mock_tree1 = MagicMock()
        mock_tree1.getroot.return_value = mock_root1
        
        mock_root2 = MagicMock()
        mock_tree2 = MagicMock()
        mock_tree2.getroot.return_value = mock_root2
        
        # Configurar parse para devolver diferentes árboles dependiendo del archivo
        def side_effect_parse(path):
            if 'archivo1.xml' in path:
                return mock_tree1
            else:
                return mock_tree2
                
        mock_parse.side_effect = side_effect_parse
        
        # Configurar findall para devolver figuras
        mock_fig1 = MagicMock()
        mock_fig2 = MagicMock()
        mock_fig3 = MagicMock()
        
        # El primer archivo tiene 2 figuras, el segundo tiene 1
        mock_root1.findall.return_value = [mock_fig1, mock_fig2]
        mock_root2.findall.return_value = [mock_fig3]
        
        # Ejecutar la función principal de graficar.py
        # Como es un script a nivel de módulo, simulamos su ejecución
        with patch.object(graficar, '__name__', '__main__'):
            pass
            
        # Verificar que se llamaron los mocks correctamente
        mock_buscar_carpeta.assert_called_with('salida')
        mock_listdir.assert_called_with('/ruta/a/salida')
        mock_parse.assert_any_call('/ruta/a/salida/archivo1.xml')
        mock_parse.assert_any_call('/ruta/a/salida/archivo3.xml')
        
        # Verificar que matplotlib.pyplot.show() se llamó
        mock_show.assert_called_once()
        
    @patch('os.walk')
    def test_buscar_carpeta_found(self, mock_walk):
        # Simular que encontramos la carpeta
        mock_walk.return_value = [
            ('/ruta/principal', ['documentos', 'salida', 'otros'], []),
            ('/ruta/principal/salida', [], ['archivo1.xml'])
        ]
        
        resultado = graficar.buscar_carpeta('salida')
        self.assertEqual(resultado, '/ruta/principal/salida')
        
    @patch('os.walk')
    def test_buscar_carpeta_not_found(self, mock_walk):
        # Simular que no encontramos la carpeta
        mock_walk.return_value = [
            ('/ruta/principal', ['documentos', 'otros'], []),
            ('/ruta/principal/documentos', [], ['archivo1.xml'])
        ]
        
        resultado = graficar.buscar_carpeta('salida')
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()
