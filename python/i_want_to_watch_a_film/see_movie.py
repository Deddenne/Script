#importe de librairies 
from tkinter import *
from tkinter.ttk import *
import bdd
import os 

#permet de pouvoir utiliser la classe data_sujet() importé depuis bdd
data = bdd.data_movie()

# FONCTION : Recherche TOUS LES SUJETS ------------------------------------------------------------------
def get_all_data_movies (): 
    fenetre = Tk()
    fenetre.title("Enumération de tous les sujets")
    fenetre.geometry("1500x450")
    fenetre.minsize(1500,450)
    fenetre.grid_columnconfigure(0, weight=1)
    fenetre.grid_columnconfigure(1, weight=1)
    fenetre.grid_columnconfigure(2, weight=1)
    espace = Label(fenetre).grid(row=0, column=1)

    libelle = Label(fenetre, text = 'Listes de tous les sujets').grid(row=1, column=1)

    #tableau
    tableau = Treeview(fenetre, columns=('Nom du film', 'Langue','Parution','Genre', 'Durée','Fini','Commentaire'), height=15)
    tableau.heading('Nom du film', text='Nom du film')
    tableau.heading('Langue', text='Langue')
    tableau.heading('Parution', text='Parution')
    tableau.heading('Genre', text='Genre')
    tableau.heading('Durée', text='Durée')
    tableau.heading('Fini', text='Fini')
    tableau.heading('Commentaire', text='Commentaire')
    tableau.column("#1", minwidth=0, width=350, stretch=NO)
    tableau.column("#2", minwidth=0, width=80, stretch=NO)
    tableau.column("#3", minwidth=0, width=70, stretch=NO)
    tableau.column("#4", minwidth=0, width=310, stretch=NO)
    tableau.column("#5", minwidth=0, width=60, stretch=NO)
    tableau.column("#6", minwidth=0, width=60, stretch=NO)
    tableau.column("#7", minwidth=0, width=400, stretch=NO)
    tableau['show'] = 'headings' # sans ceci, il y avait une colonne vide à gauche qui a pour rôle d'afficher le paramètre "text" qui peut être spécifié lors du insert
    tableau.grid(row=2, column=1)


    # Requête SQL pour récupérer les informations à afficher
    data.cursor.execute("SELECT id, name_movie, language, years, genre, time, finish, comment FROM movie ORDER BY name_movie ASC")
    results = data.cursor.fetchall()
    if len(results):
        for enreg in results:
            # chaque ligne n'a pas de parent, est ajoutée à la fin de la liste, utilise le champ id comme identifiant et on fournit les valeurs pour chacune des colonnes du tableau
            tableau.insert('', 'end', iid=enreg[0], values=(enreg[1], enreg[2], enreg[3], enreg[4], enreg[5], enreg[6], enreg[7]))
    espace = Label(fenetre).grid(row=3, column=1)

    # Ouvrir le répertoire ou le fichier 
    def open(row):
        os.startfile(row)

    # sélectionner la ligne 
    def select_row(a) : 
        selectedItem = tableau.selection()[0]
        row = tableau.item(selectedItem)['values'][1]
        open(row)

    tableau.bind("<<TreeviewSelect>>", select_row)

    def retun_menu_principal():
        fenetre.destroy()
    quit = Button(fenetre, text=" 🔙 Retrouner sur le menu principal ", command=retun_menu_principal).grid(row=9, column=1)

    espace = Label(fenetre).grid(row=10, column=1)


# FONCTION : Recherche par le SUJET ------------------------------------------------------------------
def get_data_user_by_subject():
    fenetre = Tk()
    fenetre.title("Recherche par films")
    fenetre.geometry("400x200")
    fenetre.grid_columnconfigure(0, weight=1)
    fenetre.grid_columnconfigure(1, weight=1)
    fenetre.grid_columnconfigure(2, weight=1)
    espace = Label(fenetre).grid(row=0, column=1)

    # Demander le nom de l'utilisateur à chercher
    subject_entry = Label(fenetre, text=" Que cherchez-vous ? ").grid(row=3, column=0)
    subject_entry = Entry(fenetre)
    subject_entry.grid(row=3, column=1)

    def languagereseach_data(select_subject):
        fenetre = Tk()
        fenetre.title("Recherche...")
        fenetre.geometry("1500x450")
        fenetre.minsize(1500,450)
        fenetre.grid_columnconfigure(0, weight=1)
        fenetre.grid_columnconfigure(1, weight=1)
        fenetre.grid_columnconfigure(2, weight=1)
        espace = Label(fenetre).grid(row=1, column=1)
        
        #tableau
        tableau = Treeview(fenetre, columns=('Nom du film', 'Langue','Parution','Genre', 'Durée','Fini','Commentaire'), height=15)
        tableau.heading('Nom du film', text='Nom du film')
        tableau.heading('Langue', text='Langue')
        tableau.heading('Parution', text='Parution')
        tableau.heading('Genre', text='Genre')
        tableau.heading('Durée', text='Durée')
        tableau.heading('Fini', text='Fini')
        tableau.heading('Commentaire', text='Commentaire')
        tableau.column("#1", minwidth=0, width=350, stretch=NO)
        tableau.column("#2", minwidth=0, width=80, stretch=NO)
        tableau.column("#3", minwidth=0, width=70, stretch=NO)
        tableau.column("#4", minwidth=0, width=310, stretch=NO)
        tableau.column("#5", minwidth=0, width=60, stretch=NO)
        tableau.column("#6", minwidth=0, width=60, stretch=NO)
        tableau.column("#7", minwidth=0, width=400, stretch=NO)
        tableau['show'] = 'headings' # sans ceci, il y avait une colonne vide à gauche qui a pour rôle d'afficher le paramètre "text" qui peut être spécifié lors du insert
        tableau.grid(row=2, column=1)
        
        # Requête SQL pour récupérer les informations à afficher
        subject_entry =  "SELECT id, name_movie, language, years, genre, time, finish, comment FROM movie WHERE name_movie LIKE '%" + str(select_subject) +"%' ORDER BY name_movie ASC"
        data.cursor.execute(subject_entry)
        results = data.cursor.fetchall()
        if len(results):
            for enreg in results:
                # chaque ligne n'a pas de parent, est ajoutée à la fin de la liste, utilise le champ id comme identifiant et on fournit les valeurs pour chacune des colonnes du tableau
                tableau.insert('', 'end', iid=enreg[0], values=(enreg[1], enreg[2], enreg[3], enreg[4], enreg[5], enreg[6], enreg[7]))

        # Ouvrir le répertoire ou le fichier 
        def open(row):
            os.startfile(row)

        # sélectionner la ligne 
        def select_row(a) : 
            selectedItem = tableau.selection()[0]
            row = tableau.item(selectedItem)['values'][1]
            open(row)

        tableau.bind("<<TreeviewSelect>>", select_row)

        # détruire la fenêtre précédante (fenêtre qui demande le nom) et affichier la nouvelle (fenêtre données user)
        def retun_menu_principal():
            fenetre.destroy()
        espace = Label(fenetre).grid(row=8, column=1)
        quit = Button(fenetre, text=" 🔙 Retrouner sur le menu principal ", command=retun_menu_principal).grid(row=9, column=1)

    # détruire la fenêtre précédante (fenêtre avec données user) et affichier la nouvelle (menu principal)
    def close_data(): 
        # Récupérer le nom de l'utilisateur entrée 
        select_subject = subject_entry.get()
        fenetre.destroy()
        languagereseach_data(select_subject)
    reseach = Button(fenetre, text=" Lancer la recherche 🔍 ", command=close_data).grid(row=3, column=2)


    # Espace 
    espace = Label(fenetre).grid(row=4, column=1)