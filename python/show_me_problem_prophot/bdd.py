import sqlite3
import itertools

#Connexion à la base de donnée
connection = sqlite3.connect('python_database.db')
cursor = connection.cursor()

# Utilisaiton de la base de données 
class data_subject : 
    id_iter = itertools.count()
    # Fonction pour définir les paramètres de la base de données
    def __init__(data_subject, id_sujet=-1, sujet="", destination="") :
        data_subject.id = next(data_subject.id_iter)
        data_subject.sujet = sujet
        data_subject.destination = destination 
        data_subject.connection = sqlite3.connect('python_database.db')
        data_subject.cursor = data_subject.connection.cursor()

    # Ajouter un sujet
    def add_sujbect(data_subject):
        data_subject.cursor.execute("""
        INSERT INTO info_sujet(sujet, destination) VALUES 
        ('{}','{}')
        """.format(data_subject.sujet, data_subject.destination))

        data_subject.connection.commit()
        data_subject.connection.close()

    # Modifier un sujet
    def modif_subject(data_subject,old_sujet,old_destination): 
        data_subject.cursor.execute("""
        UPDATE info_sujet SET sujet ='{}', destination = '{}' WHERE sujet ='{}' AND destination ='{}'
        """.format(data_subject.sujet, data_subject.destination,old_sujet,old_destination))

        data_subject.connection.commit()
        data_subject.connection.close()

    # Supprimer un sujet
    def del_subject(data_subject,old_sujet,old_destination):
        data_subject.cursor.execute("""
        DELETE FROM info_sujet 
        WHERE sujet = '{}' AND destination = '{}'
        """.format(data_subject.sujet, data_subject.destination,old_sujet,old_destination))

        data_subject.connection.commit()
