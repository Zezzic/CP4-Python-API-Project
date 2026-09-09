from fastapi import APIRouter, HTTPException

from models.desenvolvedora import Desenvolvedora
from services import desenvolvedora_service

router = APIRouter()


@router.get("/desenvolvedoras")
def listar_desenvolvedoras():
    return desenvolvedora_service.listar()


@router.get("/desenvolvedoras/{id_desenvolvedora}")
def buscar_desenvolvedora(id_desenvolvedora: int):
    desenvolvedora = desenvolvedora_service.buscar_por_id(id_desenvolvedora)
    if desenvolvedora is None:
        raise HTTPException(status_code=404, detail="Desenvolvedora nao encontrada.")
    return desenvolvedora


@router.post("/desenvolvedoras", status_code=201)
def criar_desenvolvedora(dados: Desenvolvedora):
    try:
        return desenvolvedora_service.criar(dados)
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))


@router.put("/desenvolvedoras/{id_desenvolvedora}")
def atualizar_desenvolvedora(id_desenvolvedora: int, dados: Desenvolvedora):
    try:
        desenvolvedora = desenvolvedora_service.atualizar(id_desenvolvedora, dados)
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))

    if desenvolvedora is None:
        raise HTTPException(status_code=404, detail="Desenvolvedora nao encontrada.")
    return desenvolvedora


@router.delete("/desenvolvedoras/{id_desenvolvedora}")
def remover_desenvolvedora(id_desenvolvedora: int):
    try:
        removeu = desenvolvedora_service.remover(id_desenvolvedora)
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))

    if not removeu:
        raise HTTPException(status_code=404, detail="Desenvolvedora nao encontrada.")
    return {"mensagem": "Desenvolvedora removida com sucesso."}
