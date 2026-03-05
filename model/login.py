from database.conexao import conectar

def autenticar_usuario(login, senha):
    conexao, cursor = conectar()
     #executado consulta genero
    cursor.execute("INSERT INTO cadastro(usuario, senhas) VALUES(%s, %s)" [login, senha])