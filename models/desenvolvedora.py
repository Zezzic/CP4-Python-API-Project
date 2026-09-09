from pydantic import BaseModel


class Desenvolvedora(BaseModel):
    nome: str
    pais: str
    ano_fundacao: int
