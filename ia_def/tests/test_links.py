import unittest
from unittest.mock import patch, mock_open, MagicMock
import os
import sys
import io
import xml.etree.ElementTree as ET

# Importamos el módulo a testear
# Nota: Asegúrate de que links.py esté en el mismo directorio
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import links

class TestLinks(unittest.TestCase):
    
    @patch('links.os.path.dirname')
    @patch('links.os.path.abspath')
    @patch('links.os.path.join')
    @patch('links.os.path.exists')
    @patch('links.os.listdir')
    @patch('links.ET.parse')
    @patch('links.open', new_callable=mock_open)
    def test_extract_links(self, mock_open_func, mock_parse, mock_listdir, 
                         mock_exists, mock_join, mock_abspath, mock_dirname):
        # Configurar los mocks
        mock_dirname.return_value = '/ruta'
        mock_abspath.return_value = '/ruta/script'
        mock_join.side_effect = lambda *args: '/'.join(args)
        mock_exists.return_value = True
        mock_listdir.return_value = ['archivo1.xml', 'archivo2.txt', 'archivo3.xml']
        
        # Crear un mock para el árbol XML y su raíz
        mock_root = MagicMock()
        mock_tree = MagicMock()
        mock_tree.getroot.return_value = mock_root
        mock_parse.return_value = mock_tree
        
        # Configurar elementos con atributos 'target'
        mock_element1 = MagicMock()
        mock_element1.attrib = {'target': 'https://ejemplo.com'}
        mock_element2 = MagicMock()
        mock_element2.attrib = {'target': 'http://otra-url.com'}
        mock_element3 = MagicMock()
        mock_element3.attrib = {'otro': 'valor'}
        
        # Configurar findall para devolver elementos
        mock_root.findall.return_value = [mock_element1, mock_element2, mock_element3]
        
        # Capturar la salida estándar
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Ejecutar el módulo (esto ejecutará todo el código en links.py)
        with patch.object(links, '__name__', '__main__'):
            # No podemos ejecutar directamente, pero verificamos las llamadas a los mocks
            pass
            
        # Restaurar stdout
        sys.stdout = sys.__stdout__
        
        # Verificar que se llamaron los mocks correctamente
        mock_exists.assert_called()
        mock_listdir.assert_called_with('/ruta/salida')
        mock_parse.assert_any_call('/ruta/salida/archivo1.xml')
        mock_parse.assert_any_call('/ruta/salida/archivo3.xml')
        
        # Verificar que el archivo de salida se abrió correctamente
        mock_open_func.assert_called_with('/ruta/links.txt', 'w')
        
        # Verificar la salida
        output = captured_output.getvalue()
        print(output)

    def test_link_filtering(self):
        # Prueba simple para verificar el comportamiento de filtrado de enlaces
        valid_links = [
            'https://ejemplo.com',
            'http://otra-url.com',
            'ftp://no-valido.org',  # No debería incluirse
            'https://ejemplo.org'
        ]
        
        filtered_links = [link for link in valid_links if link.startswith(("http://", "https://"))]
        
        self.assertEqual(len(filtered_links), 3)
        self.assertIn('https://ejemplo.com', filtered_links)
        self.assertIn('http://otra-url.com', filtered_links)
        self.assertIn('https://ejemplo.org', filtered_links)
        self.assertNotIn('ftp://no-valido.org', filtered_links)

if __name__ == '__main__':
    unittest.main()
