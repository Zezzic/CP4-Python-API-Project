from database import conectar


def validar(dados):
    if dados.nome.strip() == "":
        raise ValueError("O nome da desenvolvedora nao pode ser vazio.")
    if dados.pais.strip() == "":
        raise ValueError("O pais nao pode ser vazio.")
    if dados.ano_fundacao < 1800 or dados.ano_fundacao > 2100:
        raise ValueError("O ano de fundacao deve estar entre 1800 e 2100.")


def listar():
    conexao = conectar()
    linhas = conexao.execute(
        "SELECT * FROM desenvolvedoras ORDER BY nome"
    ).fetchall()
    conexao.close()
    return [dict(linha) for linha in linhas]


def buscar_por_id(id_desenvolvedora):
    conexao = conectar()
    linha = conexao.execute(
        "SELECT * FROM desenvolvedoras WHERE id = ?",
        (id_desenvolvedora,)
    ).fetchone()
    conexao.close()

    if linha is None:
        return None
    return dict(linha)


def criar(dados):
    validar(dados)

    conexao = conectar()
    cursor = conexao.execute(
        "INSERT INTO desenvolvedoras (nome, pais, ano_fundacao) VALUES (?, ?, ?)",
        (dados.nome.strip(), dados.pais.strip(), dados.ano_fundacao)
    )
    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()

    return buscar_por_id(novo_id)


def atualizar(id_desenvolvedora, dados):
    if buscar_por_id(id_desenvolvedora) is None:
        return None

    validar(dados)

    conexao = conectar()
    conexao.execute(
        "UPDATE desenvolvedoras SET nome = ?, pais = ?, ano_fundacao = ? WHERE id = ?",
        (dados.nome.strip(), dados.pais.strip(), dados.ano_fundacao, id_desenvolvedora)
    )
    conexao.commit()
    conexao.close()

    return buscar_por_id(id_desenvolvedora)


def remover(id_desenvolvedora):
    if buscar_por_id(id_desenvolvedora) is None:
        return False

    conexao = conectar()
    quantidade = conexao.execute(
        "SELECT COUNT(*) FROM jogos WHERE desenvolvedora_id = ?",
        (id_desenvolvedora,)
    ).fetchone()[0]

    if quantidade > 0:
        conexao.close()
        raise ValueError(
            "Nao e possivel remover: esta desenvolvedora possui jogos cadastrados."
        )

    conexao.execute(
        "DELETE FROM desenvolvedoras WHERE id = ?",
        (id_desenvolvedora,)
    )
    conexao.commit()
    conexao.close()
    return True
