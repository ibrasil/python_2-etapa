from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def questao1():
    nomep = "Isabela"
    return render_template('questao1.html', nome=nomep)

@app.route('/questao2')
def questao2():
    nomep = "Isabela"
    idadep = "17"
    return render_template('questao2.html', nome=nomep, idade=idadep)

@app.route('/questao3')
def questao3():
    nomep = "Isabela"
    emailp = "isabelabrasil3108@gmail.com"
    return render_template('questao3.html', nome=nomep, email=emailp)

@app.route("/questao4")
def questao4():
    aluno = [
        {"nome" : "isabela", "nota": 8},
        {"nome" : "ana", "nota": 7},
        {"nome": "hugo", "nota": 6}
    ]
    return render_template('questao4.html', alunos = aluno)


@app.route('/questao5')
def questao5():
    lista_alunos = [
        {"nome: ": "isabela", "nota": 8},
        {"nome: ": "ana", "nota": 7},
        {"nome: ": "hugo", "nota": 6}
    ]
    return render_template('questao5.html', alunos=lista_alunos)

    


if __name__ == '__main__':
    app.run(debug=True)