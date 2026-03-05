from database.conexao import conectar
def cadastro(usuario:str, senha:str):
    conexao, cursor = conectar()
     #executado consulta genero
    cursor.execute("INSERT INTO cadastro(usuario, senhas) VALUES(%s, %s)" [usuario, senha])

    #Fechando
    conexao.commit()
    conexao.close()