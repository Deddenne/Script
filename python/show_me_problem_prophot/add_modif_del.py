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
data = bdd.data_subject()

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
        data_envoie = bdd.data_subject(0,sujet,destination)
        data_envoie.add_sujbect()

    # Ajoute un bouton de validation
    button_valide = Button(fenetre, text="  Valider et créer le sujet ✓  ", command=get_subject_info)
    button_valide.grid(row=9, column=3)
    fenetre.mainloop()

# MODIFICATION d'un sujet   -----------------------------------------------------------------------------------------------------------
def modify_subject():
    fenetre = Tk()
    fenetre.title("Modification d'un sujet")
    fenetre.geometry("900x440")
    fenetre.minsize(900,440)
    fenetre.grid_columnconfigure(0, weight=1)
    fenetre.grid_columnconfigure(1, weight=1)
    fenetre.grid_columnconfigure(2, weight=1)

    espace = Label(fenetre).grid(row=0, column=1)

    #tableau
    tableau = Treeview(fenetre, columns=('Sujet', 'Destination'), height=15)
    tableau.heading('Sujet', text='Sujet')
    tableau.heading('Destination', text='Destination')
    tableau.column("#1", minwidth=0, width=350, stretch=NO)
    tableau.column("#2", minwidth=0, width=400, stretch=NO)
    tableau['show'] = 'headings' # sans ceci, il y avait une colonne vide à gauche qui a pour rôle d'afficher le paramètre "text" qui peut être spécifié lors du insert
    tableau.grid(row=2, column=1)

    def modify_element(event):
        item_id = tableau.focus()  # Get the selected item's ID
        sujet = tableau.item(item_id, 'values')[0]  # Get the sujet value
        destination = tableau.item(item_id, 'values')[1]  # Get the destination value
        
        # Create a dialog window for modifying the element
        dialog = Toplevel(fenetre)
        dialog.title("Modifier l'élément")
        
         # Add labels and entry widgets to the dialog window
        sujet_label = Label(dialog, text="Sujet:")
        sujet_label.grid(row=0, column=0)
        sujet_entry = Entry(dialog, width=40)
        sujet_entry.grid(row=0, column=1)
        sujet_entry.insert(0, sujet)
        
        destination_label = Label(dialog, text="Destination:")
        destination_label.grid(row=1, column=0)
        destination_entry = Entry(dialog, width=40)
        destination_entry.grid(row=1, column=1)
        destination_entry.insert(0, destination)
        

        # Function to save the modified values
        def save_changes():
            new_sujet = sujet_entry.get()
            new_destination = destination_entry.get()

            # Met à jour le tableau
            tableau.item(item_id, values=(new_sujet, new_destination))

            # Met à jour la base de donnée
            data_envoie = bdd.data_subject(0, new_sujet, new_destination)
            data_envoie.modif_subject(sujet, destination)
            
            # Ferme la ferme fenêtre près sauvegarde
            dialog.destroy()
            messagebox.showinfo("Modification réussie", "L'élément a été modifié avec succès.")

        # Bouton sauvegarde de la modification
        save_button = Button(dialog, text="Enregistrer les modifications", command=save_changes)
        save_button.grid(row=2, column=0, columnspan=2)

    # Requête SQL pour récupérer les informations à afficher
    data.cursor.execute("SELECT id_sujet, sujet, destination FROM info_sujet")
    results = data.cursor.fetchall()
    if len(results):
        for enreg in results:
            # chaque ligne n'a pas de parent, est ajoutée à la fin de la liste, utilise le champ id comme identifiant et on fournit les valeurs pour chacune des colonnes du tableau
            tableau.insert('', 'end', iid=enreg[0], values=(enreg[1], enreg[2]))

    tableau.bind('<Double-Button-1>', modify_element) 
    fenetre.mainloop()

# SUPPRESSION d'un sujet   -----------------------------------------------------------------------------------------------------------
def del_subject() : 
    fenetre = Tk()
    fenetre.title("Modification d'un sujet")
    fenetre.geometry("900x440")
    fenetre.minsize(900,440)
    fenetre.grid_columnconfigure(0, weight=1)
    fenetre.grid_columnconfigure(1, weight=1)
    fenetre.grid_columnconfigure(2, weight=1)

    espace = Label(fenetre).grid(row=0, column=1)

    #tableau
    tableau = Treeview(fenetre, columns=('Sujet', 'Destination'), height=15)
    tableau.heading('Sujet', text='Sujet')
    tableau.heading('Destination', text='Destination')
    tableau.column("#1", minwidth=0, width=350, stretch=NO)
    tableau.column("#2", minwidth=0, width=400, stretch=NO)
    tableau['show'] = 'headings' # sans ceci, il y avait une colonne vide à gauche qui a pour rôle d'afficher le paramètre "text" qui peut être spécifié lors du insert
    tableau.grid(row=2, column=1)

    def modify_element(event):
        item_id = tableau.focus()  # Get the selected item's ID
        sujet = tableau.item(item_id, 'values')[0]  # Get the sujet value
        destination = tableau.item(item_id, 'values')[1]  # Get the destination value

        # Function to save the modified values
        def save_changes():
            new_sujet = sujet_entry.get()
            new_destination = destination_entry.get()

            # Met à jour le tableau
            tableau.item(item_id, values=(new_sujet, new_destination))

            # Met à jour la base de donnée
            data_envoie = bdd.data_subject(0, new_sujet, new_destination)
            data_envoie.modif_subject(sujet, destination)



    # Requête SQL pour récupérer les informations à afficher
    data.cursor.execute("SELECT id_sujet, sujet, destination FROM info_sujet")
    results = data.cursor.fetchall()
    if len(results):
        for enreg in results:
            # chaque ligne n'a pas de parent, est ajoutée à la fin de la liste, utilise le champ id comme identifiant et on fournit les valeurs pour chacune des colonnes du tableau
            tableau.insert('', 'end', iid=enreg[0], values=(enreg[1], enreg[2]))

    tableau.bind('<Double-Button-1>', modify_element) 
    fenetre.mainloop()

del_subject()