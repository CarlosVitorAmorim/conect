import mysql.connector

def conectar():
    host = 'localhost'
    usuario = 'root'
    senha = 'admin'
    banco_de_dados = 'meubanco'
    
    
    conexao = mysql.connector.connect(
        host = host
        user = usuario,
        password = senha,
        database = banco_de_dados,
    )
    
    return conexao

def criar_tabela(conexao):
    curso = conexao.curso()
    
    curso.execute('''
        CREATE TABLE IF NOT EXISTS aluno(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255),
            data_nascimento DATE,
            cidade_natal VARCHAR(255),
            bairro VARCHAR(255)
        )
    
    ''')
    
    conexao.commit()
    
def cadastra_aluno(conexao,nome,data_nascimento,cidade_natal,bairro):
    curso = conexao.curso()
    
    isenrir_query = '''
        INSERT INTO aluno (nome,data_nascimento,cidade_natal,bairro)
        VALUES(%s,%s,%s,%s)
    '''
    
    valores = (nome,data_nascimento,cidade_natal,bairro)
    curso.execute(isenrir_query,valores)
    conexao.commit()