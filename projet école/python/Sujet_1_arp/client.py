import socket
import time
import tkinter as tk
import sys

# Classe pour récupérer les sorties du terminale serveur et ajouter la fenetre
class ServerOutputWindow(tk.Toplevel):
    def __init__(self, master, window_title="Sortie du Serveur"):
        super().__init__(master)
        self.title(window_title)  # Définit le titre de la fenêtre

        # Crée un widget de texte pour afficher le contenu
        self.output_text = tk.Text(self, wrap=tk.WORD, state=tk.DISABLED)
        self.output_text.grid(row=0, column=0, sticky="nsew")  # Place le widget de texte dans la grille de la fenêtre

        # Ajoute un bouton "Fermer" en bas de la fenêtre
        close_button = tk.Button(self, text="Fermer", command=self.destroy)
        close_button.grid(row=1, column=0, sticky="ew")  # Place le bouton dans la grille, s'étend horizontalement

        # Configure la gestion de grille pour que la ligne 0 (contenant le texte) s'étende, 
        # mais la ligne 1 (contenant le bouton) ait une taille fixe
        self.grid_rowconfigure(0, weight=1)  # Le texte s'étend verticalement
        self.grid_rowconfigure(1, weight=0)  # Le bouton a une taille fixe
        self.grid_columnconfigure(0, weight=1)  # La colonne 0 s'étend horizontalement

        self.geometry("400x200")  # Définit la taille initiale de la fenêtre

    def update_output(self, text):
        # Met à jour le texte affiché dans le widget de texte
        self.output_text.config(state="normal")
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, text)
        self.output_text.config(state="disabled")
        self.output_text.see(tk.END)  # Fait défiler la fenêtre vers le bas pour afficher les nouveaux messages
        
        # Ajuste automatiquement la taille de la fenêtre en fonction du nombre de lignes de texte
        num_lines = int(self.output_text.index(tk.END).split('.')[0])
        self.geometry("400x" + str(num_lines * 20 + 200))  # Calcul de la nouvelle hauteur en fonction du texte

# Fonction qui crée la fenetre de connexion
def create_main_window():
    # Crée une instance de la classe Tk, qui représente la fenêtre principale de l'application
    root = tk.Tk()
    root.title("Boite à Outils")  # Définit le titre de la fenêtre

    # Crée un libellé pour afficher "Adresse IP du serveur :" dans la fenêtre
    label_host = tk.Label(root, text="Adresse IP du serveur :")
    label_host.grid(row=0, column=0, padx=10, pady=10)  # Place le libellé dans la grille à la position (0, 0)

    # Crée un champ de saisie pour l'adresse IP du serveur
    entry_host = tk.Entry(root, width=30)
    entry_host.grid(row=0, column=1, padx=10, pady=10)  # Place le champ de saisie dans la grille à la position (0, 1)

    # Crée un libellé pour afficher "Numéro de port du serveur :" dans la fenêtre
    label_port = tk.Label(root, text="Numéro de port du serveur :")
    label_port.grid(row=1, column=0, padx=10, pady=10)  # Place le libellé dans la grille à la position (1, 0)

    # Crée un champ de saisie pour le numéro de port du serveur
    entry_port = tk.Entry(root, width=30)
    entry_port.grid(row=1, column=1, padx=10, pady=10)  # Place le champ de saisie dans la grille à la position (1, 1)

    # Crée un bouton "Se connecter" qui appelle la fonction connect_to_server lorsque cliqué
    button_connect = tk.Button(root, text="Se connecter", command=lambda: connect_to_server(root, entry_host, entry_port))
    button_connect.grid(row=2, column=0, padx=10, pady=10)  # Place le bouton dans la grille à la position (2, 0)

    # Crée un bouton "Quitter" qui ferme la fenêtre et quitte l'application lorsque cliqué
    button_quit = tk.Button(root, text="Quitter", command=lambda: [root.destroy(), sys.exit()])
    button_quit.grid(row=2, column=1, padx=10, pady=10)  # Place le bouton dans la grille à la position (2, 1)

    return root  # Renvoie l'instance de la fenêtre principale pour pouvoir l'utiliser dans le reste du programme

# Fonction qui génére le fenetre de connexion en cours
def display_connection(root, mySocket):
    message_window = tk.Toplevel(root)
    message_window.title("Connexion réussie")
    message_label = tk.Label(message_window, text="La connexion a été établie avec succès. En cours de connexion...")
    message_label.pack(padx=10, pady=10)
    # Fermer la fenêtre de message après 2 secondes et afficher le display_menu
    message_window.after(2000, lambda: [message_window.destroy(), display_menu(root, mySocket)])

# Fonction qui génère la fenetre de choix
def display_menu(root, mySocket):
    root.withdraw()  # Cache la fenêtre principale pour afficher la fenêtre de choix
    menu_window = tk.Toplevel()  # Crée une nouvelle fenêtre enfant (fenêtre de choix)
    menu_window.title("Boite à Outils")  # Définit le titre de la fenêtre de choix

    # Définit une fonction de rappel pour gérer la fermeture de la fenêtre de choix
    menu_window.protocol("WM_DELETE_WINDOW", lambda: on_quit(root, mySocket))

    # Crée des boutons pour chaque option de menu avec des étiquettes et des commandes associées
    button_ip_config = tk.Button(menu_window, text="Configuration IP", command=lambda: send_to_server("1", mySocket, root, "Configuration IP"))
    button_ip_config.grid(row=0, column=0, padx=10, pady=10)

    button_network_latency = tk.Button(menu_window, text="Latence réseau", command=lambda: send_to_server("2", mySocket, root, "Latence réseau"))
    button_network_latency.grid(row=1, column=0, padx=10, pady=10)

    button_arp_table = tk.Button(menu_window, text="Table ARP", command=lambda: send_to_server("3", mySocket, root, "Table ARP"))
    button_arp_table.grid(row=2, column=0, padx=10, pady=10)

    button_active_connections = tk.Button(menu_window, text="Connexions en cours", command=lambda: send_to_server("4", mySocket, root, "Connexions en cours"))
    button_active_connections.grid(row=3, column=0, padx=10, pady=10)

    button_bandwidth_usage = tk.Button(menu_window, text="Utilisation de la bande passante", command=lambda: send_to_server("5", mySocket, root, "Utilisation de la bande passante"))
    button_bandwidth_usage.grid(row=4, column=0, padx=10, pady=10)

    button_machine_info = tk.Button(menu_window, text="Informations physique de la machine", command=lambda: send_to_server("6", mySocket, root, "Informations physique de la machine"))
    button_machine_info.grid(row=5, column=0, padx=10, pady=10)

    # Crée un bouton "Quitter" qui appelle la fonction on_quit lorsque cliqué
    button_quit = tk.Button(menu_window, text="Quitter", command=lambda: on_quit(root, mySocket))
    button_quit.grid(row=6, column=0, padx=10, pady=10)

# Fonction pour établir la connexion avec le serveur en utilisant l'adresse IP et le numéro de port fournis par l'utilisateur
def connect_to_server(root, entry_host, entry_port):
    # Récupère l'adresse IP et le numéro de port entrés par l'utilisateur à partir des champs de saisie
    host = entry_host.get()
    port = entry_port.get()

    try:
        # Convertit le numéro de port en entier
        port = int(port)
        # Crée un objet de socket pour établir une connexion avec le serveur
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Tente de se connecter au serveur en utilisant l'adresse IP et le numéro de port spécifiés
        mySocket.connect((host, port))
        # Si la connexion est réussie, affiche la fenêtre de connexion en cours
        display_connection(root, mySocket)
    except (socket.error, ValueError) as err:
        # En cas d'erreur lors de la connexion, affiche un message d'erreur dans une nouvelle fenêtre
        error_message = tk.Toplevel(root)
        error_message.title("Erreur de connexion")
        # Crée un libellé avec le message d'erreur spécifique
        error_label = tk.Label(error_message, text=f"Erreur de connexion : {err}")
        error_label.pack(padx=10, pady=10)

# Fonction pour envoyer une commande au serveur et afficher la sortie dans une fenêtre dédiée
def send_to_server(id, mySocket, root, button_text):
    try:
        code = str(id)
        mySocket.send(code.encode("utf-8"))  # Envoie la commande au serveur encodée en UTF-8
        time.sleep(1)  # Attends pendant 1 seconde pour laisser le serveur traiter la commande
        result = mySocket.recv(1024).decode("utf-8")  # Reçoit la réponse du serveur et la décode en UTF-8
        
        if result.strip():
            # Si la réponse n'est pas vide, crée une nouvelle fenêtre de sortie dédiée avec un titre spécifique
            output_window = ServerOutputWindow(root, window_title=button_text)
            # Met à jour le contenu de la fenêtre de sortie avec la réponse du serveur
            output_window.update_output(result)
    except ConnectionRefusedError:
        # Si la connexion est refusée (serveur inaccessible), affiche un message d'erreur et quitte le programme
        print("Impossible de communiquer avec le serveur. Fermeture en cours...")
        sys.exit()

# Fonction appelée lors de la fermeture de l'application
def on_quit(root, mySocket):
    exit_command = str("!DISCONNECT")  # Définit la commande pour notifier le serveur de la déconnexion du client
    mySocket.send(exit_command.encode("utf-8"))  # Envoie la commande au serveur encodée en UTF-8
    time.sleep(1)  # Attends pendant 1 seconde pour permettre au serveur de traiter la commande
    
    result = mySocket.recv(1024).decode("utf-8")  # Reçoit la réponse du serveur et la décode en UTF-8
    print(result)  # Affiche la réponse du serveur dans la console
    
    mySocket.close()  # Ferme la connexion socket avant de quitter l'application
    root.quit()  # Quitte la boucle principale tkinter, arrêtant ainsi l'interface graphique
    root.destroy()  # Détruit la fenêtre principale tkinter pour fermer l'application graphique

# Point d'entrée principal du programme. Cela vérifie si le script est exécuté en tant que programme principal.
if __name__ == "__main__":
    # Crée la fenêtre principale de l'application en appelant la fonction create_main_window()
    root = create_main_window()
    # Lance la boucle principale de l'interface graphique tkinter, permettant à l'application de répondre aux événements
    root.mainloop()