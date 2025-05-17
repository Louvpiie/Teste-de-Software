# 📦 Testes E2E com Cypress – Sistema de Estoque

Este documento orienta a execução dos testes End-to-End (E2E) utilizando o Cypress, para verificar o correto funcionamento da **API de estoque** desenvolvida com FastAPI.

---

## 🚀 Pré-requisitos

- Node.js instalado (https://nodejs.org)
- Cypress instalado globalmente ou no projeto

Para instalar Cypress no projeto:

```bash
npm install cypress --save-dev
```

---

## 🧪 Como executar os testes E2E

### 1. Abra um terminal e rode só a API FastAPI

A API precisa estar rodando em `http://localhost:8000`.

```bash
uvicorn src.api:app --reload
```

---

### 2. Abra outro terminal e rode só a interface gráfica

```bash
python src/estoque.py
```

---

### 3. Em outro terminal (ou depois de iniciar API e GUI), execute os testes E2E da API com Cypress

```bash
npx cypress run --spec "cypress/e2e/api_estoque.cy.js"
```

Você verá uma saída como esta:

```
  Teste E2E da API de Estoque
    ✓ GET /produtos deve retornar lista inicial vazia ou existente
    ✓ POST /produtos deve adicionar um novo produto
    ✓ PUT /produtos/{index} deve atualizar o produto
    ✓ DELETE /produtos/{index} deve remover o produto
    ✓ GET /produtos após remoção deve refletir a lista atualizada
```

---

## ✅ Resultados Esperados

- 5 testes passando
- Nenhuma falha
- Lista de produtos sendo manipulada com sucesso via requisições HTTP

---

## 🧾 Observações

- Cypress é escrito em JavaScript, mas pode testar APIs Python sem problemas.
- Os testes verificam diretamente os endpoints, simulando o uso completo do sistema.

---

## 📌 Dica

Caso queira abrir o Cypress em modo interativo (com interface visual):

```bash
npx cypress open
```

Isso é útil para depuração ou acompanhamento visual dos testes.
