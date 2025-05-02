import subprocess
import time
import threading
import sys
from PyQt6.QtWidgets import QApplication
from estoque import LoginApp

def iniciar_api():
    subprocess.Popen(["uvicorn", "src.api:app", "--reload"])

def iniciar_interface():
    app = QApplication(sys.argv)
    janela = LoginApp()
    janela.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    # Iniciar a API em thread separada
    threading.Thread(target=iniciar_api, daemon=True).start()
    
    # Espera um pouco para a API iniciar (ajuste se necessário)
    time.sleep(2)

    # Iniciar a interface gráfica
    iniciar_interface()
