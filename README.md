# NotePads

Este é um aplicativo web simples de bloco de notas e lista de tarefas, desenvolvido com Flask e MySQL.

## Estrutura do Projeto

NotePads/
│
├── database/
│   └── database.sql         # Script SQL para criação das tabelas
│
├── static/
│   └── style.css            # Arquivo de estilo CSS
│
├── templates/
│   ├── add_tarefa.html      # Template para adicionar tarefas
│   ├── dash.html            # Dashboard principal
│   ├── index.html           # Página inicial
│   ├── login.html           # Página de login
│   ├── nota.html            # Template para adicionar/editar notas
│   ├── register.html        # Página de registro
│   ├── tarefa.html          # Página para exibir tarefas
│   └── ver_nota.html        # Página para visualizar notas
│
├── app.py                   # Arquivo principal da aplicação Flask
├── init_db.py               # Script para inicializar o banco de dados MySQL
├── models.py                # Modelos e funções de acesso ao banco de dados
├── README.md                # Este arquivo
├── requirements.txt         # Dependências da aplicação

## Funcionalidades

- **Autenticação de Usuário**: Registro, login e logout.
- **Bloco de Notas**: Adicionar, editar, visualizar e deletar notas.
- **Lista de Tarefas**: Adicionar e deletar tarefas.
- **Envio de Emails**: Envia emails de boas-vindas para o usuário registrado.

## Instalação e Execução

1. Clone este repositório:

   ```bash
   git clone https://github.com/fleabagreact/NotePads.git
   ```

2. Crie um ambiente virtual:

   - **No Linux/MacOS**:

     ```bash
     python3 -m venv env
     source env/bin/activate
     ```

   - **No Windows**:

     ```bash
     python -m venv venv
     .\env\Scripts\activate
     ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure o banco de dados MySQL:

   ```bash
   python init_db.py
   ```

5. Execute a aplicação:

   ```bash
   flask run --debug
   ```

6. Acesse o aplicativo em `http://127.0.0.1:5000/`.

## Tecnologias Utilizadas

- Python
- Flask
- MySQL
- HTML/CSS
