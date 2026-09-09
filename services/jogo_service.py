from database import conectar
from services import desenvolvedora_service

# o JOIN traz o nome da desenvolvedora junto do jogo, para a tela nao mostrar so o id
SELECT_COM_DESENVOLVEDORA = """
    SELECT jogos.id,
           jogos.titulo,
           jogos.console,
           jogos.ano,
           jogos.desenvolvedora_id,
           desenvolvedoras.nome AS desenvolvedora_nome
    FROM jogos
    JOIN desenvolvedoras ON desenvolvedoras.id = jogos.desenvolvedora_id
"""


def validar(dados):
    if dados.titulo.strip() == "":
        raise ValueError("O titulo do jogo nao pode ser vazio.")
    if dados.console.strip() == "":
        raise ValueError("O console nao pode ser vazio.")
    if dados.ano < 1970 or dados.ano > 2100:
        raise ValueError("O ano do jogo deve estar entre 1970 e 2100.")
    if desenvolvedora_service.buscar_por_id(dados.desenvolvedora_id) is None:
        raise ValueError("Desenvolvedora nao encontrada.")


def listar():
    conexao = conectar()
    linhas = conexao.execute(
        SELECT_COM_DESENVOLVEDORA + " ORDER BY jogos.titulo"
    ).fetchall()
    conexao.close()
    return [dict(linha) for linha in linhas]


def buscar_por_id(id_jogo):
    conexao = conectar()
    linha = conexao.execute(
        SELECT_COM_DESENVOLVEDORA + " WHERE jogos.id = ?",
        (id_jogo,)
    ).fetchone()
    conexao.close()

    if linha is None:
        return None
    return dict(linha)


def criar(dados):
    validar(dados)

    conexao = conectar()
    cursor = conexao.execute(
        "INSERT INTO jogos (titulo, console, ano, desenvolvedora_id) VALUES (?, ?, ?, ?)",
        (dados.titulo.strip(), dados.console.strip(), dados.ano, dados.desenvolvedora_id)
    )
    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()

    return buscar_por_id(novo_id)


def atualizar(id_jogo, dados):
    if buscar_por_id(id_jogo) is None:
        return None

    validar(dados)

    conexao = conectar()
    conexao.execute(
        "UPDATE jogos SET titulo = ?, console = ?, ano = ?, desenvolvedora_id = ? WHERE id = ?",
        (dados.titulo.strip(), dados.console.strip(), dados.ano,
         dados.desenvolvedora_id, id_jogo)
    )
    conexao.commit()
    conexao.close()

    return buscar_por_id(id_jogo)


def remover(id_jogo):
    if buscar_por_id(id_jogo) is None:
        return False

    conexao = conectar()
    conexao.execute("DELETE FROM jogos WHERE id = ?", (id_jogo,))
    conexao.commit()
    conexao.close()
    return True
