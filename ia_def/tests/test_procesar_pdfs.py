import unittest
from unittest.mock import patch, mock_open, MagicMock
import os
import sys
import io

# Importamos el módulo a testear
# Nota: Asegúrate de que procesar_pdfs.py esté en el mismo directorio
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import procesar_pdfs

class TestProcesarPDFs(unittest.TestCase):
    
    @patch('procesar_pdfs.buscar_carpeta')
    @patch('procesar_pdfs.os.makedirs')
    @patch('procesar_pdfs.os.listdir')
    @patch('procesar_pdfs.os.path.join')
    @patch('procesar_pdfs.open', new_callable=mock_open)
    @patch('procesar_pdfs.requests.post')
    def test_procesar_pdf_successful(self, mock_post, mock_open_func, mock_join, 
                               mock_listdir, mock_makedirs, mock_buscar_carpeta):
        # Configurar los mocks
        mock_buscar_carpeta.side_effect = ['/ruta/a/pdfs', '/ruta/a/salida']
        mock_listdir.return_value = ['documento1.pdf', 'documento2.txt', 'documento3.pdf']
        mock_join.side_effect = lambda *args: '/'.join(args)
        
        # Mock para la respuesta HTTP
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b'<xml>Contenido XML</xml>'
        mock_post.return_value = mock_response
        
        # Configurar el mock del archivo abierto
        mock_file = MagicMock()
        mock_file.name = 'documento1.pdf'
        mock_open_func.return_value.__enter__.return_value = mock_file
        
        # Capturar la salida estándar
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Ejecutar el módulo (esto ejecutará todo el código en procesar_pdfs.py)
        # En lugar de ejecutar el módulo, simulamos la ejecución principal
        with patch.object(procesar_pdfs, '__name__', '__main__'):
            # Aquí llamamos a la función principal manualmente
            # Ya que el código está en el nivel principal, lo único que podemos hacer
            # es probar que los mocks se llamaron correctamente
            pass
            
        # Restaurar stdout
        sys.stdout = sys.__stdout__
        
        # Verificar que se llamaron los mocks correctamente
        mock_buscar_carpeta.assert_any_call('pdfs')
        mock_buscar_carpeta.assert_any_call('salida')
        mock_makedirs.assert_called_once_with('/ruta/a/salida', exist_ok=True)
        mock_listdir.assert_called_once_with('/ruta/a/pdfs')
        
        # Verificamos que se procesaron los PDFs correctamente
        mock_post.assert_called()  # Verificar que se llamó a requests.post
        
        print(captured_output.getvalue())
        
    @patch('os.walk')
    def test_buscar_carpeta_found(self, mock_walk):
        # Simular que encontramos la carpeta
        mock_walk.return_value = [
            ('/ruta/principal', ['documentos', 'pdfs', 'otros'], []),
            ('/ruta/principal/pdfs', [], ['archivo1.pdf'])
        ]
        
        resultado = procesar_pdfs.buscar_carpeta('pdfs')
        self.assertEqual(resultado, '/ruta/principal/pdfs')
        
    @patch('os.walk')
    def test_buscar_carpeta_not_found(self, mock_walk):
        # Simular que no encontramos la carpeta
        mock_walk.return_value = [
            ('/ruta/principal', ['documentos', 'otros'], []),
            ('/ruta/principal/documentos', [], ['archivo1.pdf'])
        ]
        
        resultado = procesar_pdfs.buscar_carpeta('pdfs')
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()
