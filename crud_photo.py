from flask import render_template, request

def crud_photos(db):
    if request.method == 'POST':
        if request.form['action'] == 'add':
            # Récupérer les informations de la nouvelle photo à partir du formulaire
            photo_nom = request.form['photo_nom']
            photo_description = request.form['photo_description']
            photo_date = request.form['photo_date']

            # Insérer la nouvelle photo dans la base de données
            cursor = db.cursor()
            query = "INSERT INTO gallerie (photo_nom, photo_description, photo_date) VALUES (%s, %s, %s)"
            cursor.execute(query, (photo_nom, photo_description, photo_date))
            db.commit()

            # Rediriger vers la page du CRUD des photos
            return render_template('crud_photos.html')

        elif request.form['action'] == 'update':
            # Récupérer les informations de la photo à modifier à partir du formulaire
            photo_id = request.form['photo_id']
            photo_nom = request.form['photo_nom']
            photo_description = request.form['photo_description']
            photo_date = request.form['photo_date']

            # Mettre à jour les informations de la photo dans la base de données
            cursor = db.cursor()
            query = "UPDATE gallerie SET photo_nom = %s, photo_description = %s, photo_date = %s WHERE id_photo = %s"
            cursor.execute(query, (photo_nom, photo_description, photo_date, photo_id))
            db.commit()

            # Rediriger vers la page du CRUD des photos
            return render_template('crud_photos.html')

        elif request.form['action'] == 'delete':
            # Récupérer l'identifiant de la photo à supprimer à partir du formulaire
            photo_id = request.form['photo_id']

            # Supprimer la photo de la base de données
            cursor = db.cursor()
            query = "DELETE FROM gallerie WHERE id_photo = %s"
            cursor.execute(query, (photo_id,))
            db.commit()

            # Rediriger vers la page du CRUD des photos
            return render_template('crud_photos.html')

    # Afficher la liste des photos et le formulaire pour ajouter/modifier/supprimer une photo
    cursor = db.cursor()
    query = "SELECT * FROM gallerie"
    cursor.execute(query)
    photos = cursor.fetchall()

    return render_template('crud_photos.html', photos=photos)