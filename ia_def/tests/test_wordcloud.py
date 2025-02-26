import unittest
from unittest.mock import patch, MagicMock
import os
import sys
import matplotlib
matplotlib.use('Agg')  # Usar backend no interactivo para pruebas

# Importamos el módulo a testear
# Nota: Asegúrate de que generate_wordcloud.py esté en el mismo directorio
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import generate_wordcloud

class TestWordCloud(unittest.TestCase):
    
    @patch('generate_wordcloud.buscar_carpeta')
    @patch('generate_wordcloud.glob.glob')
    @patch('generate_wordcloud.ET.parse')
    @patch('generate_wordcloud.WordCloud')
    @patch('generate_wordcloud.plt.figure')
    @patch('generate_wordcloud.plt.show')
    def test_generate_wordcloud(self, mock_show, mock_figure, mock_wordcloud, 
                              mock_parse, mock_glob, mock_buscar_carpeta):
        # Configurar los mocks
        mock_buscar_carpeta.return_value = '/ruta/a/salida'
        mock_glob.return_value = ['/ruta/a/salida/archivo1.xml', '/ruta/a/salida/archivo2.xml']
        
        # Crear mocks para los árboles XML y abstracts
        mock_root = MagicMock()
        mock_tree = MagicMock()
        mock_tree.getroot.return_value = mock_root
        mock_parse.return_value = mock_tree
        
        # Crear un mock para el elemento abstract
        mock_abstract = MagicMock()
        # Configurar itertext para devolver un texto de muestra
        mock_abstract.itertext.return_value = ['Este es un texto de muestra ', 'para la nube de palabras.']
        mock_root.find.return_value = mock_abstract
        
        # Configurar el mock de WordCloud
        mock_wordcloud_instance = MagicMock()
        mock_wordcloud.return_value = mock_wordcloud_instance
        mock_wordcloud_instance.generate.return_value = mock_wordcloud_instance
        
        # Configurar mock de figure de matplotlib
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_figure.return_value = mock_fig
        
        # Ejecutar la función principal
        with patch.object(generate_wordcloud, '__name__', '__main__'):
            pass
            
        # Verificar que se llamaron los mocks correctamente
        mock_buscar_carpeta.assert_called_with('salida')
        mock_glob.assert_called_with(os.path.join('/ruta/a/salida', '*.xml'))
        
        # Verificar que se llamó a ET.parse para cada archivo
        self.assertEqual(mock_parse.call_count, 2)
        
        # Verificar que se generó la nube de palabras para cada archivo
        self.assertEqual(mock_wordcloud_instance.generate.call_count, 2)
        
        # Verificar que se llamó a plt.show() para cada archivo
        self.assertEqual(mock_show.call_count, 2)
        
    def test_extract_abstract_text(self):
        # Crear un XML para probar la extracción de texto del abstract
        xml_string = '''
        <TEI xmlns="http://www.tei-c.org/ns/1.0">
          <teiHeader>
            <profileDesc>
              <abstract>
                <p>Este es un texto de abstract de prueba.</p>
                <p>Con múltiples párrafos para verificar la extracción.</p>
              </abstract>
            </profileDesc>
          </teiHeader>
        </TEI>
        '''
        
        # Crear un archivo temporal para la prueba
        import tempfile
        with tempfile.NamedTemporaryFile(suffix='.xml', delete=False) as temp_file:
            temp_file.write(xml_string.encode('utf-8'))
            temp_path = temp_file.name
        
        try:
            # Llamar a la función de extracción de abstract
            with patch('sys.stdout'):  # Silenciar salida estándar
                text = generate_wordcloud.extract_abstract_text(temp_path)
            
            # Verificar que el texto extraído contiene los textos de los párrafos
            self.assertIn('Este es un texto de abstract de prueba.', text)
            self.assertIn('Con múltiples párrafos para verificar la extracción.', text)
        finally:
            # Eliminar el archivo temporal
            os.unlink(temp_path)
    
    @patch('os.walk')
    def test_buscar_carpeta(self, mock_walk):
        # Simular que encontramos la carpeta
        mock_walk.return_value = [
            ('/ruta/principal', ['documentos', 'salida'], []),
            ('/ruta/principal/salida', [], ['archivo1.xml'])
        ]
        
        resultado = generate_wordcloud.buscar_carpeta('salida')
        self.assertEqual(resultado, '/ruta/principal/salida')

if __name__ == '__main__':
    unittest.main()
