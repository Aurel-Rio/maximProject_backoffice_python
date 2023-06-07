from flask import Flask, render_template, request, redirect
import mysql.connector
import crud_photo

app = Flask(__name__)

# Paramètres de connexion à la base de données MySQL
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='maximarmengolcasino'
)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Vérification des informations d'identification en base de données
        cursor = db.cursor()
        query = "SELECT * FROM admin WHERE pseudo = %s AND mdp = %s"
        cursor.execute(query, (username, password))
        admin = cursor.fetchone()

        if admin:
            # Informations d'identification valides, rediriger vers la page du CRUD des photos
            return redirect('/crud-photos')
        else:
            # Informations d'identification invalides, afficher un message d'erreur
           return render_template('login.html')

    return render_template('login.html')

@app.route('/crud-photos')
def crud_photos_route():
    return crud_photo.crud_photos(db)

if __name__ == '__main__':
    app.run()