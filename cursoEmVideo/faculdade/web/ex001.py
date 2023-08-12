from flask import Flask

app = Flask(__name__)

@app.route('/')
def raiz():
    return "Link para <br><a href='user/'>outra pagina web</a>"

@app.route('/user/')
def user():
    return "altere o endereco de browser"

@app.route('/user/<nome_de_usuario>/')
def user_nome(nome):
    return "Olá, " + nome

if __name__ == '__main__':
    app.run(debug=True)
