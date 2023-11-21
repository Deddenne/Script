# Import des modules après installation
from install_requirements import install_requirements  # Importez la fonction install_requirements du fichier install_requirements.py
from datetime import datetime  # Importer le module datetime - Ajouter l'heure de la capture
import threading  # Importer le module threading - lancer des processus
from scapy.all import *  # Importer le module scapy.all - capturer les paquets en python
import tkinter as tk                # Importer le module tkinter - graphique python
from tkinter import ttk             # Importer le module ttk depuis tkinter - graphique python
from tkinter import messagebox      # Importer le module messagebox depuis tkinter - graphique python - popup
from tkinter import Menu            # Importer le module tkinter - graphique python - popup
from tkinter import filedialog      
from tkinter import simpledialog
import json                         # Importer le module json - traiter des fichiers JSON
import os
import platform
import re                           # Importer le module re - utiliser une expression réculière - recherche dans une chaine 

# -------------------------- INSTALLATION -------------------------

install_requirements()

# -------------------------- FONCTIONS -------------------------

# Variables pour contrôler la capture
capture_active = False
capture_paused = False
# Créer un objet Event pour coordonner le démarrage et l'arrêt de la capture
capture_event = threading.Event()

# Fonction configuration de l'interface
def configure_interface(state_text, background_color, start_state, stop_state, pause_resume_text, pause_resume_state, resume_state, pause_state, bsearch_state, search_state):
    status_color_label["text"] = state_text
    status_color_label["background"] = background_color
    start_button.config(state=start_state)
    search_button.config(state=bsearch_state)
    stop_button.config(state=stop_state)
    pause_resume_button.config(text=pause_resume_text, state=pause_resume_state)
    file_menu.entryconfigure("Recherche", state=search_state)
    file_menu2.entryconfigure("Reprise", state=resume_state)
    file_menu2.entryconfigure("Pause", state=pause_state)

# Fonction pour mettre à jour le texte des options sélectionnées
def update_selected_options_text():
    selected_options = [option for option, var in zip(["UDP", "TCP", "DNS", "ICMP", "HTTPS", "HTTP"], [udp_var, tcp_var, dns_var, icmp_var, https_var, http_var])]
    selected_options = [option for option, var in zip(selected_options, [udp_var, tcp_var, dns_var, icmp_var, https_var, http_var]) if var.get()]
    selected_options_text.set("Options sélectionnées: " + ", ".join(selected_options))

# Fonction pour mettre à jour l'étiquette d'état
def update_status_label():
    if capture_active and not capture_paused:
        configure_interface("En cours", "green", "disabled", "enabled", "Pause", "enabled", "disabled", "normal", "disabled", "disabled")
    elif capture_active and capture_paused:
        configure_interface("En Pause", "yellow", "disabled", "enabled", "Reprise", "enabled", "normal", "disabled", "enabled","normal")
    else:
        configure_interface("Arrêtée", "red", "enabled", "disabled" ,"Pause", "disabled", "disabled", "disabled", "enabled", "normal")

    # Désactiver les cases à cocher si la capture est active
    specific_ports_checkbox.config(state="disabled" if capture_active else "normal")
    # Désactiver les ports input si la capture est active
    specific_ports_entry.config(state="disabled" if capture_active else "normal")
    # Désactiver l'interface réseau si la capture est active
    interface_combobox.config(state="disabled" if capture_active else "normal")

# Fonction créer les trames à afficher
def trame(packet_id, current_time, packet): 
    trame_packet= f"{packet_id} - {current_time} - {str(packet)}\n"
    packet_text.insert(tk.END, trame_packet)
    scroll_to_end()  # Faites défiler vers la fin

# Fonction pour vérifier quelles sont les cases cochées
def verify_checkbox(valeurs, informations):
    informations_recuperees = []
    for index, valeur in enumerate(valeurs):
        if valeur:  # Vérifie si la valeur est vraie
            if index < len(informations):  # Vérifie si l'index est dans la plage des informations
                informations_recuperees.append(informations[index])  # Récupère l'information correspondante
            else:
                informations_recuperees.append(None)  # Si l'index dépasse la plage des informations, ajoute None
    return informations_recuperees

# Fonction pour capturer les paquets
def capture_packets(interface, capture_event, capture_tcp, capture_udp, capture_dns, capture_icmp, capture_https, capture_http, capture_specific_ports):
    global capture_paused
    packet_id = 1  # Initialisation de l'identifiant
    # Boucle principale de capture des paquets si le capture event n'est pas activé
    while not capture_event.is_set():
        try:
            capture_event.wait(0.5)  # Attendre 0.5 seconde pour permettre la vérification de l'événement
            # Faire une boucle si la capture est en pause
            while capture_paused:
                time.sleep(0.1)
            # Vérifier si la capture n'est pas en pause
            if not capture_paused:
                packets = sniff(iface=interface, count=1)  # Capture 1 paquet à la fois
                print ("packets : ", packets)
                for packet in packets:
                    # Obtenir la date et l'heure actuelles
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    # Créer une trame identifiant - temps - packet 
                    trame_packet = ""
                    found_ports = ""
                    
                    # Vérifier si les cases protocoles cochées sont True ou False
                    valeurs_a_verifier = [capture_tcp, capture_udp, capture_dns, capture_icmp, capture_https, capture_http]
                    informations_disponibles = ["TCP", "UDP", "DNS", "ICMP", "HTTPS", "HTTP"]
                    # Vérifier et filtrer les paquets en fonction des options sélectionnées
                    resultat = verify_checkbox(valeurs_a_verifier, informations_disponibles)
                    protocol_packet = packet.summary().split()[4]
                    if capture_specific_ports : 
                        # condition ports 
                        ports_entry = specific_ports_entry.get()
                        # Trier les ports
                        all_ports_shorted = ports_sorted(ports_entry)
                        # Vérification des ports capturé dans la liste des ports spécifiques récupérés
                        if ((str(packet.sport) in all_ports_shorted or str(packet.dport) in all_ports_shorted) and (protocol_packet in resultat)) : 
                            trame(packet_id, current_time, packet)
                            packet_id += 1
                    else :
                        if protocol_packet in resultat:
                            trame(packet_id, current_time, packet)
                            packet_id += 1
        # Afficher une boîte de dialogue d'erreur en cas d'exception
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

# Fonction pour trier les ports
def ports_sorted(donnees):
    elements = donnees.split(',')
    nombres = []
    for element in elements:
        if '-' in element:
            start, end = map(int, element.split('-'))
            if start > end:
                messagebox.showwarning("Erreur", "Le nombre avant le tiret doit être plus petit que celui après le tiret.")
                return
            nombres.extend(range(start, end + 1))
        else:
            nombres.append(int(element))

    nombres_tries = sorted(nombres)
    # Convertir les ports en chaînes de caractères
    liste_ports_en_string = list(map(str, nombres_tries))
    return liste_ports_en_string


# Fonction pour gérer le démarrage de la capture
def start_capture():
    packet_text.delete("1.0", tk.END)
    global capture_active, capture_paused, capture_event
    interface = interface_var.get()

    # Arrêter le thread de capture précédent s'il était actif
    if capture_active:
        capture_event.set()
        capture_active = False
        update_status_label()

    # Créer un nouvel objet Event pour coordonner le démarrage et l'arrêt de la capture
    capture_event = threading.Event()

    # Vérifier si une interface a été sélectionnée
    if not interface:
        messagebox.showwarning("Interface réseau non sélectionnée", "Veuillez sélectionner une interface avant de démarrer la capture.")
        return

    # Vérifier les cases à cocher
    capture_udp = udp_var.get()
    capture_tcp = tcp_var.get()
    capture_dns = dns_var.get()
    capture_icmp = icmp_var.get()
    capture_https = https_var.get()
    capture_http = http_var.get()
    capture_specific_ports = specific_ports_var.get()
    ports_entry = specific_ports_entry.get()
    # !Vérifier si la chaîne contient un séparateur invalide
    if capture_specific_ports and re.search(r'[^,\d-]', ports_entry):
        messagebox.showwarning("Ports spécifiques", "Les données contiennent des séparateurs invalides.")
        return

    # Vérifier au moins une des cases à cocher
    if not any([capture_udp, capture_tcp, capture_dns, capture_icmp, capture_https, capture_http]) and not capture_specific_ports :
        messagebox.showwarning("Aucune option de capture sélectionnée", "Veuillez sélectionner au moins une option de capture (portocoles ou ports spécifiques) avant de démarrer la capture.")
        return

    # Marquer la capture comme active
    capture_active = True

    # Mettre à jour l'étiquette d'état
    update_status_label()

    # Créez un thread pour la capture
    capture_thread = threading.Thread(target=capture_packets, args=(interface, capture_event, capture_tcp, capture_udp, capture_dns, capture_icmp, capture_https, capture_http,capture_specific_ports))
    capture_thread.start()

# Fonction pour arrêter la capture
def stop_capture():
    global capture_active
    # Définir l'événement de capture pour indiquer l'arrêt
    capture_event.set()
    # Mettre à jour la variable global capture_active pour signaler l'arrêt
    capture_active = False
    # Mettre à jour l'étiquette d'état
    update_status_label()

# Fonction pour mettre en pause/reprendre la capture
def pause_resume_capture():
    global capture_paused
    # Vérifier si la capture est active avant de mettre en pause ou de reprendre
    if capture_active:
         # Inverser l'état de la variable capture_paused (passer de True à False ou vice versa)
        capture_paused = not capture_paused
        # Mettre à jour l'étiquette d'état pour refléter l'état actuel de la capture
        update_status_label()

# Fonction pour toujours voir la dernière trame
def scroll_to_end():
    packet_text.see("end")

# Fonction pour enregistrer la capture dans un fichier TXT
def save_capture_to_file_txt():
    # Vérifier si la zone de texte est vide
    lines = packet_text.get("1.0", tk.END).splitlines()
    if len(lines) == 1:
        messagebox.showwarning("Aucune donnée", "Il n'y a pas de données à enregistrer.")
        return
    current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"capture_{current_date}.txt"
    with open(filename, "w") as file:
        text_to_save = packet_text.get("1.0", tk.END)
        file.write(text_to_save)
    messagebox.showinfo("Enregistrement réussi", f"La capture a été enregistrée avec succès dans le fichier '{filename}'.")

# Fonction pour enregistrer la capture dans un fichier JSON
def save_capture_to_file_json():
    # Vérifier si la zone de texte est vide
    lines = packet_text.get("1.0", tk.END).splitlines()
    if len(lines) == 1:
        messagebox.showwarning("Aucune donnée", "Il n'y a pas de données à enregistrer.")
        return
    current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"capture_{current_date}.json"

    # Créez une liste pour stocker les paquets capturés sous forme de dictionnaires
    captured_packets = []
    for line in packet_text.get("1.0", tk.END).splitlines():
        parts = line.split(" - ")
        if len(parts) == 3:
            packet_id, current_time, packet_data = parts
            captured_packets.append({
                "packet_id": packet_id,
                "timestamp": current_time,
                "interface": interface_var.get(),
                "packet_data": packet_data
            })
    # Écrivez la liste des paquets capturés dans un fichier JSON
    with open(filename, "w") as file:
        json.dump(captured_packets, file, indent=4)
    messagebox.showinfo("Enregistrement réussi", f"La capture a été enregistrée avec succès dans le fichier '{filename}' en format JSON.")

# Formatte les données JSON pour les afficher de la même manière que le fichier texte.
def format_json_data(json_data):
    # Initialisation de la lsite
    formatted_data = ""
    # Parcours le JSON et ajoute les objets dans une seule ligne puis dans une liste
    for packet in json_data:
        formatted_data += f"{packet['packet_id']} - {packet['timestamp']} - {packet['packet_data']}\n"

    return formatted_data

# Ouvre et affiche le contenu d'un fichier en fonction de son format
def open_and_display_file(format):
    # Si le format est en TXT
    if format == ".txt": 
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers texte", "*.txt")])
        # Vérifier que le fichier ne soit pas vide et commande par capture_
        if file_path and os.path.basename(file_path).startswith("capture_"):
            with open(file_path, 'r') as file:
                file_content = file.read() # Récupère le contenu
                packet_text.delete("1.0", tk.END)  # Effacer le contenu actuel de la zone de texte
                packet_text.insert(tk.END, file_content)  # Insérer le contenu du fichier dans la zone de texte
        else:
            # Message d'erreur si le fichier ne correspond pas aux enregistrements
            messagebox.showwarning("Erreur", "Ce fichier n'est pas pris en charge.")
    elif format == ".json":
        # Vérifier que le fichier ne soit pas vide et commande par capture_
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers JSON", "*.json")])
        if file_path and os.path.basename(file_path).startswith("capture_"):
            with open(file_path, 'r') as file:
                json_data = json.load(file) # Récupère le contenu de type json
                file_content = format_json_data(json_data) # Utilise la function pour convertir
                packet_text.delete("1.0", tk.END)  # Effacer le contenu actuel de la zone de texte
                packet_text.insert(tk.END, file_content)  # Insérer le contenu du fichier dans la zone de texte
        else:
            # Message d'erreur si le fichier ne correspond pas aux enregistrements
            messagebox.showwarning("Erreur", "Ce fichier n'est pas pris en charge.")
    else:
        messagebox.showwarning("Erreur", "Ce format n'est pas pris en charge.")

# Fonction de recherche
def search_packets():
    if capture_active and not capture_paused:
        messagebox.showwarning("Fonctionnalité indisponible", "La fonction de recherche n'est pas disponible pendant la capture.")
        return
    # Obtenir le texte actuel de la zone de texte
    current_text = packet_text.get("1.0", tk.END)
    if len(current_text) < 1:
        messagebox.showwarning("Recherche impossible", "Aucune donnée d'affichée.")
        return
    # Ouverture d'une fenêtre de dialogue
    search_term = simpledialog.askstring("Recherche", "Entrez le terme de recherche:")
    if search_term :
        # Diviser le texte en lignes
        lines = current_text.splitlines()
        # Filtrer les lignes qui contiennent le terme de recherche
        filtered_lines = [line for line in lines if search_term in line]
        # Mettre à jour la zone de texte avec les lignes filtrées
        packet_text.delete("1.0", tk.END)
        packet_text.insert(tk.END, "\n".join(filtered_lines))
        packet_text.insert(tk.END, "\n")
        # Afficher un message si aucune correspondance n'est trouvée
        if not filtered_lines:
            messagebox.showinfo("Résultats de la recherche", "Aucune correspondance trouvée.")
    else:
        messagebox.showwarning("Aucun Mot-Clé", "Merci de bien vouloir saisir une donnée.")

# Quitter et demander si enregistrer
def confirm_quit():
    # Obtenir les lignes de texte dans la zone de texte
    lines = packet_text.get("1.0", tk.END).splitlines()
     # Vérifier s'il y a des données dans la zone de texte
    if len(lines) == 1:
        # Demander confirmation pour quitter s'il n'y a pas de données
        confirm_quit = messagebox.askyesnocancel("Confirmation", "Voulez-vous vraiment quitter?")
        # Si la confirmation est affirmative, détruire la fenêtre et quitter l'application
        if confirm_quit:
            window.destroy()
            os._exit(0)
    else:
        # Si des données sont présentes, demander si l'utilisateur veut enregistrer avant de quitter
        confirm = messagebox.askyesnocancel("Confirmation", "Voulez-vous enregistrer la capture avant de quitter?")
        # Si l'utilisateur choisit d'enregistrer, appeler la fonction pour sauvegarder en format JSON
        if confirm:
            save_capture_to_file_json()
            # Marquer l'événement de capture comme défini (True) pour indiquer l'arrêt de la capture
            capture_event.set()
            # Détruire la fenêtre et quitter l'application
            window.destroy()
            os._exit(0)
        # Si l'utilisateur choisit de ne pas enregistrer, quitter sans sauvegarder
        if confirm is not None:
            # Marquer l'événement de capture comme défini (True) pour indiquer l'arrêt de la capture
            capture_event.set()
            # Détruire la fenêtre et quitter l'application
            window.destroy()
            os._exit(0)

# Fonction pour afficher la fenêtre "À propos de"
def show_about_info():
    python_version = platform.python_version()

    about_info = (
        f"Version: 1.0\n"
        f"Date: Novembre 2023 \n"
        f"Python: {python_version}\n"
        f"Auteurs: CAPPELIEZ, DUPONT, LIN\n"
        f"MIT : ESGI"
    )

    # Afficher une boîte de dialogue avec les informations
    messagebox.showinfo("À propos de", about_info)


# ---------------- CREATION FENETRE TKINTER -------------------------

# Création de la fenêtre principale
window = tk.Tk()
# Nom de la fenêtre
window.title("Whireshark")
# Taille initiale de la fenêtre 
window.geometry("700x660")
# Taille minimal de la fenêtre
window.minsize(700, 660)

# configurer 3 colonnes pour centrer les textes
for i in range(3):
    window.grid_columnconfigure(i, weight=1)

# Créer un objet Menu
menu_bar = Menu(window)

# Créer le menu Fichier
file_menu = Menu(menu_bar, tearoff=0)

# Créer le sous-menu pour ouvrir en TXT ou JSON
file_menu_ouvrir = Menu(file_menu, tearoff=0)
file_menu.add_cascade(label="Ouvrir", menu=file_menu_ouvrir)
file_menu_ouvrir.add_command(label="Fichier en TXT", command=lambda: open_and_display_file(".txt"))
file_menu_ouvrir.add_command(label="Fichier en JSON", command=lambda: open_and_display_file(".json"))

# Ajouter l'option pour rechercher au menu principal
file_menu.add_command(label="Recherche", command=search_packets)

# Créer le sous-menu pour sauvegarder en TXT ou JSON
file_menu_sauvegarder = Menu(file_menu, tearoff=0)
file_menu.add_cascade(label="Sauvegarder", menu=file_menu_sauvegarder)
file_menu_sauvegarder.add_command(label="Enregistrer en TXT", command=save_capture_to_file_txt)
file_menu_sauvegarder.add_command(label="Enregistrer en JSON", command=save_capture_to_file_json)

# Ajouter l'option pour quitter au menu principal
file_menu.add_command(label="Quitter", command=confirm_quit)

# Créer le menu Capture
file_menu2 = Menu(menu_bar, tearoff=0)
file_menu2.add_command(label="Démarrer", command=start_capture)
file_menu2.add_command(label="Arrêter", command=stop_capture)
file_menu2.add_command(label="Pause", command=pause_resume_capture, state="disabled")
file_menu2.add_command(label="Reprise", command=pause_resume_capture, state="disabled")

# Initialisation des variables pour les cases à cocher
udp_var = tk.BooleanVar(value=True)
tcp_var = tk.BooleanVar(value=True)
dns_var = tk.BooleanVar(value=True)
icmp_var = tk.BooleanVar(value=True)
https_var = tk.BooleanVar(value=True)
http_var = tk.BooleanVar(value=True)

# Créer le menu Options
file_menu3 = Menu(menu_bar, tearoff=0)
# Ajouter les cases à cocher UDP et TCP dans le menu Options
file_menu3.add_checkbutton(label="Capture UDP", variable=udp_var, command=update_selected_options_text)
file_menu3.add_checkbutton(label="Capture TCP", variable=tcp_var, command=update_selected_options_text)
file_menu3.add_checkbutton(label="Capture DNS", variable=dns_var, command=update_selected_options_text)
file_menu3.add_checkbutton(label="Capture ICMP", variable=icmp_var, command=update_selected_options_text)
file_menu3.add_checkbutton(label="Capture HTTP", variable=https_var, command=update_selected_options_text)
file_menu3.add_checkbutton(label="Capture HTTPS", variable=http_var, command=update_selected_options_text)

# Créer le menu Aider
file_menu4 = Menu(menu_bar, tearoff=0)
# Ajouter "A propos de"
file_menu4.add_command(label="A propos de", command=show_about_info)

# Ajouter les menus à la barre de menu
menu_bar.add_cascade(label="Fichier", menu=file_menu)
menu_bar.add_cascade(label="Capture", menu=file_menu2)
menu_bar.add_cascade(label="Options", menu=file_menu3)
menu_bar.add_cascade(label="Aide", menu=file_menu4)

# Configurer la fenêtre pour utiliser la barre de menu
window.config(menu=menu_bar)

# Création d'une étiquette pour l'interface réseau
interface_label = ttk.Label(window, text="Interface réseau")
interface_label.grid(row=3, column=0)

# Sélection de l'interface réseau
available_interfaces = [iface for iface in get_if_list()]
interface_var = tk.StringVar()
interface_combobox = ttk.Combobox(window, textvariable=interface_var, values=available_interfaces)
interface_combobox.grid(row=4, column=0)

# Bouton de recherche
search_button = ttk.Button(window, text="Rechercher", command=search_packets)
search_button.grid(row=4, column=1) 

specific_ports_var = tk.BooleanVar()
specific_ports_checkbox = tk.Checkbutton(window, text="Ports spécifiques", variable=specific_ports_var)
specific_ports_checkbox.grid(row=3, column=2)

# Entry pour les ports spécifiques avec un exemple
example_ports_text = "Example : 0,130,450"
specific_ports_entry = tk.Entry(window, width=20)
specific_ports_entry.insert(0, example_ports_text)  # Insérer l'exemple dans l'Entry
specific_ports_entry.grid(row=4, column=2)

# Espace
espace = ttk.Label(window).grid(row=5, column=1)

# Créer une variable pour stocker les options sélectionnées
selected_options_text = tk.StringVar(value="Options sélectionnées: ")
selected_options_label = ttk.Label(window, textvariable=selected_options_text)
selected_options_label.grid(row=6, column=0, columnspan=3)
# Appel initial pour mettre à jour le texte des options sélectionnées
update_selected_options_text()

# Espace
espace = ttk.Label(window).grid(row=7, column=1)

# Bouton pour lancer la capture
start_button = ttk.Button(window, text="Démarrer", command=start_capture)
start_button.grid(row=8, column=0, padx=1, pady=1)

# Bouton pour arrêter la capture
stop_button = ttk.Button(window, text="Arrêter la capture", state="disabled", command=stop_capture)
stop_button.grid(row=8, column=2, padx=1, pady=1)

# Bouton pour mettre en pause/reprendre la capture
pause_resume_button = ttk.Button(window, text="Pause", state="disabled", command=pause_resume_capture)
pause_resume_button.grid(row=8, column=1, padx=1, pady=1)

# Espace
espace = ttk.Label(window).grid(row=13, column=1)

# Création du cadre pour le label d'état
status_frame = ttk.Frame(window, relief="groove", padding=(10, 5))
status_frame.grid(row=14, column=1, padx=10, pady=10)

# Label d'état (texte)
status_text_label = ttk.Label(status_frame, text="Capture")
status_text_label.grid(row=0, column=0)

# Label d'état (indicateur de couleur)
status_color_label = ttk.Label(status_frame, text="Arrêtée", background="red")
status_color_label.grid(row=1, column=0)

# Espace
espace = ttk.Label(window).grid(row=15, column=1)

# Zone de texte pour afficher les paquets capturés
packet_text = tk.Text(window, font=("Helvetica", 10))
packet_text.grid(row=16, columnspan=3, sticky="nsew")  # columnspan : prendre la place sur les 3 colonnes ; sticky : étirer sur toutes les colonnes

# Barre de défilement verticale
scrollbar = ttk.Scrollbar(window, command=packet_text.yview)
scrollbar.grid(row=16, column=3, sticky="ns")  # Associer la barre de défilement à la zone de texte

# Configurer la zone de texte pour utiliser la barre de défilement
packet_text.config(yscrollcommand=scrollbar.set)

# Espace
espace = ttk.Label(window).grid(row=17, column=1)

# Bouton pour enregistrer la capture dans un fichier texte
save_button = ttk.Button(window, text="Quitter", command=confirm_quit)
save_button.grid(row=18, column=1, padx=1, pady=1)

# Point d'entrée principal du script
if __name__ == '__main__':
# Lancer la boucle de l'interface graphique
    window.mainloop()
