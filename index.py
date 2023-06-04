from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    info = ("xddd", "huevo", "hambre", "zanahoria", "gato")
    return render_template('index.html', informacion=info)


@app.route("/contacto")
def contacto():
    return "pagina de contacto"


if __name__ == '__main__':
    app.run(debug=True)

