from mysql.connector import connect
from flask_login import UserMixin

def obter_conexao():
    db_config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'BlocoNotas'
    }
    return connect(**db_config)

class User(UserMixin):
    id: str

    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

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

class Nota:
    def __init__(self, id, titulo, descricao, user_id):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.user_id = user_id

    @classmethod
    def get_all_by_user_id(cls, user_id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM notas WHERE user_id=%s', (user_id,))
        dados = cursor.fetchall()
        cursor.close()
        conexao.close()

        notas = []
        for nota in dados:
            notas.append(Nota(nota[0], nota[1], nota[2], nota[3]))
        return notas

    @classmethod
    def add(cls, titulo, descricao, user_id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute('INSERT INTO notas (titulo, descricao, user_id) VALUES (%s, %s, %s)', (titulo, descricao, user_id))
        conexao.commit()
        cursor.close()
        conexao.close()

    @classmethod
    def get_by_id(cls, id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM notas WHERE id=%s', (id,))
        nota = cursor.fetchone()
        cursor.close()
        conexao.close()

        if nota:
            return Nota(nota[0], nota[1], nota[2], nota[3])
        return None

    @classmethod
    def update(cls, id, titulo, descricao):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute('UPDATE notas SET titulo=%s, descricao=%s WHERE id=%s', (titulo, descricao, id))
        conexao.commit()
        cursor.close()
        conexao.close()

    @classmethod
    def delete(cls, id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM notas WHERE id=%s', (id,))
        conexao.commit()
        cursor.close()
        conexao.close()