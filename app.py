from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/location')
def location():
    return render_template('location.html')

if __name__ == '__main__':
    app.run(debug=True)