from flask import Flask

# instancia a classe do flask
app = Flask(__name__)

# pagina raiz
@app.route('/')
def index():
    return "Pagina principal"


@app.route('/ola/')
@app.route('/ola/<nome>/')
def ola_maundo(nome='mundo'):
    return "ola, " + nome


@app.route('/logar/', methods=['GET', 'POST'])
def logar():
    if request.method == 'POST':
        return "Recebeu Post! Fazer login"
    else:
        return "Recebeu Get! Exibir form de login"


if __name__ == '__main__':
    app.run()
