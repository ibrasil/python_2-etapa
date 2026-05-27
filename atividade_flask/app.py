from flask import Flask
app = Flask(__name__)

@app.route('/decorator')
def explicar():
    return '''
    <h1> O que é um decorator? </h1>
    Um decorator em Python é uma funcionalidade poderosa que permite modificar ou estender o comportamento de funções, métodos ou classes sem alterar o seu código original.
    Eles são definidos como funções que recebem outra função como argumento, envolvem-na (ou "embrulham") com um novo comportamento e a retornam modificada.

    <h1> Para o que serve? </h1>
    Os decorators são usados para aplicar o princípio DRY (Don't Repeat Yourself - Não repita a si mesmo), separando a lógica principal de funcionalidades transversais

    <h1> Como ele é utilizado no flask? </h1>
    No Flask, o decorator @app.route transforma uma função comum do Python em uma view function (função de visualização), mapeando uma URL específica a essa função
'''

if __name__ == '__main__':
    app.run(debug=True)
