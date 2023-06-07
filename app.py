from flask import Flask, render_template
from loginForm import LoginForm

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # Récupérer les données du formulaire
        username = form.username.data
        password = form.password.data

        # Vérifier les informations d'identification ici

        # Rediriger vers la page d'accueil si les informations sont valides

    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run()