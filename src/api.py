from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class ProdutoModel(BaseModel):
    nome: str
    quantidade: int
    preco: float
    categoria: str

estoque: List[ProdutoModel] = []

@app.get("/produtos", response_model=List[ProdutoModel])
def listar_produtos():
    return estoque

@app.post("/produtos", response_model=ProdutoModel)
def adicionar_produto(produto: ProdutoModel):
    estoque.append(produto)
    return produto

@app.delete("/produtos/{index}")
def remover_produto(index: int):
    if 0 <= index < len(estoque):
        removido = estoque.pop(index)
        return {"mensagem": "Produto removido", "produto": removido}
    return {"erro": "Índice inválido"}
