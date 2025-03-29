import pytest
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox
from unittest.mock import patch
from estoque_app import EstoqueApp, Produto  # Supondo que o código PyQt esteja em estoque_app.py

@pytest.fixture
def app(qtbot):
    """Fixture para criar e retornar a instância do app para os testes."""
    test_app = EstoqueApp()
    qtbot.addWidget(test_app)
    return test_app

def test_adicionar_produto(app, qtbot):
    """Testa a adição de um produto válido na lista e na tabela."""
    # Preencher os campos de entrada com dados válidos
    app.nome_input.setText("Produto A")
    app.quantidade_input.setText("10")
    app.preco_input.setText("20.50")
    app.categoria_input.setText("Categoria 1")
    
    # Clicar no botão "Adicionar Produto"
    qtbot.mouseClick(app.btn_add, Qt.MouseButton.LeftButton)
    
    # Verificar se a tabela foi atualizada corretamente
    assert app.tabela.rowCount() == 1
    assert app.tabela.item(0, 0).text() == "Produto A"
    assert app.tabela.item(0, 1).text() == "10"
    assert app.tabela.item(0, 2).text() == "R$ 20.50"
    assert app.tabela.item(0, 3).text() == "Categoria 1"

    # Verificar se o produto foi adicionado à lista
    assert len(app.produtos) == 1
    assert app.produtos[0].nome == "Produto A"
    assert app.produtos[0].quantidade == 10
    assert app.produtos[0].preco == 20.50
    assert app.produtos[0].categoria == "Categoria 1"

def test_adicionar_produto_invalido(app, qtbot):
    """Testa a inserção de produto com dados inválidos (quantidade e preço inválidos)."""
    # Preencher os campos com dados inválidos
    app.nome_input.setText("Produto B")
    app.quantidade_input.setText("abc")  # Quantidade inválida
    app.preco_input.setText("vinte")  # Preço não numérico
    app.categoria_input.setText("Categoria 2")
    
    # Simular clique no botão "Adicionar Produto"
    qtbot.mouseClick(app.btn_add, Qt.MouseButton.LeftButton)
    
    # Verificar que a tabela não foi atualizada
    assert app.tabela.rowCount() == 0
    
    # Verificar se o QMessageBox de erro foi chamado
    with patch.object(QMessageBox, 'warning') as mock_warning:
        qtbot.mouseClick(app.btn_add, Qt.MouseButton.LeftButton)
        mock_warning.assert_called_once()  # Verifica se a função de alerta foi chamada

def test_adicionar_produto_limpar_campos(app, qtbot):
    """Verifica se os campos de entrada são limpos após adicionar um produto."""
    # Preencher os campos com dados válidos
    app.nome_input.setText("Produto C")
    app.quantidade_input.setText("5")
    app.preco_input.setText("30.00")
    app.categoria_input.setText("Categoria 3")
    
    # Simular clique no botão "Adicionar Produto"
    qtbot.mouseClick(app.btn_add, Qt.MouseButton.LeftButton)
    
    # Verificar se os campos foram limpos após a adição do produto
    assert app.nome_input.text() == ""
    assert app.quantidade_input.text() == ""
    assert app.preco_input.text() == ""
    assert app.categoria_input.text() == ""

def test_remover_produto(app, qtbot):
    """Testa a remoção de um produto da tabela."""
    # Adicionar um produto primeiro
    app.nome_input.setText("Produto D")
    app.quantidade_input.setText("8")
    app.preco_input.setText("40.00")
    app.categoria_input.setText("Categoria 4")
    qtbot.mouseClick(app.btn_add, Qt.MouseButton.LeftButton)
    
    # Verificar que há 1 produto na tabela
    assert app.tabela.rowCount() == 1
    
    # Selecionar o produto na tabela
    app.tabela.selectRow(0)
    
    # Clicar no botão "Remover Produto"
    qtbot.mouseClick(app.btn_remover, Qt.MouseButton.LeftButton)
    
    # Verificar se o produto foi removido corretamente
    assert app.tabela.rowCount() == 0
    assert len(app.produtos) == 0

def test_remover_produto_sem_selecao(app, qtbot):
    """Testa a tentativa de remover um produto sem selecionar nada."""
    # Adicionar um produto primeiro
    app.nome_input.setText("Produto E")
    app.quantidade_input.setText("4")
    app.preco_input.setText("25.00")
    app.categoria_input.setText("Categoria 5")
    qtbot.mouseClick(app.btn_add, Qt.MouseButton.LeftButton)
    
    # Verificar que há 1 produto na tabela
    assert app.tabela.rowCount() == 1
    
    # Tentar remover sem selecionar uma linha
    qtbot.mouseClick(app.btn_remover, Qt.MouseButton.LeftButton)
    
    # Verificar que a tabela não foi alterada
    assert app.tabela.rowCount() == 1

def test_remover_produto_com_selecao(app, qtbot):
    """Testa a remoção de um produto quando selecionado na tabela."""
    # Adicionar um produto primeiro
    app.nome_input.setText("Produto F")
    app.quantidade_input.setText("7")
    app.preco_input.setText("50.00")
    app.categoria_input.setText("Categoria 6")
    qtbot.mouseClick(app.btn_add, Qt.MouseButton.LeftButton)
    
    # Verificar que há 1 produto na tabela
    assert app.tabela.rowCount() == 1
    
    # Selecionar o produto na tabela
    app.tabela.selectRow(0)
    
    # Clicar no botão "Remover Produto"
    qtbot.mouseClick(app.btn_remover, Qt.MouseButton.LeftButton)
    
    # Verificar que a tabela foi atualizada corretamente
    assert app.tabela.rowCount() == 0
