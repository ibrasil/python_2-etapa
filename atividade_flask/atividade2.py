from flask import Flask
app = Flask(__name__)

@app.route('/curriculo')
def inicio():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1> Currículo </h1>

        <h2> Informações pessoais: </h2>
        <ul>
            <li> Nome: Isabela Aleixo Brasil Rodriguues </li>
            <li> Email: isabelabrasil3108@gmail.com </li>
            <li> Telefone: 31 99188-9279 </li>
        </ul>

        <h2> Experiência Profissional: </h2>
        <ul>
            <li> Empresa: Hotel San Diego </li>
            <li> Cargo: Administração </li>
            <li> Período: 3° ano do EM </li>
        </ul>

    </body>
    </html>

   

'''

if __name__ == '__main__':
    app.run(debug=True)