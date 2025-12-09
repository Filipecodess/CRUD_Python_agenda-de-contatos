---

# 📇 Agenda de Contatos — CRUD em Python + SQLite3 (Arquitetura MVC sem POO)

Este projeto é uma **Agenda de Contatos** desenvolvida em **Python 3**, utilizando **SQLite3**, e organizada no padrão arquitetural **MVC (Model–View–Controller)**, **sem as técnicas e conceitos mais fundamentais de Programação Orientada a Objetos**, seguindo um estilo de código baseado exclusivamente em funções.
É um projeto simples e direto do curso de coding da faculdade Senac do Recife

---

## 📁 Estrutura do Projeto

```
PYTHON_AGENDA_CONTATOS/
│── banco_dados.py          # Parte responsável pelo banco de dados (CRUD real), temos a camada MODEL
│── controller.py     # Lógica intermediária entre o banco e o usuário
│── main.py           # Menu principal e interação no terminal
│── agenda_contatos.db   # Gerado automaticamente
```

---

## 🧠 Objetivo do Projeto

* Praticar Python com foco em funções (sem "POO")
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
* **VIEW** → interação do usuário (não foi feito ainda pois deve ter algum tempo de estudo, interações foi feito no terminal [main])
* * **MAIN** → Menu e interação com o usuário via terminal 

Esse padrão deixa o código mais limpo, modular e fácil de manter.

---

## 📝 Melhorias Futuras (Sugestões)

* Criar interface gráfica com **Tkinter** ou **Flet**
* Exportar contatos para **CSV**
* Criar testes automatizados com **pytest**
* Transformar o projeto em API usando **Flask** ou **FastAPI**
* Desenvolver uma versão em POO para fins comparativos

---

## 🤝 Contribuições

Contribuições são muito bem-vindas!
Sinta-se à vontade para abrir **Issues** ou enviar **Pull Requests**.

---

**Vamos por mais! 📚**
