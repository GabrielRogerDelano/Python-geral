from flask import Flask

app = Flask(__name__)


@app.route('/')
def raiz():
    return "Olá, Entre no endereco com dois numeros"


@app.route('/somar/')
@app.route('/somar/<n1>/<n2>')
def somar(n1 = 0.0, n2=0.0):
    resultado = float(n1) + float(n2)
    return str(resultado)

if __name__ == '__main__':
    app.run(debug=True)
