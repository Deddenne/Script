################################################
####                                        ####
####         PROJET PYTHON - 3SRC3          ####
####                                        ####
####          Anthime & Sandrine            ####
####                                        ####
#### Fichier en rapport avec un utilisateur ####
####   Création, Modification, Supression   ####
####                                        ####
################################################


##### LIER LES INFO A LA BASE DE DONNE

#importe de librairies 
import bdd
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *


#permet de pouvoir utiliser la classe user() importé depuis bdd
data = bdd.data_movie()

# CREATION d'un nouveau sujet  -----------------------------------------------------------------------------------------------------------
def create_subject() :
    # Crée une fenêtre Tkinter
    fenetre = Tk()
    fenetre.geometry("800x200")
    fenetre.minsize(800,200)
    fenetre.grid_columnconfigure(0, weight=1)
    fenetre.grid_columnconfigure(1, weight=1)
    fenetre.grid_columnconfigure(2, weight=1)
    titre = Label(fenetre, text = "Création d'un nouveau sujet").grid(row=0, column=1)

    remaque = Label(fenetre, text = "Veuillez entrer les informations suivantes : ").grid(row=1, column=1)
    espace = Label(fenetre).grid(row=2, column=1)

    name_subject = Label(fenetre, text=" Entrer le nom du sujet : ").grid(row=3, column=0)
    name_subject = Entry(fenetre)
    name_subject.configure(width=40)
    name_subject.grid(row=3, column=1)

    # Ajoute un libellé pour le mot de passe
    destination_subject = Label(fenetre, text=" Entrer un commentaire ou le chemain complet vers le fichier : ").grid(row=4, column=0)
    destination_subject = Entry(fenetre)
    destination_subject.configure(width=40)
    destination_subject.grid(row=4, column=1)

    # Espace 
    espace = Label(fenetre).grid(row=5, column=3)

    #GET POUR RECUPERER LES INFORMATIONS ET ENVOYER DANS LA BASE DE DONNEES
    def get_subject_info():
        sujet = name_subject.get()
        destination = destination_subject.get()
        # envoyer les données à la base de données
        data_envoie = bdd.data_movie(0,sujet,destination)
        data_envoie.add_sujbect()

    # Ajoute un bouton de validation
    button_valide = Button(fenetre, text="  Valider et créer le sujet ✓  ", command=get_subject_info)
    button_valide.grid(row=9, column=3)

    espace = Label(fenetre).grid(row=10, column=3)

    def retun_menu_principal():
        fenetre.destroy()
    quit = Button(fenetre, text=" 🔙 Retrouner sur le menu principal ", command=retun_menu_principal).grid(row=11, column=1)

    fenetre.mainloop()

# MODIFICATION d'un sujet   -----------------------------------------------------------------------------------------------------------
def modify_movie():
    fenetre = Tk()
    fenetre.title("Modification d'un film")
    fenetre.geometry("1500x440")
    fenetre.minsize(1500,440)
    fenetre.grid_columnconfigure(0, weight=1)
    fenetre.grid_columnconfigure(1, weight=1)
    fenetre.grid_columnconfigure(2, weight=1)

    espace = Label(fenetre).grid(row=0, column=1)

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

    # fenêtre qui apparaît après avoir choisi le film
    def modify_element(event):
        item_id = tableau.focus()  # Get the selected item's ID
        name_movie = tableau.item(item_id, 'values')[0]  
        language = tableau.item(item_id, 'values')[1]
        parution = tableau.item(item_id, 'values')[2] 
        genre = tableau.item(item_id, 'values')[3]
        time = tableau.item(item_id, 'values')[4]
        comment = tableau.item(item_id, 'values')[6]

        # Create a dialog window for modifying the element
        dialog = Toplevel(fenetre)
        dialog.title("Modifier le film")
        
         # Add labels and entry widgets to the dialog window
        name_label = Label(dialog, text="Nom du film:")
        name_label.grid(row=0, column=0)
        name_entry = Entry(dialog, width=40)
        name_entry.grid(row=0, column=1)
        name_entry.insert(0, name_movie)
        
        langue_label = Label(dialog, text="Langue du film :")
        langue_label.grid(row=1, column=0)
        langue_entry = Entry(dialog, width=40)
        langue_entry.grid(row=1, column=1)
        langue_entry.insert(0, language)

        parution_label = Label(dialog, text="Année de parution :")
        parution_label.grid(row=3, column=0)
        parution_entry = Entry(dialog, width=40)
        parution_entry.grid(row=3, column=1)
        parution_entry.insert(0, parution)

        genre_label = Label(dialog, text="Genre du film :")
        genre_label.grid(row=4, column=0)
        genre_entry = Entry(dialog, width=40)
        genre_entry.grid(row=4, column=1)
        genre_entry.insert(0, genre)
        
        time_label = Label(dialog, text="Durée du film (..h..min):")
        time_label.grid(row=5, column=0)
        time_entry = Entry(dialog, width=40)
        time_entry.grid(row=5, column=1)
        time_entry.insert(0, time)

        comment_label = Label(dialog, text="Commentaires :")
        comment_label.grid(row=6, column=0)
        comment_entry = Entry(dialog, width=40)
        comment_entry.grid(row=6, column=1)
        comment_entry.insert(0, comment)

        # Function to save the modified values
        def save_changes():
            new_name = name_entry.get()
            new_langue = langue_entry.get()
            new_parution = parution_entry.get()
            new_genre = genre_entry.get()
            new_time = time_entry.get()
            new_comment = comment_entry.get()

            # Met à jour le tableau
            tableau.item(item_id, values=(new_name, new_langue, new_parution, new_genre, new_time, new_comment))

            # Met à jour la base de donnée
            data_envoie = bdd.data_movie(0, new_name, new_langue, new_parution, new_genre, new_time, new_comment)
            data_envoie.modif_subject(name_movie, parution, time)
            
            # Ferme la ferme fenêtre près sauvegarde
            dialog.destroy()
            messagebox.showinfo("Modification réussie", "L'élément a été modifié avec succès.")

        # Bouton sauvegarde de la modification
        save_button = Button(dialog, text="Enregistrer les modifications", command=save_changes)
        save_button.grid(row=7, column=0, columnspan=2)

     # Requête SQL pour récupérer les informations à afficher
    data.cursor.execute("SELECT id, name_movie, language, years, genre, time, finish, comment FROM movie ORDER BY name_movie ASC")
    results = data.cursor.fetchall()
    if len(results):
        for enreg in results:
            # chaque ligne n'a pas de parent, est ajoutée à la fin de la liste, utilise le champ id comme identifiant et on fournit les valeurs pour chacune des colonnes du tableau
            tableau.insert('', 'end', iid=enreg[0], values=(enreg[1], enreg[2], enreg[3], enreg[4], enreg[5], enreg[6], enreg[7]))

    tableau.bind('<Double-Button-1>', modify_element) 

    espace = Label(fenetre).grid(row=10, column=3)

    def retun_menu_principal():
        fenetre.destroy()
    quit = Button(fenetre, text=" 🔙 Retrouner sur le menu principal ", command=retun_menu_principal).grid(row=11, column=1)

    fenetre.mainloop()

# SUPPRESSION d'un sujet   -----------------------------------------------------------------------------------------------------------
def del_subject() : 
    fenetre = Tk()
    fenetre.title("Modification d'un sujet")
    fenetre.geometry("1500x440")
    fenetre.minsize(1500,440)
    fenetre.grid_columnconfigure(0, weight=1)
    fenetre.grid_columnconfigure(1, weight=1)
    fenetre.grid_columnconfigure(2, weight=1)

    espace = Label(fenetre).grid(row=0, column=1)

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

    def del_element(event):
        item_id = tableau.focus()  # Get the selected item's ID
        name_movie = tableau.item(item_id, 'values')[0] 
        years = tableau.item(item_id, 'values')[2]  
        time = tableau.item(item_id, 'values')[4]  
        
        # Create a dialog window for modifying the element
        dialog = Toplevel(fenetre)
        dialog.title("Modifier l'élément")

        dialog.title("Confirmation de suppression")
        name_subject = Label(dialog, text=" Etes-vous sûre de vouloir supprimer le sujet ? ").grid(row=1, column=1)
        name_subject = Label(dialog, text=" La supression est irréversible. ").grid(row=2, column=1)

        
        def verify_del():
            # Met à jour le tableau
            tableau.delete(item_id)

            # Met à jour la base de donnée
            data_envoie = bdd.data_movie(0, name_movie, years, time)
            data_envoie.del_subject(name_movie, years, time)
            
            # Ferme la ferme fenêtre près sauvegarde
            dialog.destroy()
            messagebox.showinfo("Suppression réussie", "L'élément a été supprimé avec succès.")

        # Bouton sauvegarde de la modification
        save_button = Button(dialog, text="Supprimer", command=verify_del)
        save_button.grid(row=3, column=0, columnspan=2)

     # Requête SQL pour récupérer les informations à afficher
    data.cursor.execute("SELECT id, name_movie, language, years, genre, time, finish, comment FROM movie ORDER BY name_movie ASC")
    results = data.cursor.fetchall()
    if len(results):
        for enreg in results:
            # chaque ligne n'a pas de parent, est ajoutée à la fin de la liste, utilise le champ id comme identifiant et on fournit les valeurs pour chacune des colonnes du tableau
            tableau.insert('', 'end', iid=enreg[0], values=(enreg[1], enreg[2], enreg[3], enreg[4], enreg[5], enreg[6], enreg[7]))

    tableau.bind('<Double-Button-1>', del_element) 

    espace = Label(fenetre).grid(row=10, column=3)

    def retun_menu_principal():
        fenetre.destroy()
    quit = Button(fenetre, text=" 🔙 Retrouner sur le menu principal ", command=retun_menu_principal).grid(row=11, column=1)
    
    fenetre.mainloop()