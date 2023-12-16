import pexpect
import os
from dotenv import load_dotenv
import time

def load_env():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    load_dotenv(dotenv_path=dir_path + '/.env')

def ssh_command(ssh_host, ssh_user, ssh_password, ssh_port):
    print(f"Ouverture d'une connexion SSH vers {ssh_host}")
    ssh_session = pexpect.spawn(f"ssh {ssh_user}@{ssh_host} -p {ssh_port}", timeout=10)
    lines= []

    try:
        index = ssh_session.expect(["password:", "Last login"], timeout=10)

        if index == 0:
            ssh_session.sendline(ssh_password)
            ssh_session.expect("Last login", timeout=10)
            print("Connecté")
        elif index == 1:
            print("Connecté (sans mot de passe)")
        time.sleep(1)
        ssh_session.sendline("sudo -i")
        ssh_session.expect("[sudo]", timeout=10)
        ssh_session.sendline(ssh_password)




        ssh_session.expect("from", timeout=10)
        ssh_session.sendline("iptables -L -n")
        ssh_session.sendline("echo command ls executed")
        ssh_session.expect("echo command ls executed", timeout=10)
        output_lines = ssh_session.before.decode().splitlines()
        for line in output_lines:
            if not "@" in line:
                lines.append(line)

    except pexpect.EOF:
        print("La connexion SSH a été fermée de manière inattendue.")
    except pexpect.TIMEOUT:
        print("Timeout lors de la connexion SSH.")

    print("Sortie de la commande :")
    #print uniqument a partir de la ligne qui contient "Chain"
    lines = lines[lines.index("Chain INPUT (policy ACCEPT)"):]
    INPUT=[]
    OUTPUT=[]
    FORWARD=[]
    for line in lines:
        if "Chain" in line:
            if "INPUT" in line:
                types = INPUT
            elif "OUTPUT" in line:
                types = OUTPUT
            elif "FORWARD" in line:
                types = FORWARD
        if "target" in line:
            pass
        else:
            types.append(line)
        
    print(INPUT)
    print(OUTPUT)
    print(FORWARD)
    # Fermer la session SSH
    ssh_session.sendline("exit")
    ssh_session.close()



if __name__ == "__main__":
    load_env()

    ssh_host = os.getenv('SSH_HOST')
    ssh_user = os.getenv('SSH_USER')
    ssh_password = os.getenv('SSH_PASSWORD')
    ssh_port = os.getenv('SSH_PORT')

    ssh_command(ssh_host, ssh_user, ssh_password, ssh_port)
