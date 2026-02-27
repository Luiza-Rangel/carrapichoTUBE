from database.conexao import conectar

def recuperar_musica(ativos:bool = False):
    #passo 1 e 2 fitos
    conexao, cursor = conectar()
     
     #executando a consulta       
    cursor.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero, ativo FROM musica") 


    musicas = cursor.fetchall()

    #fechando
    conexao.close()      

    return musicas         

def salvar_musica( cantor: str, duracao: str, nome: str,  imagem: str, genero: str) -> bool:
    """ Essa função serve para salvar as musicas dentro da função, e o bool vai mostrar se deu ou nao certo"""
    try:
        conexao, cursor = conectar()

        cursor.execute("""INSERT INTO musica (cantor, duracao, nome, url_imagem, nome_genero) 
                    VALUES (%s, %s, %s, %s, %s)""", [cantor, duracao, nome, imagem, genero])

        conexao.commit()

      
        conexao.close()

        return True
    except Exception as erro:
        print(erro)
        return False

def excluir_musica(codigo):
    

    conexao, cursor = conectar()
     
     #executando a consulta       
    cursor.execute("delete from musica where codigo = %s", (codigo,)) 


    conexao.commit()
    #fechando
    conexao.close()      

def ativo(codigo, status):
    conexao,cursor= conectar() #Conexao
    status = int(status)
    status_atual = 0 if status == 1 else 1
    cursor.execute("update musica set ativo = %s where codigo = %s",(status_atual,codigo))
    conexao.commit()
    conexao.close()