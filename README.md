# NotePads

Este é um aplicativo web simples de bloco de notas e lista de tarefas, desenvolvido com Flask e MySQL.

## Estrutura do Projeto

- **database/**: Contém o arquivo SQL para a criação do banco de dados.
  - `database.sql`: Script de criação das tabelas para o banco de dados MySQL.

- **static/**: Pasta para arquivos estáticos (como CSS).
  - `style.css`: Estilos personalizados para o layout do aplicativo.

- **templates/**: Contém os templates HTML usados pelo Flask para renderizar as páginas.
  - `add_tarefa.html`: Página para adicionar novas tarefas.
  - `dash.html`: Painel principal do usuário após login.
  - `index.html`: Página inicial do aplicativo.
  - `login.html`: Página de login.
  - `nota.html`: Página para criar e editar notas.
  - `register.html`: Página de registro de novos usuários.
  - `tarefa.html`: Página que lista todas as tarefas do usuário.
  - `ver_nota.html`: Página que exibe as notas do usuário.

- **app.py**: Arquivo principal da aplicação Flask que define as rotas e o comportamento do servidor.

- **init_db.py**: Script para inicializar e configurar o banco de dados MySQL.

- **models.py**: Arquivo contendo as classes de modelo que representam as entidades do banco de dados, como `User`, `Nota`, e `Tarefa`.

- **README.md**: Este arquivo, com informações sobre o projeto.

- **requirements.txt**: Lista de dependências do projeto, utilizadas para instalar as bibliotecas necessárias.

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
