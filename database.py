import sqlite3

NOME_BANCO = "catalogo.db"


def conectar():
    conexao = sqlite3.connect(NOME_BANCO)
    conexao.row_factory = sqlite3.Row
    # no SQLite a checagem de chave estrangeira vem desligada por padrao
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao


def criar_tabelas():
    conexao = conectar()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS desenvolvedoras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            pais TEXT NOT NULL,
            ano_fundacao INTEGER NOT NULL
        )
    """)

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS jogos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            console TEXT NOT NULL,
            ano INTEGER NOT NULL,
            desenvolvedora_id INTEGER NOT NULL,
            FOREIGN KEY (desenvolvedora_id) REFERENCES desenvolvedoras (id)
        )
    """)

    conexao.commit()
    conexao.close()
