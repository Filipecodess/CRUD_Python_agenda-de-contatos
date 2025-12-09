# controller.py
# Camada de controle: funções que orquestram validações mínimas e chamam o model (banco_dados.py).

import banco_dados as model

def inicializar_banco():
    # Abre conexão, retorna a conexão já pronta.

    conexao = model.get_connection()  # abre (ou cria) arquivo SQLite
    if conexao is None:
        raise RuntimeError("Não foi possível conectar ao banco de dados.")
    model.create_table(conexao)       # garante que tabela exista
    return conexao

# ---------------------------
# Operações CRUD expostas
# ---------------------------

def listar_contatos(conexao):
    #Retorna lista de contatos
    
    return model.retorna_contatos(conexao)

def obter_contato_por_id(conexao, id_contato):
    
    # Retorna um contato ou None.
    
    
    try:
        _id = int(id_contato)
    except (ValueError, TypeError):
        return None
    return model.contatos_id(conexao, _id)

def buscar_contatos_por_nome(conexao, termo):
   # Busca contatos cujo nome contenha 'termo' (case-insensitive).
    
    if termo is None:
        termo = ""
    termo = str(termo).strip()
    return model.busca_name_filtro(conexao, termo)

def criar_contato(conexao, nome, telefone, email=None, endereco=None, observacoes=None):
    # Valida campos mínimos e insere um novo contato.
    # Retorna id do novo contato ou None.
    # Regras simples:
    # - nome e telefone são obrigatórios (não vazios).
    # - email, endereco, observacoes podem ser None ou vazios.
    # validações básicas
    if not nome or not str(nome).strip():
        print("[controller] 'nome' é obrigatório.")
        return None
    if not telefone or not str(telefone).strip():
        print("[controller] 'telefone' é obrigatório.")
        return None

    nome = str(nome).strip()
    telefone = str(telefone).strip()
    email = str(email).strip() if email else None
    endereco = str(endereco).strip() if endereco else None
    observacoes = str(observacoes).strip() if observacoes else None

    return model.insert_contatos(conexao, nome, telefone, email, endereco, observacoes)

def atualizar_contato(conexao, id_contato, nome, telefone, email=None, endereco=None, observacoes=None):
    # Atualiza contato por id. Retorna True se atualizado, False caso contrário.
    # Valida id e campos mínimos.
    
    try:
        _id = int(id_contato)
    except (ValueError, TypeError):
        print("[controller] id inválido.")
        return False

    if not nome or not str(nome).strip():
        print("[controller] 'nome' é obrigatório.")
        return False
    if not telefone or not str(telefone).strip():
        print("[controller] 'telefone' é obrigatório.")
        return False

    nome = str(nome).strip()
    telefone = str(telefone).strip()
    email = str(email).strip() if email else None
    endereco = str(endereco).strip() if endereco else None
    observacoes = str(observacoes).strip() if observacoes else None

    return model.update_contatos(conexao, _id, nome, telefone, email, endereco, observacoes)

def deletar_contato(conexao, id_contato):

    # Deleta contato por id. Retorna True se deletado, False caso contrário.
    
    try:
        _id = int(id_contato)
    except (ValueError, TypeError):
        print("[controller] id inválido.")
        return False
    return model.delete_contatos(conexao, _id)
