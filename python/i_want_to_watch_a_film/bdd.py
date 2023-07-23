import sqlite3
import itertools

#Connexion à la base de donnée
connection = sqlite3.connect('python_database.db')
cursor = connection.cursor()

# Utilisaiton de la base de données 
class data_movie : 
    id_iter = itertools.count()
    # Fonction pour définir les paramètres de la base de données
    def __init__(data_movie, id=-1, name_movie="", language="", years="", genre="", time="", finish="", comment="") :
        data_movie.id = next(data_movie.id_iter)
        data_movie.name_movie = name_movie
        data_movie.language = language 
        data_movie.years = years
        data_movie.genre = genre
        data_movie.time = time
        data_movie.finish = finish
        data_movie.comment = comment
        data_movie.connection = sqlite3.connect('python_database.db')
        data_movie.cursor = data_movie.connection.cursor()

    # Ajouter un name_movie_1
    def add_sujbect(data_movie):
        data_movie.cursor.execute("""
        INSERT INTO movie (name_movie, language, years, genre, time, finish, comment) VALUES 
        ('{}','{}','{}','{}','{}','{}','{}')
        """.format(data_movie.name_movie, data_movie.language, data_movie.years, data_movie.genre, data_movie.time, data_movie.finish, data_movie.comment))

        data_movie.connection.commit()
        data_movie.connection.close()

    # Modifier un name_movie_1
    def modif_subject(data_movie, new_name, new_parution, new_time): 
        data_movie.cursor.execute("""
        UPDATE movie SET name_movie ='{}', language = '{}', years = '{}', genre = '{}', time = '{}', finish = '{}', comment = '{}' WHERE name_movie ='{}' AND years = '{}' AND time = '{}'
        """.format(data_movie.name_movie, data_movie.language, data_movie.years, data_movie.genre, data_movie.time, data_movie.finish, data_movie.comment,new_name, new_parution, new_time))

        data_movie.connection.commit()
        data_movie.connection.close()

    # Supprimer un name_movie_1
    def del_subject(data_movie,old_name_movie,old_years,old_time):
        data_movie.cursor.execute("""
        DELETE FROM movie 
        WHERE name_movie ='{}' AND years = '{}' AND time = '{}'
        """.format(data_movie.name_movie, data_movie.language, data_movie.years, data_movie.genre, data_movie.time, data_movie.finish, data_movie.comment,old_name_movie,old_years,old_time))

        data_movie.connection.commit()
