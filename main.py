# main.py
# Interface de linha de comando simples para interagir com o controller e banco SQLite.

import controller

def formatar_contato(row):
    # Recebe sqlite3.Row (que funciona como dict) e retorna string formatada.
    
    if row is None:
        return "Contato não encontrado."
    # Acessa colunas pelo nome (row['nome'], etc.)
    return (
        f"ID: {row['id_contatos']}\n"
        f"Nome: {row['nome']}\n"
        f"Telefone: {row['telefone']}\n"
        f"Email: {row['email'] or '-'}\n"
        f"Endereço: {row['endereco'] or '-'}\n"
        f"Observações: {row['observacoes'] or '-'}"
    )

def listar_todos(conexao):
    rows = controller.listar_contatos(conexao)
    if not rows:
        print("Nenhum contato cadastrado.")
        return
    for row in rows:
        print("-" * 40)
        print(formatar_contato(row))
    print("-" * 40)
    print(f"Total: {len(rows)} contato(s).")

def criar_novo(conexao):
    print("=== Criar novo contato ===")
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("Email (opcional): ").strip() or None
    endereco = input("Endereço (opcional): ").strip() or None
    observacoes = input("Observações (opcional): ").strip() or None

    novo_id = controller.criar_contato(conexao, nome, telefone, email, endereco, observacoes)
    if novo_id:
        print(f"Contato criado com sucesso! ID = {novo_id}")
    else:
        print("Falha ao criar contato. Verifique os dados e tente novamente.")

def buscar_por_nome(conexao):
    termo = input("Digite parte do nome para buscar: ").strip()
    rows = controller.buscar_contatos_por_nome(conexao, termo)
    if not rows:
        print("Nenhum contato encontrado.")
        return
    for row in rows:
        print("-" * 40)
        print(formatar_contato(row))
    print("-" * 40)
    print(f"Total: {len(rows)} contato(s).")

def ver_por_id(conexao):
    _id = input("Informe o ID do contato: ").strip()
    contato = controller.obter_contato_por_id(conexao, _id)
    print(formatar_contato(contato))

def atualizar(conexao):
    print("=== Atualizar contato ===")
    _id = input("ID do contato que deseja atualizar: ").strip()
    contato = controller.obter_contato_por_id(conexao, _id)
    if not contato:
        print("Contato não encontrado.")
        return

    print("Deixe em branco para manter o valor atual.")
    nome = input(f"Nome [{contato['nome']}]: ").strip() or contato['nome']
    telefone = input(f"Telefone [{contato['telefone']}]: ").strip() or contato['telefone']
    email = input(f"Email [{contato['email'] or '-'}]: ").strip() or contato['email']
    endereco = input(f"Endereço [{contato['endereco'] or '-'}]: ").strip() or contato['endereco']
    observacoes = input(f"Observações [{contato['observacoes'] or '-'}]: ").strip() or contato['observacoes']

    ok = controller.atualizar_contato(conexao, _id, nome, telefone, email, endereco, observacoes)
    if ok:
        print("Contato atualizado com sucesso.")
    else:
        print("Falha ao atualizar contato.")

def deletar(conexao):
    _id = input("ID do contato que deseja deletar: ").strip()
    contato = controller.obter_contato_por_id(conexao, _id)
    if not contato:
        print("Contato não encontrado.")
        return

    confirma = input(f"Tem certeza que deseja deletar '{contato['nome']}'? (s/N): ").strip().lower()
    if confirma == "s":
        ok = controller.deletar_contato(conexao, _id)
        if ok:
            print("Contato deletado.")
        else:
            print("Falha ao deletar contato.")
    else:
        print("Operação cancelada.")

def mostrar_menu():
    print()
    print("=== Agenda de Contatos ===")
    print("1) Listar todos os contatos")
    print("2) Criar novo contato")
    print("3) Buscar por nome")
    print("4) Ver contato por ID")
    print("5) Atualizar contato")
    print("6) Deletar contato")
    print("0) Sair")
    print()

def main():
    conexao = None
    try:
        conexao = controller.inicializar_banco()
        while True:
            mostrar_menu()
            opc = input("Escolha uma opção: ").strip()
            if opc == "1":
                listar_todos(conexao)
            elif opc == "2":
                criar_novo(conexao)
            elif opc == "3":
                buscar_por_nome(conexao)
            elif opc == "4":
                ver_por_id(conexao)
            elif opc == "5":
                atualizar(conexao)
            elif opc == "6":
                deletar(conexao)
            elif opc == "0":
                print("Saindo. Até mais!")
                break
            else:
                print("Opção inválida. Tente novamente.")
    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        if conexao:
            controller.model = None  # apenas faz a limpeza
            controller_con = conexao
            try:
                conexao.close()
            except Exception:
                pass

if __name__ == "__main__":
    main()
