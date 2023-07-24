            ################################################
            ####                                        ####
            ####               Projet :                 ####
            ####    Faciliter la recherche d'un sujet   ####
            ####                                        ####
            ####            Par Lin Sandrine            #### 
            ####                12/07/23                ####
            ####                                        ####                                   
            ################################################

# # Import des noms du module
from tkinter import *
import see_subject
import add_modif_del


def index():
    # Crée une fenêtre Tkinter
    fenetre = Tk()
    fenetre.title("Où trouver quoi ?")
    fenetre.geometry("450x350")
    fenetre.minsize(450,350)

    #configurer 3 colonnes pour centrer les textes
    fenetre.grid_columnconfigure(0, weight=1)
    fenetre.grid_columnconfigure(1, weight=1)
    fenetre.grid_columnconfigure(2, weight=1)

    # Commentaires 
    remarque_1 = Label(fenetre, text="Binevenue sur le menu principal")
    remarque_2 = Label(fenetre, text="Voici un petit logiciel pour vous aider à trouver les bonnes informations.")
    remarque_1.grid(row=0, column=1)
    remarque_2.grid(row=1, column=1)

    # Espace 
    espace = Label(fenetre)
    espace.grid(row=2, column=1)

    # Boutons de choix 
    # ---- Bouton pour accéder à tous les sujets -----------------------------------------------------------------------------

    view_all_sujbect = Button(fenetre, text=" > Afficher tous les sujets 📋", command=see_subject.get_all_data_subjects)
    view_all_sujbect.grid(row=3, column=1)

    espace = Label(fenetre).grid(row=4, column=1)

    # ---- Bouton pour rechercher un sujet -----------------------------------------------------------------------------
    search_a_subject = Button(fenetre, text=" > Rechercher un sujet 🔍 ", command=see_subject.get_data_user_by_subject)
    search_a_subject.grid(row=5, column=1)

    espace = Label(fenetre).grid(row=6, column=1)

    # ---- Bouton pour rechercher un sujet -----------------------------------------------------------------------------
    search_a_subject = Button(fenetre, text=" > Ajouter un sujet ➕ ", command=add_modif_del.create_subject)
    search_a_subject.grid(row=7, column=1)

    espace = Label(fenetre).grid(row=8, column=1)


    # ---- Bouton pour rechercher un sujet -----------------------------------------------------------------------------
    search_a_subject = Button(fenetre, text=" > Modifier un sujet  🖍️", command=add_modif_del.modify_subject)
    search_a_subject.grid(row=9, column=1)

    espace = Label(fenetre).grid(row=10, column=1)

    # ---- Bouton pour rechercher un sujet -----------------------------------------------------------------------------
    search_a_subject = Button(fenetre, text=" > Supprimer un sujet 🗑️", command=add_modif_del.del_subject)
    search_a_subject.grid(row=11, column=1)

    espace = Label(fenetre).grid(row=12, column=1)

    # ---- Bouton Quitter -----------------------------------------------------------------------------
    quit = Button(fenetre, text=" ✘ Quitter ✘ ", command=fenetre.destroy)
    quit.grid(row=13, column=1)


    fenetre.mainloop()

index()