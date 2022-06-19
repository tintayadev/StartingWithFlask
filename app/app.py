from flask import Flask, render_template, request

app = Flask(__name__)

@app.before_request
def before_request():
    print('Antes de la peticion...')

@app.after_request
def after_request(response):
    print('Despues de la peticion...')
    return response

'''
@app.route('/')
def index():
    return "CodigoFacilito"
'''


@app.route('/')
def index():
    print('Estamos realizando la peticion...')
    # return "Bievenido a este curso de Codigo Facilito"
    # return render_template("index.html", titulo= 'Pagina principal Uwu')
    data = {
        'titulo': "Página principal",
        'encabezado': "Bienvenido(a)"
    }
    return render_template("index.html", data=data)


@app.route('/contacto')
def contacto():
    data = {
        'titulo': "Contacto",
        'encabezado': "Bienvenido(a)"
    }
    return render_template("contacto.html", data=data)


@app.route('/saludo/<nombre>')
def saludo(nombre: str):
    # return "Hola Codi ;D"
    # return 'Hola!, {0}!'.format(nombre)
    return f'Hola!, {nombre}!'


@app.route('/holaMundo')
def hola_mundo():
    return "Hola Mundo!"


@app.route('/suma/<int:valor1>/<int:valor2>')
def suma(valor1, valor2):
    return f"La suma es {valor1 + valor2}"


@app.route('/perfil/<nombre>/<int:edad>')
def perfil(nombre, edad):
    return f"Tu nombre es {nombre} y tu edad es {edad}"

@app.route('/lenguajes')
def lenguajes():
    data= {
        'hay_lenguajes': True,
        'lenguajes': ['PHP', 'Python', 'Kotlin', 'Swift', 'Java', 'C#', 'JavaScript' ]
    }
    return render_template("lenguajes.html", data=data)

# HTTP: 
@app.route('/datos')
def datos():
    print(request.args)
    language_programming = request.args.get('valor1')
    number = int(request.args.get('valor2'))
    return f'Estos son los datos: {language_programming}, {number+ 15}'

if __name__ == '__main__':
    app.add_url_rule('/', view_func=index)
    app.run(debug=True, port=5005)
