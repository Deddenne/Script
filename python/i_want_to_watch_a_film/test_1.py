import tkinter as tk


# Créer la fenêtre principale
root = tk.Tk()
root.title("Choix Oui/Non")

# Variable de contrôle pour les Radiobuttons
choix = tk.IntVar()

# Créer les Radiobuttons "Oui" et "Non"
oui_radio = tk.Radiobutton(root, text="Oui", variable=choix, value=1)
non_radio = tk.Radiobutton(root, text="Non", variable=choix, value=2)

# Placer les Radiobuttons dans la grille (grid)
oui_radio.grid(row=0, column=0, padx=10, pady=5)
non_radio.grid(row=0, column=1, padx=10, pady=5)


def on_envoyer_click():
    # Vérifier quelle option a été sélectionnée
    if choix.get() == 1:
        finish = '✔'
        print("Vous avez choisi 'Oui'. finish : ",finish )
    elif choix.get() == 2:
        finish = ''
        print("Vous avez choisi 'Non'. finish : ",finish )

    # Récupérer la réponse de l'utilisateur pour le film

# Créer le bouton "Envoyer"
bouton_envoyer = tk.Button(root, text="Envoyer", command=on_envoyer_click)
bouton_envoyer.grid(row=9, column=0, columnspan=2, pady=10)




# Lancer la boucle principale de l'interface graphique
root.mainloop()
