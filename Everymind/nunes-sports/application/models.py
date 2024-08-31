import mysql.connector
from application.config import Config

def get_db_connection():
    return mysql.connector.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DB
    )

def obter_produtos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    cursor.close()
    conn.close()
    return produtos

def add_produto(nome, codigo_produto, descricao, preco):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO produtos (nome, codigo_produto, descricao, preco) VALUES (%s, %s, %s, %s)',
        (nome, codigo_produto, descricao, preco)
    )
    conn.commit()
    cursor.close()
    conn.close()

def deletar_produto(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM produtos WHERE id = %s', (product_id,))
    conn.commit()
    cursor.close()
    conn.close()
