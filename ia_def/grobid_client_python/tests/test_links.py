# tests/test_links.py
import pytest
import os
from links import extraer_enlaces

@pytest.fixture
def sample_xml(tmpdir):
    xml = """<?xml version='1.0' encoding='UTF-8'?>
    <TEI xmlns="http://www.tei-c.org/ns/1.0">
        <ptr target="https://example.com"/>
        <ref target="http://test.org"/>
        <invalid target="ftp://old.org"/>
    </TEI>"""
    file = tmpdir.join("test.xml")
    file.write(xml)
    return str(file)

def test_extraer_enlaces(sample_xml):
    enlaces = extraer_enlaces(sample_xml)
    assert "https://example.com" in enlaces
    assert "http://test.org" in enlaces
    assert len(enlaces) == 2