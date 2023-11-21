import pexpect
from dotenv import load_dotenv
import os
import time
import re
import tkinter as tk
from tkinter import simpledialog, Button, Label, StringVar,Tk, messagebox
try:
    import progressbar
except BaseException:
    pass



def message_box(Text):
    root = tk.Tk()
    root.withdraw()  # Cacher la fenêtre principale pour que seule la boîte de dialogue d'erreur soit visible
    #si le Text est une liste, on le transforme en string
    if type(Text) == list:
        Text = "\n".join(Text)    
    messagebox.showerror("Erreur", Text)

def message_box_success(Text):
    root = tk.Tk()
    root.withdraw()  # Cacher la fenêtre principale pour que seule la boîte de dialogue d'erreur soit visible
    #si le Text est une liste, on le transforme en string
    if type(Text) == list:
        Text = "\n".join(Text)
    messagebox.showinfo("Succès", Text)
    

def Empty():
    print("Vous devez rempire le fichier .env avec les data manquante...")
    exit(code="Error: File Empty")


def test_sudo(ssh_session, ssh_password):
    ssh_session.sendline("echo test sudo")
    try:
        ssh_session.expect("[sudo]")
        ssh_session.sendline(ssh_password)
        ssh_session.expect("test sudo", timeout=2)
    except BaseException:
        print("You are not sudoer")
        exit(code="Error: You are not sudoer")


def test_iptables(ssh_session, ssh_password):
    ssh_session.sendline("iptables -L -n")
    try:
        ssh_session.expect("iptables", timeout=2)
    except BaseException:
        print("iptables is not working")
        exit(code="Error: iptables is not working")


def get_variable():
    purge = False
    dir_path = os.path.dirname(os.path.realpath(__file__))
    load_dotenv(dotenv_path=dir_path + '/.env')
    class ChoixReglesDialog(simpledialog.Dialog):
        def body(self, master):
            Label(master, text="Veuillez choisir l'action à effectuer:").pack()
            self.choice_var = StringVar()
            Button(master, text="Ajouter", command=self.choisir_ajouter).pack(pady=5)
            Button(master, text="Retirer", command=self.choisir_retirer).pack(pady=5)
            Button(master, text="Supprimer", command=self.choisir_supprimer).pack(pady=5)
            return None  # Retourner None à la place de self.choice_var.get()

        def apply(self):
            choice = self.choice_var.get()
            self.result = choice.lower()

        def choisir_ajouter(self):
            self.choice_var.set("Ajouter")
            self.ok()

        def choisir_retirer(self):
            self.choice_var.set("Retirer")
            self.ok()

        def choisir_supprimer(self):
            self.choice_var.set("Supprimer")
            self.ok()

    root = Tk()
    root.withdraw()
    dialog = ChoixReglesDialog(root, "Choix des règles iptables")
    choice = dialog.result

    # Si ne choisi pas a, r ou s
    if choice is None or choice.lower() not in ["ajouter", "retirer", "supprimer"]:
        print("Vous n'avez pas choisi d'appliquer ou de retirer les règles iptables.")
        root.destroy()
        exit(code="Error: No choice")

    # Traitement en fonction du choix
    if choice == "ajouter": # ajouter 
        path = dir_path + "/Rules/Add.txt"
        #Dialog box with yes/no button and return value
        change_file = messagebox.askyesno("Ajouter des règles", "Voulez-vous changer le fichier des règles iptables?")

        if change_file == True:
            root = tk.Tk()
            root.withdraw()
            with open(path, 'r') as file:
                current_content = file.read()

            # Ouvrir une fenêtre Tkinter pour éditer le fichier
            editor = tk.Tk()
            editor.title("Éditeur de règles iptables (mode ajout)")

            text_widget = tk.Text(editor, wrap="word", height=20, width=50)
            text_widget.insert(tk.END, current_content)
            text_widget.pack()

            # Fonction pour enregistrer les modifications
            def save_changes():
                new_content = text_widget.get("1.0", tk.END)
                with open(path, 'w') as file:
                    file.write(new_content)
                print(f"Les modifications ont été enregistrées dans {path}")
                editor.destroy()

            # Bouton pour enregistrer les modifications
            save_button = tk.Button(editor, text="Enregistrer", command=save_changes)
            save_button.pack()

    elif choice == "retirer": # retirer 
        path = dir_path + "/Rules/Del.txt"
        change_file = messagebox.askyesno("Retirer des règles", "Voulez-vous changer le fichier des règles iptables?")

        if change_file == True:
            root = tk.Tk()
            root.withdraw()
            with open(path, 'r') as file:
                current_content = file.read()

            # Ouvrir une fenêtre Tkinter pour éditer le fichier
            editor = tk.Tk()
            editor.title("Éditeur de règles iptables (mode retrait)")

            text_widget = tk.Text(editor, wrap="word", height=20, width=50)
            text_widget.insert(tk.END, current_content)
            text_widget.pack()

            # Fonction pour enregistrer les modifications
            def save_changes():
                new_content = text_widget.get("1.0", tk.END)
                with open(path, 'w') as file:
                    file.write(new_content)
                print(f"Les modifications ont été enregistrées dans {path}")
                editor.destroy()

            # Bouton pour enregistrer les modifications
            save_button = tk.Button(editor, text="Enregistrer", command=save_changes)
            save_button.pack()
    elif choice == "supprimer": # supprimer
        purge = True

    
    ssh_host = ""
    ssh_user = ""
    ssh_password = ""
    ssh_port = "22"

    if ssh_host == "":
        answer = ""
        while True:
            answer = simpledialog.askstring("Adresse IP", "Entrer l'adresse IP du serveur:", initialvalue=answer)
            #check if answer is a valid IP address with regex
            ip_regex = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
            if answer is not None:
                if ip_regex.match(answer):
                    ssh_host = answer
                    break
                else:
                    message_box("L'adresse IP n'est pas valide")
                    continue                 
            else:
                Empty()


    if ssh_user == "":
        while True:
            answer = simpledialog.askstring("Nom d'utilisateur", "Entez le nom de l'utilsateur du serveur sudo :")
            if answer is not None:
                ssh_user = answer
                break
            else:
                Empty()

    if ssh_password == "":
        while True:
            answer = simpledialog.askstring("Mot de passe", "Entez le mot de passe de l'utilsateur du serveur sudo :", show="*")
            if answer is not None:
                ssh_password = answer
                break
            else:
                Empty()


    if ssh_port == "" or ssh_port == "22":
        answer = simpledialog.askstring("Port SSH", "Entez le port SSH du serveur(22 par défaut):", initialvalue="22")
        if answer is not None:
            ssh_port = answer


    log_file_path = dir_path + "/logs/log.txt"
    try:
        with open(path, 'r') as commandes_file:
            commandes = commandes_file.readlines()
    except BaseException:
        commandes = []
    return ssh_host, ssh_user, ssh_password, log_file_path, commandes, ssh_port, purge


def connection(ssh_host, ssh_user, ssh_password, ssh_port):
    print(f"Ouverture d'une connexion SSH vers {ssh_host}")
    try:
        ssh_session = pexpect.spawn(f"ssh {ssh_user}@{ssh_host} -p {ssh_port}")

        try:
            ssh_session.expect("sure", timeout=2)
            ssh_session.sendline("yes")
        except BaseException:
            pass

        ssh_session.expect("password:")
        ssh_session.sendline(ssh_password)
        ssh_session.expect("Last login")
        print("Connecté")
        test_sudo(ssh_session, ssh_password)
        ssh_session.sendline("sudo -i")
        ssh_session.expect("[sudo]")
        ssh_session.sendline(ssh_password)
        return ssh_session
    except BaseException:
        message_box("Impossible de se connecter au serveur")
        exit(code="Error: Impossible de se connecter au serveur")

def apply_rules(ssh_session, ssh_password, command):
    ssh_session.sendline(f"{command.strip()}")


def iptables_rules(ssh_session):
    lines = []
    ssh_session.sendline("iptables -L -n")
    ssh_session.sendline("echo command iptables executed")
    ssh_session.expect("echo command iptables executed", timeout=10)
    time.sleep(1)
    output_lines = ssh_session.before.decode().splitlines()
    for line in output_lines:
        if "@" not in line:
            lines.append(line)
    try:
        lines = lines[lines.index("Chain INPUT (policy ACCEPT)"):]
    except:
        message_box("une erreur est survenue")
        exit(code="Error: une erreur est survenue")
    INPUT = []
    OUTPUT = []
    FORWARD = []
    INPUTP = []
    OUTPUTP = []
    FORWARDP = []
    Icounter = 0
    Ocounter = 0
    Fcounter = 0
    for line in lines:
        if Icounter == 2 or Ocounter == 2 or Fcounter == 2:
            break
        else:
            if "Chain" in line:
                if "INPUT" in line:
                    types = INPUT
                    Icounter += 1
                elif "OUTPUT" in line:
                    types = OUTPUT
                    Ocounter += 1
                elif "FORWARD" in line:
                    types = FORWARD
                    Fcounter += 1
                continue
            if "target" in line:
                continue
            else:
                types.append(line)

    for line in INPUT:
        if "tcp" in line or "udp" in line:
            port_matches = re.findall(r"\b(?:dpt|spt):(\S+)\b", line)
            str_matches = str(port_matches)
            if str_matches == "[]":
                # if there are some text in the line set a variable to " "
                if len(line) > 0:
                    port_matches = [" "]

            for match in port_matches:
                INPUTP.append(match)

    for line in OUTPUT:
        if "tcp" in line or "udp" in line or "icmp" in line or "/" in line:
            port_matches = re.findall(r"\b(?:dpt|spt):(\S+)\b", line)
            str_matches = str(port_matches)
            if str_matches == "[]":
                # if there are some text in the line set a variable to " "
                if len(line) > 0:
                    port_matches = [" "]

            for match in port_matches:
                OUTPUTP.append(match)
    for line in FORWARD:
        if "tcp" in line or "udp" in line:
            port_matches = re.findall(r"\b(?:dpt|spt):(\S+)\b", line)
            str_matches = str(port_matches)
            if str_matches == "[]":
                # if there are some text in the line set a variable to " "
                if len(line) > 0:
                    port_matches = [" "]

            for match in port_matches:
                FORWARDP.append(match)

    if len(INPUTP) == 0:
        INPUTP = ["n/a"]
    if len(FORWARDP) == 0:
        FORWARDP = ["n/a"]
    if len(OUTPUTP) == 0:
        OUTPUTP = ["n/a"]
    return [INPUTP, FORWARDP, OUTPUTP]


def settings_rules(ssh_session, commandes, ssh_password):
    results = []
    IPTABLES = iptables_rules(ssh_session)
    INPUTP = IPTABLES[0]
    FORWARDP = IPTABLES[1]
    OUTPUTP = IPTABLES[2]
    total_commandes = len(commandes)
    try:
        bar = progressbar.ProgressBar(maxval=total_commandes)
    except BaseException:
        pass
    i = 1
    problem = []
    for command in commandes:
        present = False
        if "-A" in command:
            if "INPUT" in command:
                for port in INPUTP:
                    if str(port) in command:
                        present = True
                        port_present = port
                        if "!" in command:
                            port_present = "!" + port_present
                        break
                if present:
                    results_lines = (
                        f"La règle {i} pour le port {port_present} existe déjà")
                    problem.append(f"La règle {i} pour le port {port_present} existe déjà")
                else:
                    apply_rules(ssh_session, ssh_password, command)
            elif "FORWARD" in command:
                for port in FORWARDP:
                    if str(port) in command:
                        present = True
                        port_present = port
                        if "!" in command:
                            port_present = "!" + port_present
                        break
                if present:
                    results_lines = (
                        f"La règle {i} pour le port {port_present} existe déjà")
                    problem.append(f"La règle {i} pour le port {port_present} existe déjà")
                else:
                    apply_rules(ssh_session, ssh_password, command)
            elif "OUTPUT" in command:
                for port in OUTPUTP:
                    if str(port) in command:
                        present = True
                        port_present = port
                        if "!" in command:
                            port_present = "!" + port_present
                        break
                if present:
                    results_lines = (
                        f"La règle {i} pour le port {port_present} existe déjà")
                    problem.append(f"La règle {i} pour le port {port_present} existe déjà")
                else:
                    apply_rules(ssh_session, ssh_password, command)
        elif "-D" in command:
            if "INPUT" in command:
                for port in INPUTP:
                    if str(port) in command:
                        present = True
                        port_present = port
                        if "!" in command:
                            port_present = "!" + port_present
                        break
                if present:
                    apply_rules(ssh_session, ssh_password, command)
                else:
                    results.append(
                        f"La règle pour le port {port} n'existe pas")
                    problem.append(f"La règle pour le port {port} n'existe pas")
            elif "FORWARD" in command:
                for port in FORWARDP:
                    if str(port) in command:
                        present = True
                        port_present = port
                        if "!" in command:
                            port_present = "!" + port_present
                        break
                if present:
                    apply_rules(ssh_session, ssh_password, command)
                else:
                    results.append(
                        f"La règle pour le port {port} n'existe pas")
                    problem.append(f"La règle pour le port {port} n'existe pas")
            elif "OUTPUT" in command:
                for port in OUTPUTP:
                    if str(port) in command:
                        present = True
                        port_present = port
                        if "!" in command:
                            port_present = "!" + port_present
                        break
                if present:
                    apply_rules(ssh_session, ssh_password, command)
                else:
                    results.append(
                        f"La règle pour le port {port} n'existe pas")
                    problem.append(f"La règle pour le port {port} n'existe pas")
        try:
            results.append(results_lines)
        except BaseException:
            pass
        try:
            bar.update(commandes.index(command) + 1)
        except BaseException:
            pass
        i += 1
    # verifier si les règles ont bien été appliquées
    time.sleep(2)
    IPTABLES = iptables_rules(ssh_session)
    INPUTP = IPTABLES[0]
    FORWARDP = IPTABLES[1]
    OUTPUTP = IPTABLES[2]

    # get port of all commands
    commandes_ports = []
    commandes_status = []
    commandes_type = []
    for command in commandes:
        if "-A" in command:
            commandes_status.append("added")
        elif "-D" in command:
            commandes_status.append("deleted")
        if "INPUT" in command:
            commandes_type.append("INPUT")
        elif "FORWARD" in command:
            commandes_type.append("FORWARD")
        elif "OUTPUT" in command:
            commandes_type.append("OUTPUT")
        try:
            splited = command.split("-j")
            port = splited[0]
            # split at all spaces and get the last one
            port = port.split(" ")
            end_port = port[-1]
            if end_port.isnumeric() == False:
                end_port = port[-2]
            # if end port is not a number
            if end_port.isnumeric() == False:
                end_port = " "
            if "!" in command:
                end_port = "!" + end_port
            commandes_ports.append(end_port)

        except Exception as e:
            print(e)
            pass

    # compare results and commands
    commandes_number = 0
    for port in commandes_ports:
        if commandes_status[commandes_number] == "added":
            if commandes_type[commandes_number] == "INPUT":
                if port in INPUTP:
                    results.append(
                        f"La règle {commandes_number+1} pour le port {port} en INPUT est bien présente")
                else:
                    results.append(
                        f"La règle {commandes_number+1} pour le port {port} en INPUT n'a pas été ajoutée")
                    problem.append(f"La règle {commandes_number+1} pour le port {port} en INPUT n'a pas été ajoutée")
            elif commandes_type[commandes_number] == "FORWARD":
                if port in FORWARDP:
                    results.append(
                        f"La règle {commandes_number+1} pour le port {port} en FORWARD est bien présente")
                else:
                    results.append(
                        f"La règle {commandes_number+1} pour le port {port} en FORWARD n'a pas été ajoutée")
                    problem.append(f"La règle {commandes_number+1} pour le port {port} en FORWARD n'a pas été ajoutée")
            elif commandes_type[commandes_number] == "OUTPUT":
                if port in OUTPUTP:
                    results.append(
                        f"La règle {commandes_number+1} pour le port {port} en OUTPUT est bien présente")
                else:
                    results.append(
                        f"La règle {commandes_number+1} pour le port {port} en OUTPUT n'a pas été ajoutée")
                    problem.append(f"La règle {commandes_number+1} pour le port {port} en OUTPUT n'a pas été ajoutée")
        elif commandes_status[commandes_number] == "deleted":
            if commandes_type[commandes_number] == "INPUT":
                if port in INPUTP:
                    results.append(
                        f"La règle {commandes_number+1} pour le port {port} en INPUT n'a pas été supprimée")
                    problem.append(f"La règle {commandes_number+1} pour le port {port} en INPUT n'a pas été supprimée")
                else:
                    results.append(
                        f"La règle {commandes_number+1} pour le port {port} en INPUT a bien été supprimée")
            elif commandes_type[commandes_number] == "FORWARD":
                if port in FORWARDP:
                    results.append(
                        f"La règle {commandes_number+1} pour le port {port} en FORWARD n'a pas été supprimée")
                    problem.append(f"La règle {commandes_number+1} pour le port {port} en FORWARD n'a pas été supprimée")
                else:
                    results.append(
                        f"La règle {commandes_number+1} pour le port {port} en FORWARD a bien été supprimée")
            elif commandes_type[commandes_number] == "OUTPUT":
                if port in OUTPUTP:
                    results.append(
                        f"La règle {commandes_number+1} pour le port {port} en OUTPUT n'a pas été supprimée")
                    problem.append(f"La règle {commandes_number+1} pour le port {port} en OUTPUT n'a pas été supprimée")
                else:
                    results.append(
                        f"La règle {commandes_number+1} pour le port {port} en OUTPUT a bien été supprimée")
        commandes_number += 1
    # for line in results:
    #     print(line)
    if problem==[]:
        results.append("Toutes les règles ont été appliquées avec succès")
        message_box_success("Toutes les règles ont été appliquées avec succès")
    else:
        message_box(problem)
    results.append(
        "Si une régle déclarée comme déjà existante et que cette même régle est déclarée comme ajoutée, rien ne s'est passé")

    # close ssh session
    ssh_session.close()
    return results


def logs(results, log_file_path):
    with open(log_file_path, 'a') as log_file:
        for result in results:
            actual_date_time = time.strftime("%d/%m/%Y %H:%M:%S")
            log_file.write(actual_date_time + " " + result + '\n')

    print(f"Résultats sauvegardés dans {log_file_path}")


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Pour masquer la fenêtre principale
    purge = False
    ssh_host, ssh_user, ssh_password, log_file_path, commandes, ssh_port, purge = get_variable()
    if not purge:
        ssh_session = connection(ssh_host, ssh_user, ssh_password, ssh_port)
        test_iptables(ssh_session, ssh_password)
        results = settings_rules(ssh_session, commandes, ssh_password)
        logs(results, log_file_path)
    elif purge:
        ssh_session = connection(ssh_host, ssh_user, ssh_password, ssh_port)
        test_iptables(ssh_session, ssh_password)
        ssh_session.sendline("iptables -F")
        message_box_success("Toutes les règles iptables ont été supprimées")
        logs(["Toutes les règles iptables ont été supprimées"], log_file_path)
