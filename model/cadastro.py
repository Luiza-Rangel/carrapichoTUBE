from database.conexao import conectar
def cadastro(usuario:str, senha:str):
    conexao, cursor = conectar()
     #executado consulta genero
    cursor.execute("INSERT INTO cadastro(usuario, senhas) VALUES(%s, %s)" [usuario, senha])

    #Fechando
    conexao.commit()
    conexao.close()


def verificar_usuario(login:str, senha:str)-> list:
    """ Função que verifica se o usuario esta cadastrado, se estiver
    cadastrado retorno os dados do usuario. se nao estiver cadastrado retorno none. 
    """

    conexao, cursor = conectar()
    cursor.execute("SELECT login, senha FROM usuario WHERE login = %s and senha = %s", [login, senha])
    usuario = cursor.fetchone()

    conexao.commit()
    conexao.close()
    return usuario