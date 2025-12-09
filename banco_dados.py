# banco_dados.py
# Responsável por toda a lógica de acesso ao banco de dados (SQLite).
import sqlite3
from sqlite3 import Error

DB_FILE = "agenda_contatos.db"  # DB_FILE (para criar nome do arquivo do banco SQLite)

def get_connection():

    #Abre (ou cria) uma conexão com o banco SQLite e configura row_factory
    #para retornar linhas como dicionários (sqlite3.Row).

    try:
        conexao = sqlite3.connect(DB_FILE)  # cria arquivo se não existir
        conexao.row_factory = sqlite3.Row   # permite acessar colunas por nome
        return conexao
    except Error as e:
        print(f"[model] Erro ao conectar ao DB: {e}")
        return None

def create_table(conexao):
    # Cria a tabela contatos se ela não existir.
    # "IF NOT EXISTS - ajuda a não mostrar erro de criação de tabela (a mesma tabela pode ser criada várias vezes)"
    sql = """
    CREATE TABLE IF NOT EXISTS contatos ( 
        id_contatos INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL,
        email TEXT NULL,
        endereco TEXT,
        observacoes TEXT
    );
    """
    try:
        cur = conexao.cursor()
        cur.execute(sql)     # executa criação da tabela
        conexao.commit()        # salva as mudanças
    except Error as e:
        print(f"[model] Erro ao criar tabela: {e}")

def insert_contatos(conexao, nome, telefone, email, endereco, observacoes):
    # Insere um novo contato
    # Retorna o id do novo contato ou None em caso de erro.
    
    sql = """
    INSERT INTO contatos (nome, telefone, email, endereco, observacoes)
    VALUES (?, ?, ?, ?, ?)
    """
    try:
        cur = conexao.cursor()
        cur.execute(sql, (nome, telefone, email, endereco, observacoes))
        conexao.commit()                       # persiste a inserção
        return cur.lastrowid                # retorna id gerado
    except Error as e:
        print(f"[model] Erro ao adicionar contato: {e}")
        return None

def retorna_contatos(conexao):
    # Retorna uma lista de todas as linhas na tabela contatos.
    
    sql = "SELECT * FROM contatos ORDER BY nome;"
    try:
        cur = conexao.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(f"[model] Erro ao buscar contatos: {e}")
        return []

def contatos_id(conexao, contatos_id):
    #Busca um contato pelo id. Retorna uma sqlite3.Row ou None.

    sql = "SELECT * FROM contatos WHERE id_contatos = ?;"
    try:
        cur = conexao.cursor()
        cur.execute(sql, (contatos_id,))
        row = cur.fetchone()
        return row
    except Error as e:
        print(f"[model] Erro ao buscar por id: {e}")
        return None

def busca_name_filtro(conexao, parte_nome):
    # Busca contatos cujo nome contenha a string fornecida (case-insensitive).
    #Usa LIKE com curingas.

    sql = "SELECT * FROM contatos WHERE nome LIKE ? ORDER BY nome;"
    pattern = f"%{parte_nome}%"
    try:
        cur = conexao.cursor()
        cur.execute(sql, (pattern,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(f"[model] Erro ao buscar por nome: {e}")
        return []

def update_contatos(conexao, contatos_id, nome, telefone, email, endereco, observacoes):
    # Atualiza os campos de um contato identificado por id.
    # Retorna True se alguma linha foi alterada, False caso contrário.

    sql = """
    UPDATE contatos
    SET nome = ?, telefone = ?, email = ?, endereco = ?, observacoes = ?
    WHERE id_contatos = ?;
    """
    try:
        cur = conexao.cursor()
        cur.execute(sql, (nome, telefone, email, endereco, observacoes, contatos_id))
        conexao.commit()
        return cur.rowcount > 0
    except Error as e:
        print(f"[model] Erro ao atualizar contato: {e}")
        return False

def delete_contatos(conexao, contatos_id):
    #Deleta um contato pelo id. Retorna True se deletou, False caso contrário. 

    sql = "DELETE FROM contatos WHERE id_contatos = ?;"
    try:
        cur = conexao.cursor()
        cur.execute(sql, (contatos_id,))
        conexao.commit()
        return cur.rowcount > 0
    except Error as e:
        print(f"[model] Erro ao deletar contato: {e}")
        return False

def close_connection(conexao):
    # Fecha a conexão com o banco, se existir.
    
    try:
        if conexao:
            conexao.close()
    except Error as e:
        print(f"[model] Erro ao fechar conexão: {e}")

# Aqui temos a parte do banco e suas conexões, é visto o CRUD - CREATE, READ (ISERT/SELECT), UPDATE, DELETE 
