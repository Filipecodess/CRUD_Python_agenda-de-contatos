Aqui está o **README.md** em formato Markdown, totalmente organizado, formatado e pronto para colar no GitHub — mantendo o conteúdo que você trouxe, mas deixando mais elegante, estruturado e profissional.

---

# 📇 Agenda de Contatos — CRUD em Python + SQLite3 (Arquitetura MVC sem POO)

Este projeto é uma **Agenda de Contatos** desenvolvida em **Python 3**, utilizando **SQLite3**, e organizada no padrão arquitetural **MVC (Model–View–Controller)** — tudo **sem Programação Orientada a Objetos**, seguindo um estilo de código baseado exclusivamente em funções.
É um projeto educativo, simples e direto, ideal para iniciantes que desejam consolidar os fundamentos de Python e banco de dados.

---

## 📁 Estrutura do Projeto

```
agenda_contatos/
│── model.py          # Parte responsável pelo banco de dados (CRUD real)
│── controller.py     # Lógica intermediária entre o banco e o usuário
│── main.py           # Menu principal e interação no terminal
│── agenda_contatos.db   # Gerado automaticamente
│── README.md         # Documentação
```

---

## 🧠 Objetivo do Projeto

* Praticar Python com foco em funções (sem POO)
* Compreender o fluxo de um CRUD completo
* Aprender a manipular banco SQLite
* Entender como funciona uma arquitetura MVC na prática
* Criar um sistema simples, funcional e fácil de executar

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **SQLite3** (nativo do Python)
* Funções e modularização
* Terminal / CLI
* Nenhuma dependência externa necessária

---

## 📦 Requisitos para Executar

* Python 3.10 ou superior
* Sistemas suportados:

  * Windows
  * Linux
  * macOS
* Editor recomendado: **VS Code**

---

## ▶️ Como Executar o Projeto

Clone o repositório:

```sh
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
```

Acesse a pasta:

```sh
cd NOME_DO_REPOSITORIO
```

Execute o sistema:

```sh
python main.py
```

O arquivo **agenda_contatos.db** será criado automaticamente ao iniciar o sistema.

---

## 📚 Funcionalidades do Sistema (CRUD Completo)

### ➕ Criar contato

Permite cadastrar um novo contato informando:

* Nome
* Telefone
* E-mail
* Endereço
* Observações

### 📑 Listar contatos

Exibe todos os contatos armazenados no banco SQLite, ordenados por nome.

### 🔍 Buscar por nome

Localiza contatos utilizando parte do nome.
Exemplo:

* “an” → Ana, André, Fernanda…

### 📝 Atualizar contato

Permite modificar qualquer informação de um contato existente.

### 🗑️ Excluir contato

Remove contatos definitivamente do banco de dados.

---

## 🧩 Arquitetura MVC Utilizada

O projeto segue o padrão:

* **MODEL** → Conexão com banco de dados e execução das operações SQL
* **CONTROLLER** → Regras de negócio e validações
* **MAIN** → Menu e interação com o usuário via terminal

Esse padrão deixa o código mais limpo, modular e fácil de manter.

---

## 📝 Melhorias Futuras (Sugestões)

* Criar interface gráfica com **Tkinter** ou **Flet**
* Exportar contatos para **CSV**
* Criar testes automatizados com **pytest**
* Transformar o projeto em API usando **Flask** ou **FastAPI**
* Desenvolver uma versão em POO para fins comparativos

---

## 🎓 Público-alvo

Este projeto é indicado para:

* Iniciantes em Python
* Quem deseja aprender CRUD com SQLite
* Pessoas estudando MVC sem POO
* Projetos acadêmicos e portfólio
* Quem quer entender lógica de programação aplicada

---

## 🤝 Contribuições

Contribuições são muito bem-vindas!
Sinta-se à vontade para abrir **Issues** ou enviar **Pull Requests**.

---

Se quiser, posso também:

✅ Criar uma versão **em inglês**
✅ Criar **badges** de tecnologia para deixar o README mais bonito
✅ Gerar um **modelo de commit** para esse projeto
✅ Criar uma **licença MIT**

É só pedir!
