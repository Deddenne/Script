import sqlite3
import itertools

#Connexion à la base de donnée
connection = sqlite3.connect('python_database.db')
cursor = connection.cursor()

# Créer une table de donnée
cursor.execute("""
CREATE TABLE IF NOT EXISTS info_sujet (
    id_sujet integer primary key,
    sujet TEXT,
    destination TEXT
)
""")

class data_sujet : 
    id_iter = itertools.count()
    # Fonction pour définir les paramètres de la base de données
    def __init__(data_sujet, id_sujet=-1, sujet="", destination="") :
        data_sujet.id = next(data_sujet.id_iter)
        data_sujet.sujet = sujet
        data_sujet.destination = destination 
        data_sujet.connection = sqlite3.connect('python_database.db')
        data_sujet.cursor = data_sujet.connection.cursor()

    

