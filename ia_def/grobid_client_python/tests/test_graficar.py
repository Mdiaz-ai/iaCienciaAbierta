# tests/test_graficar.py
import pytest
import os
import xml.etree.ElementTree as ET
from graficar import contar_figuras

@pytest.fixture
def sample_xml(tmpdir):
    xml = """<?xml version='1.0' encoding='UTF-8'?>
    <TEI xmlns="http://www.tei-c.org/ns/1.0">
        <figure></figure>
        <figure></figure>
    </TEI>"""
    file = tmpdir.join("test.xml")
    file.write(xml)
    return str(file)

def test_contar_figuras(sample_xml):
    count = contar_figuras(sample_xml)
    assert count == 2

def test_sin_figuras(tmpdir):
    xml = "<TEI xmlns='http://www.tei-c.org/ns/1.0'></TEI>"
    file = tmpdir.join("empty.xml")
    file.write(xml)
    
    count = contar_figuras(str(file))
    assert count == 0