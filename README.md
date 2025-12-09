Sistema de Agenda de Contatos (CRUD com Python + SQLite3)

Este projeto é uma agenda de contatos desenvolvida em Python, utilizando o banco de dados SQLite3 e uma arquitetura organizada em MVC sem POO — seguindo um padrão simples, direto e ideal para estudantes em formação.

O sistema permite Cadastrar, Listar, Buscar, Atualizar e Excluir contatos facilmente pelo terminal.

📌 Funcionalidades

➕ Adicionar um novo contato

📄 Listar todos os contatos

🔍 Buscar contato pelo nome

✏️ Atualizar os dados de um contato existente

🗑️ Excluir um contato pelo ID

💾 Banco de dados SQLite criado automaticamente

🔧 Lógica separada em arquivos (MVC simplificado sem POO)

🧱 Arquitetura do Projeto (MVC sem POO)
Camada	Arquivo	Função
Model	model.py	Acesso ao banco de dados, criação da tabela e funções CRUD
Controller	controller.py	Lida com a lógica de controle e fluxo do sistema
Main/App	main.py ou app.py	Ponto de entrada do sistema, interface via terminal

❗ Não foi utilizada a camada view.py a pedido do usuário.

⚙️ Requisitos para executar o sistema

Antes de rodar o sistema, verifique se você possui:

Python 3.8+

Biblioteca padrão sqlite3 (já vem com o Python)

Sistema operacional:

Windows, Linux ou macOS

📦 Como instalar e executar o projeto
1️⃣ Clone o repositório
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git

2️⃣ Acesse a pasta do projeto
cd NOME_DO_REPOSITORIO

3️⃣ Execute o sistema
python main.py


ou

python app.py


O arquivo principal depende do nome escolhido no seu projeto.

🗂️ Estrutura de Diretórios
📁 agenda_contatos/
│── model.py
│── controller.py
│── main.py   (ou app.py)
│── agenda_contatos.db   (criado automaticamente)
│── README.md

🗃️ Banco de Dados

Utiliza SQLite3, que cria automaticamente o arquivo agenda_contatos.db.

Estrutura da tabela:

CREATE TABLE contatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT
);

▶️ Como usar o sistema

Ao rodar o programa, aparecerá um menu semelhante a este:

===== AGENDA DE CONTATOS =====
1. Adicionar contato
2. Listar contatos
3. Buscar contato por nome
4. Editar contato
5. Excluir contato
0. Sair


Basta escolher a opção desejada digitando o número correspondente.

🧪 Testes manuais recomendados

Criar um contato e verificar se aparece na listagem.

Buscar um nome inexistente e observar o retorno.

Atualizar um contato e checar as modificações.

Excluir um contato e confirmar a remoção.

📖 Objetivo Educacional

Este projeto foi desenvolvido para estudos de:

Python sem programação orientada a objetos

Conceitos de CRUD

Arquitetura MVC simples

Manipulação de bancos SQLite

Boas práticas de organização de código

É uma excelente base para evoluir para projetos maiores.
