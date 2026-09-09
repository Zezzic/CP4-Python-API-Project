from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from database import criar_tabelas
from controllers import desenvolvedora_controller, jogo_controller

app = FastAPI(title="Catalogo de Jogos de Cartucho")

criar_tabelas()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(desenvolvedora_controller.router)
app.include_router(jogo_controller.router)


@app.get("/")
def abrir_pagina():
    return FileResponse("templates/index.html")
