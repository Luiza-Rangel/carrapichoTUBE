from flask import Flask, render_template, request, redirect
import mysql.connector
from model.musica import recuperar_musica, excluir_musica
from model.genero import recuperar_generos
from model.musica import salvar_musica, ativo
from model.cadastro import cadastro, verificar_usuario

app = Flask(__name__)

@app.route("/home", methods=["GET"])
@app.route("/")
def pg_principal():

    musicas = recuperar_musica()
    generos = recuperar_generos()



    return render_template("principal.html", musicas = musicas, generos = generos)


@app.route("/admin")
def pg_administracao():
    musicas = recuperar_musica()
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

@app.route("/musica/ativar/<codigo>/<status>")
def atualizar(codigo,status):
    ativo(codigo, status)
    return redirect("/admin")

@app.route("/cadastro")
def cadastro():
    # Renderiza o arquivo criado na pasta templates
    return render_template("cadastro.html")

@app.route("/cadastro", methods=["POST"])
def rota_cadastro_usuario():
    usuario = request.form.get("nome")
    senha = request.form.get("senha")
    cadastro(usuario, senha)
    return redirect("/cadastro")

@app.route("/login", methods=["POST"])
def rota_login():
    login = request.form.get("usuario")
    senha = request.form.get("senha")
    usuario = verificar_usuario(login, senha)
    if usuario:
        return redirect("/admin")
    else:
        return redirect("/login")




if __name__ == "__main__":
    app.run(debug=True)
