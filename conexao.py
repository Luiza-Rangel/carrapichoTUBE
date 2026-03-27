import mysql.connector

conexao_banco = "LOCAL"

def conectar():
        if conexao_banco == "LOCAL":
                
            conexao = mysql.connector.connect(
                    host="localhost",
                    port=3306,
                    user="root",
                    password= "root",
                    database= "carrapichoTube"
                )
        else:
              conexao = mysql.connector.connect(
                    host="servidor-luizarangel-luizarangel.a.aivencloud.com",
                    port=20659,
                    user="avnadmin",
                    password= "<redacted>",
                    database= "defaultdb"
                    )
            #criando cursor
        cursor = conexao.cursor(dictionary=True)

        return conexao, cursor
        