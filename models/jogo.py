from pydantic import BaseModel


class Jogo(BaseModel):
    titulo: str
    console: str
    ano: int
    desenvolvedora_id: int
