from fastapi import APIRouter, HTTPException

from models.jogo import Jogo
from services import jogo_service

router = APIRouter()


@router.get("/jogos")
def listar_jogos():
    return jogo_service.listar()


@router.get("/jogos/{id_jogo}")
def buscar_jogo(id_jogo: int):
    jogo = jogo_service.buscar_por_id(id_jogo)
    if jogo is None:
        raise HTTPException(status_code=404, detail="Jogo nao encontrado.")
    return jogo


@router.post("/jogos", status_code=201)
def criar_jogo(dados: Jogo):
    try:
        return jogo_service.criar(dados)
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))


@router.put("/jogos/{id_jogo}")
def atualizar_jogo(id_jogo: int, dados: Jogo):
    try:
        jogo = jogo_service.atualizar(id_jogo, dados)
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))

    if jogo is None:
        raise HTTPException(status_code=404, detail="Jogo nao encontrado.")
    return jogo


@router.delete("/jogos/{id_jogo}")
def remover_jogo(id_jogo: int):
    if not jogo_service.remover(id_jogo):
        raise HTTPException(status_code=404, detail="Jogo nao encontrado.")
    return {"mensagem": "Jogo removido com sucesso."}
