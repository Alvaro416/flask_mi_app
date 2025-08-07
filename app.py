from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    '''
    enseña la pag principal de la aplicacion
    renderiza el template 'index.html' que contiene la estructura
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
'''
terminado
'''
