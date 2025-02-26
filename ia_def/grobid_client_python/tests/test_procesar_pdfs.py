# tests/test_procesar_pdfs.py
import pytest
import os
import shutil
from unittest import mock
from procesar_pdfs import buscar_carpeta, procesar_pdfs

@pytest.fixture
def mock_folders(tmpdir):
    pdf_dir = tmpdir.mkdir("pdfs")
    output_dir = tmpdir.mkdir("salida")
    return pdf_dir, output_dir

def test_buscar_carpeta(tmpdir):
    test_dir = tmpdir.mkdir("test_busqueda")
    found = buscar_carpeta("test_busqueda")
    assert found == str(test_dir)

def test_procesar_pdf_exitoso(mock_folders):
    pdf_dir, output_dir = mock_folders
    test_pdf = pdf_dir.join("test.pdf")
    test_pdf.write(b"dummy content")
    
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.content = b"<xml>test</xml>"
    
    with mock.patch("requests.post", return_value=mock_response) as mock_post:
        procesar_pdfs(str(pdf_dir), str(output_dir))
        
        assert mock_post.called
        assert os.path.exists(os.path.join(output_dir, "procesado_test.pdf.xml"))

def test_procesar_pdf_error(mock_folders, capsys):
    pdf_dir, output_dir = mock_folders
    test_pdf = pdf_dir.join("error.pdf")
    test_pdf.write(b"dummy content")
    
    mock_response = mock.Mock()
    mock_response.status_code = 500
    mock_response.text = "Server error"
    
    with mock.patch("requests.post", return_value=mock_response):
        procesar_pdfs(str(pdf_dir), str(output_dir))
        
        captured = capsys.readouterr()
        assert "Error al procesar el PDF: 500" in captured.out