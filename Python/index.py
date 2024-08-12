from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")

@app.route('/consulta')
def consulta():
    return render_template("consulta.html")


if __name__ == '__main__':
    app.run(debug=True)