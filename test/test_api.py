import sys
import os

# Adiciona o diretório '../src' ao início da lista de caminhos onde o Python procura por módulos para importar.
# Isso permite importar arquivos da pasta 'src', mesmo que o script de teste esteja em outra pasta.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from fastapi.testclient import TestClient
from api import app, estoque

client = TestClient(app)

def setup_function():
    """Limpa o estoque antes de cada teste"""
    estoque.clear()

def test_adicionar_produto():
    produto = {
        "nome": "Camiseta",
        "quantidade": 10,
        "preco": 49.99,
        "categoria": "Vestuário"
    }
    response = client.post("/produtos", json=produto)
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Camiseta"
    assert data["quantidade"] == 10
    assert data["preco"] == 49.99
    assert data["categoria"] == "Vestuário"
    assert len(estoque) == 1

def test_listar_produtos_vazio():
    response = client.get("/produtos")
    assert response.status_code == 200
    assert response.json() == []

def test_remover_produto_sucesso():
    produto = {
        "nome": "Livro",
        "quantidade": 5,
        "preco": 30.00,
        "categoria": "Educação"
    }
    client.post("/produtos", json=produto)
    response = client.delete("/produtos/0")
    assert response.status_code == 200
    data = response.json()
    assert data["mensagem"] == "Produto removido"
    assert data["produto"]["nome"] == "Livro"
    assert len(estoque) == 0

def test_remover_produto_indice_invalido():
    response = client.delete("/produtos/5")
    assert response.status_code == 200
    data = response.json()
    assert "erro" in data
    assert data["erro"] == "Índice inválido"
