from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'this is the Index Page, and it has no html static page, just this. Trippy right?'

# @app.route('/hello')
# def hello_world():
#     return 'Hello World!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/variables/')
def variables():
    return render_template('variables.html' )

if __name__ == '__main__':
    app.run(debug=True)
