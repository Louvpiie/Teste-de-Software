# 📦 Sistema de Estoque com FastAPI + PyQt6

Este projeto é um sistema simples de **gerenciamento de estoque**, com uma API FastAPI e uma interface gráfica em PyQt6, desenvolvido como atividade avaliativa da matéria de **Teste de Software**.

## 🚀 Como Executar

1. **Clone o repositório**

```bash
clone https://github.com/louvpiie/gerenciamento-de-produtos-python.git
cd gerenciamento-tarefas-python
```

2. **Instale as dependências**

```bash
pip install -r requirements.txt
```

Ou, se preferir instalar manualmente:

```bash
pip install fastapi uvicorn pydantic requests PyQt6
```

3. **Execute o sistema**

```bash
python src/start.py
```

## 🔑 Login

- Usuário: ```usuario```
- Senha: ```123```


## 🧠 Tecnologias Utilizadas

- FastAPI
- PyQt6
- Uvicorn
- Requests
- Pydantic
- Threading

## 📁 Arquivos

| Arquivo      | Descrição                                        |
| ------------ | ------------------------------------------------ |
| `api.py`     | Define a API com os endpoints REST               |
| `estoque.py` | Interface gráfica com funcionalidades de estoque |
| `start.py`   | Inicializa a API e a interface gráfica juntas    |


## 💠 Comandos Úteis

Rodar só a API:

```bash
uvicorn src.api:app --reload
```

Rodar só a interface (a API precisa já estar rodando):

```bash
python src/estoque.py
```

## 👩🏻‍💻 Desenvolvedores

- Isabela Martins Bandeira
- João Felipe Alves de Albuquerque da Silva
- Louie Nery Silva
- Maria Eduarda Rita Marques Noleto
- Natália Ematné Kruchak 
