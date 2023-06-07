from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Vérifier les informations d'identification ici

        # Rediriger vers la page d'accueil si les informations sont valides

    return render_template('login.html')

if __name__ == '__main__':
    app.run()