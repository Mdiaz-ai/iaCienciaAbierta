# tests/test_generate_wordcloud.py
import pytest
import os
import xml.etree.ElementTree as ET
from generate_wordcloud import extract_abstract_text

@pytest.fixture
def sample_xml(tmpdir):
    xml = """<?xml version='1.0' encoding='UTF-8'?>
    <TEI xmlns="http://www.tei-c.org/ns/1.0">
        <profileDesc>
            <abstract><p>Este es un abstract de prueba con palabras relevantes.</p></abstract>
        </profileDesc>
    </TEI>"""
    file = tmpdir.join("test.xml")
    file.write(xml)
    return str(file)

def test_extract_abstract_text(sample_xml):
    text = extract_abstract_text(sample_xml)
    assert "abstract de prueba" in text

def test_empty_abstract(tmpdir, capsys):
    xml = "<TEI xmlns='http://www.tei-c.org/ns/1.0'></TEI>"
    file = tmpdir.join("empty.xml")
    file.write(xml)
    
    text = extract_abstract_text(str(file))
    assert text == ""
    assert "No se encontró el abstract" in capsys.readouterr().out