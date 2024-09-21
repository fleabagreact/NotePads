import mysql.connector

db_config = {
    'user': 'root',
    #sem nescissade de senha, uso do xampp
    'password': '',
    'host': 'localhost',
}

conn = None

try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE BlocoNotas")
    print("Banco de dados 'BlocoNotas' criado ou já existente.")

    cursor.close()
    conn.close()

    db_config['database'] = 'BlocoNotas'
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    print("Conexão estabelecida com sucesso ao banco de dados 'BlocoNotas'.")

except mysql.connector.Error as erro:
    print(f"Erro ao conectar ou criar banco de dados: {erro}")
finally:
    if conn is not None:
        conn.close()

if conn is not None:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    SCHEMA = "database/database.sql"

    with open(SCHEMA, 'r') as f:
        sql_script = f.read()

    for statement in sql_script.split(';'):
        if statement.strip():
            try:
                cursor.execute(statement)
            except mysql.connector.Error as e:
                print(f"Erro ao executar statement: {e}")

    # Encerra operações
    conn.commit()
    cursor.close()
    conn.close()
    print("Script executado com sucesso.")