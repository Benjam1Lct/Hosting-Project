from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/connexion')
def connexion():
    return render_template('connexion.html')

@app.route('/inscription')
def inscription():
    return render_template('inscription.html')

@app.route('/mobile')
def mobile():
    return render_template('mobile.html')

if __name__ == '__main__':
    app.run(debug=True)