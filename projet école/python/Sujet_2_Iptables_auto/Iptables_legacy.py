import pexpect
from dotenv import load_dotenv
import os
import time
import re
try:
    import progressbar
except BaseException:
    pass


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

    choice = input("Voulez-vous appliquer les règles iptables qui sont dans le fichier Add.txt ou les retirer avec Del.txt ? Ou Supprimer toutes les règles ? (a/r/s) ")
    if choice == "a":
        print("Vous avez choisi d'appliquer les règles iptables")
        path = dir_path + "/Rules/Add.txt"
    elif choice == "r":
        print("Vous avez choisi de retirer les règles iptables")
        path = dir_path + "/Rules/Del.txt"
    elif choice == "s":
        print("Vous avez choisi de supprimer toutes les règles iptables")
        purge = True
    else:
        print("Vous n'avez pas choisi d'appliquer ou de retirer les règles iptables")
        exit(code="Error: No choice")

    ssh_host = os.getenv('SSH_HOST')
    ssh_user = os.getenv('SSH_USER')
    ssh_password = os.getenv('SSH_PASSWORD')
    ssh_port = os.getenv('SSH_PORT')

    if ssh_host == "":
        print("Vous n'avez pas renseigné l'adresse IP du serveur, voulez-vous le faire maintenant ?")
        ssh_host = input("Adresse IP du serveur: ")
        if ssh_host == "":
            Empty()
    if ssh_user == "":
        print("Vous n'avez pas renseigné le nom d'utilisateur, voulez-vous le faire maintenant ?")
        ssh_user = input("Nom d'utilisateur: ")
        if ssh_user == "":
            Empty()
    if ssh_password == "":
        print(
            "Vous n'avez pas renseigné le mot de passe, voulez-vous le faire maintenant ?")
        ssh_password = input("Mot de passe: ")
        if ssh_password == "":
            Empty()
    if ssh_port == "":
        print("Vous n'avez pas renseigné le port SSH, voulez-vous le faire maintenant ?")
        ssh_port = input("Port SSH: ")
        if ssh_port == "":
            Empty()

    log_file_path = dir_path + "/logs/log.txt"
    try:
        with open(path, 'r') as commandes_file:
            commandes = commandes_file.readlines()
    except BaseException:
        commandes = []
    return ssh_host, ssh_user, ssh_password, log_file_path, commandes, ssh_port, purge


def connection(ssh_host, ssh_user, ssh_password, ssh_port):
    print(f"Ouverture d'une connexion SSH vers {ssh_host}")
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


def apply_rules(ssh_session, ssh_password, command):
    ssh_session.sendline(f"{command.strip()}")


def iptables_rules(ssh_session):
    lines = []
    ssh_session.sendline("iptables -L -n")
    ssh_session.sendline("echo command ls executed")
    ssh_session.expect("echo command ls executed", timeout=10)
    output_lines = ssh_session.before.decode().splitlines()
    for line in output_lines:
        if "@" not in line:
            lines.append(line)
    lines = lines[lines.index("Chain INPUT (policy ACCEPT)"):]
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
            elif commandes_type[commandes_number] == "FORWARD":
                if port in FORWARDP:
                    results.append(
                        f"La règle {commandes_number+1} pour le port {port} en FORWARD est bien présente")
                else:
                    results.append(
                        f"La règle {commandes_number+1} pour le port {port} en FORWARD n'a pas été ajoutée")
            elif commandes_type[commandes_number] == "OUTPUT":
                if port in OUTPUTP:
                    results.append(
                        f"La règle {commandes_number+1} pour le port {port} en OUTPUT est bien présente")
                else:
                    results.append(
                        f"La règle {commandes_number+1} pour le port {port} en OUTPUT n'a pas été ajoutée")
        elif commandes_status[commandes_number] == "deleted":
            if commandes_type[commandes_number] == "INPUT":
                if port in INPUTP:
                    results.append(
                        f"La règle {commandes_number+1} pour le port {port} en INPUT n'a pas été supprimée")
                else:
                    results.append(
                        f"La règle {commandes_number+1} pour le port {port} en INPUT a bien été supprimée")
            elif commandes_type[commandes_number] == "FORWARD":
                if port in FORWARDP:
                    results.append(
                        f"La règle {commandes_number+1} pour le port {port} en FORWARD n'a pas été supprimée")
                else:
                    results.append(
                        f"La règle {commandes_number+1} pour le port {port} en FORWARD a bien été supprimée")
            elif commandes_type[commandes_number] == "OUTPUT":
                if port in OUTPUTP:
                    results.append(
                        f"La règle {commandes_number+1} pour le port {port} en OUTPUT n'a pas été supprimée")
                else:
                    results.append(
                        f"La règle {commandes_number+1} pour le port {port} en OUTPUT a bien été supprimée")
        commandes_number += 1
    for line in results:
        print(line)
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
        print("Toutes les règles iptables ont été supprimées")
        logs(["Toutes les règles iptables ont été supprimées"], log_file_path)
