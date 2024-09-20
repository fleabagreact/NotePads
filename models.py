from flask_login import UserMixin
import mysql.connector as sql

# Função para obter a conexão com o banco de dados
def obter_conexao():
    db_config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'prova'
    }
    return sql.connect(**db_config)

class User(UserMixin):
    id: str
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    # Busca um usuário pelo id (matrícula) no banco de dados
    @classmethod
    def get(cls, id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE id=%s', (id,))
        dados = cursor.fetchone()
        cursor.close()
        conexao.close()

        if dados:
            user = User(dados[1], dados[2])
            user.id = dados[0]
        else:
            user = None
        return user
    
    # Busca um usuário pelo número de matrícula
    @classmethod
    def select_get_by_email(cls, email):
        conexao = obter_conexao()
        cursor = conexao.cursor(buffered=True)
        cursor.execute('SELECT * FROM usuarios WHERE email=%s', (email,))
        dados = cursor.fetchone()
        cursor.close()
        conexao.close()
        if dados:
            user = User(dados[1], dados[2])
            user.id = dados[0]
            return user
        
    @classmethod
    def insert_data_user(cls, email, senha):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute('INSERT INTO usuarios (email, senha) VALUES (%s, %s)', (email, senha))
        conexao.commit()
        cursor.close()
        conexao.close()