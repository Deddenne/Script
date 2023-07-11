################################################
####                                        ####
####         PROJET PYTHON - 3SRC3          ####
####                                        ####
####          Anthime & Sandrine            ####
####                                        ####
####         Interface graphique :          ####
####       Fichier accueil super-adm        ####
####                                        ####
################################################


# ADMIN S connecté ok
# 	1. créa user -> 1. Génération login ; 2. Génération mdp ; 3. Quitter
# 	2. modif user -> 1. login ; 2. mdp ; 3. quitter
# 	3. supp user -> à entrer nom,prénom  et confirmer
# 	4. consultation -> 1. tous les users ; 2. un user ; 3. Quitter
# 	5. Quitter 


# # Import des noms du module
from tkinter import *
import see_subject


def super_adm():
    # Crée une fenêtre Tkinter
    fenetre = Tk()
    fenetre.title("Où trouver quoi ?")
    fenetre.geometry("400x300")
    fenetre.minsize(400,300)

    #configurer 3 colonnes pour centrer les textes
    fenetre.grid_columnconfigure(0, weight=1)
    fenetre.grid_columnconfigure(1, weight=1)
    fenetre.grid_columnconfigure(2, weight=1)

    # Commentaires 
    remarque_1 = Label(fenetre, text="Binevenue sur le menu principal")
    remarque_2 = Label(fenetre, text="Voici un petit logiciel poru vous aider à trouver les bonnes informations.")
    remarque_1.grid(row=0, column=1)
    remarque_2.grid(row=1, column=1)

    # Espace 
    espace = Label(fenetre)
    espace.grid(row=2, column=1)

    # Boutons de choix 
    # ---- Bouton pour accéder à tous les sujets -----------------------------------------------------------------------------

    button_create_user = Button(fenetre, text=" > Afficher tous les sujets 📋", command=see_subject.get_all_data_subjects)
    button_create_user.grid(row=3, column=1)

    espace = Label(fenetre).grid(row=4, column=1)

    # ---- Bouton pour rechercher un sujet -----------------------------------------------------------------------------
    button_modify_user = Button(fenetre, text=" > Rechercher un sujet 🔍 ", command=see_subject.get_data_user_by_subject)
    button_modify_user.grid(row=5, column=1)

    espace = Label(fenetre).grid(row=6, column=1)

    # ---- Bouton Quitter -----------------------------------------------------------------------------
    quit = Button(fenetre, text=" ✘ Quitter ✘ ", command=fenetre.destroy)
    quit.grid(row=12, column=1)


    fenetre.mainloop()

super_adm()