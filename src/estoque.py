from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QMessageBox
import sys
import requests 

class Produto:
    def __init__(self, nome, quantidade, preco, categoria):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.categoria = categoria

class LoginApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela de Login")
        self.setGeometry(100, 100, 300, 200)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.usuario_input = QLineEdit()
        self.usuario_input.setPlaceholderText("Usuário")
        layout.addWidget(self.usuario_input)

        self.senha_input = QLineEdit()
        self.senha_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.senha_input.setPlaceholderText("Senha")
        layout.addWidget(self.senha_input)

        self.btn_login = QPushButton("Entrar")
        self.btn_login.clicked.connect(self.verificar_login)
        layout.addWidget(self.btn_login)

        self.setLayout(layout)

    def verificar_login(self):
        usuario = self.usuario_input.text()
        senha = self.senha_input.text()

        if self.validar_login(usuario, senha):
            self.close()
            self.abre_estoque_app()
        else:
            QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos.")

    def validar_login(self, usuario, senha):
        if usuario == "usuario" and senha == "123":
            return True
        return False

    def abre_estoque_app(self):
        self.estoque_app = EstoqueApp()
        self.estoque_app.show()


class EstoqueApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Estoque")
        self.setGeometry(100, 100, 600, 400)
        self.produtos = []
        self.initUI()
        self.carregar_produtos()

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
            produto = {
                "nome": nome,
                "quantidade": int(quantidade),
                "preco": float(preco),
                "categoria": categoria
            }

            
            try:
                response = requests.post("http://localhost:8000/produtos", json=produto)
                if response.status_code == 200:
                    QMessageBox.information(self, "Sucesso", "Produto adicionado com sucesso!")
                    self.carregar_produtos()
                else:
                    QMessageBox.warning(self, "Erro", "Erro ao adicionar produto na API.")
            except Exception as e:
                QMessageBox.critical(self, "Erro de Conexão", str(e))

            self.limpar_campos()
        else:
            QMessageBox.warning(self, "Erro", "Por favor, preencha todos os campos corretamente.")

    def carregar_produtos(self):
        try:
            response = requests.get("http://localhost:8000/produtos")
            if response.status_code == 200:
                produtos = response.json()
                self.produtos = [Produto(p["nome"], p["quantidade"], p["preco"], p["categoria"]) for p in produtos]
                self.atualizar_tabela()
            else:
                QMessageBox.warning(self, "Erro", "Não foi possível carregar os produtos da API.")
        except Exception as e:
            QMessageBox.critical(self, "Erro de Conexão", str(e))

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
            produto = self.produtos[linha]
            try:
                response = requests.delete(f"http://localhost:8000/produtos/{linha}")
                if response.status_code == 200:
                    QMessageBox.information(self, "Sucesso", "Produto removido com sucesso!")
                    self.carregar_produtos()
                else:
                    QMessageBox.warning(self, "Erro", "Erro ao remover produto na API.")
            except Exception as e:
                QMessageBox.critical(self, "Erro de Conexão", str(e))
        else:
            QMessageBox.warning(self, "Erro", "Selecione um produto para remover.")

    def limpar_campos(self):
        self.nome_input.clear()
        self.quantidade_input.clear()
        self.preco_input.clear()
        self.categoria_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = LoginApp()
    janela.show()
    sys.exit(app.exec())
