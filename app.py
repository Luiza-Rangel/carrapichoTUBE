from flask import Flask, render_template, request, redirect
import mysql.connector
from model.musica import lista_musicas, excluir_musica
from model.genero import recuperar_generos
from model.musica import salvar_musica


app = Flask(__name__)

@app.route("/home", methods=["GET"])
@app.route("/")
def pg_principal():

    musicas = lista_musicas()
    generos = recuperar_generos()



    return render_template("principal.html", musicas = musicas, generos = generos)


@app.route("/admin")
def pg_administracao():
    musicas = lista_musicas()
    generos = recuperar_generos()
    return render_template("administracao.html", musicas = musicas, generos = generos)

@app.route("/musica/post", methods=["POST"])
def api_inserir_musica():
    nome_musica = request.form.get("input-nome")
    cantor = request.form.get("input-cantor")
    genero = request.form.get("input-genero")
    duracao = request.form.get("input-duracao")
    imagem = request.form.get("input-imagem")
    try:
        if salvar_musica(cantor, duracao, nome_musica, imagem, genero):
            return redirect("/admin")
        else: return "erro"
    except Exception as erro:
        print(erro)
    

@app.route("/musica/delete/<codigo>")
def deletar_musica(codigo):
    excluir_musica(codigo)
    return redirect("/admin")

@app.route()




    
 

if __name__ == "__main__":
    app.run(debug=True)
