from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QMessageBox
import sys

class Produto:
    def __init__(self, nome, quantidade, preco, categoria):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.categoria = categoria

class EstoqueApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Estoque")
        self.setGeometry(100, 100, 600, 400)
        self.produtos = []
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(4)
        self.tabela.setHorizontalHeaderLabels(["Nome", "Quantidade", "Preço", "Categoria"])
        layout.addWidget(self.tabela)
        
        self.nome_input = QLineEdit()
        self.nome_input.setPlaceholderText("Nome do produto")
        layout.addWidget(self.nome_input)
        
        self.quantidade_input = QLineEdit()
        self.quantidade_input.setPlaceholderText("Quantidade")
        layout.addWidget(self.quantidade_input)
        
        self.preco_input = QLineEdit()
        self.preco_input.setPlaceholderText("Preço")
        layout.addWidget(self.preco_input)
        
        self.categoria_input = QLineEdit()
        self.categoria_input.setPlaceholderText("Categoria")
        layout.addWidget(self.categoria_input)
        
        self.btn_add = QPushButton("Adicionar Produto")
        self.btn_add.clicked.connect(self.adicionar_produto)
        layout.addWidget(self.btn_add)
        
        self.btn_remover = QPushButton("Remover Produto")
        self.btn_remover.clicked.connect(self.remover_produto)
        layout.addWidget(self.btn_remover)
        
        self.setLayout(layout)

    def adicionar_produto(self):
        nome = self.nome_input.text()
        quantidade = self.quantidade_input.text()
        preco = self.preco_input.text()
        categoria = self.categoria_input.text()
        
        if nome and quantidade.isdigit() and preco.replace('.', '', 1).isdigit() and categoria:
            produto = Produto(nome, int(quantidade), float(preco), categoria)
            self.produtos.append(produto)
            self.atualizar_tabela()
            self.limpar_campos()
        else:
            QMessageBox.warning(self, "Erro", "Por favor, preencha todos os campos corretamente.")
    
    def atualizar_tabela(self):
        self.tabela.setRowCount(len(self.produtos))
        for i, produto in enumerate(self.produtos):
            self.tabela.setItem(i, 0, QTableWidgetItem(produto.nome))
            self.tabela.setItem(i, 1, QTableWidgetItem(str(produto.quantidade)))
            self.tabela.setItem(i, 2, QTableWidgetItem(f"R$ {produto.preco:.2f}"))
            self.tabela.setItem(i, 3, QTableWidgetItem(produto.categoria))
    
    def remover_produto(self):
        linha = self.tabela.currentRow()
        if linha != -1:
            self.produtos.pop(linha)
            self.atualizar_tabela()
        else:
            QMessageBox.warning(self, "Erro", "Selecione um produto para remover.")
    
    def limpar_campos(self):
        self.nome_input.clear()
        self.quantidade_input.clear()
        self.preco_input.clear()
        self.categoria_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = EstoqueApp()
    janela.show()
    sys.exit(app.exec())
