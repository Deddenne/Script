import socket
import threading
import psutil
import time
import humanfriendly
from pyroute2 import IPRoute
import ping3
import netifaces

# Fonction pour récupérer l'ip publique
def get_private_ip():
    try:
        # Créer une connexion à un serveur quelconque (peu importe l'adresse ou le port)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except socket.error:
        return None

# Définition des constantes
HEADER = 1024
PORT = 5050
SERVER = get_private_ip()
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

# Fonction pour gérer la connexion d'un client
def handle_client(conn, addr):
    print(f"[NOUVELLE CONNEXION] {addr} connecté.")
    connected = True
    while connected:
        msg = conn.recv(HEADER).decode(FORMAT)  # Recevoir le message du client et le décoder en UTF-8
        if msg == DISCONNECT_MESSAGE:
            print(f"[{addr}] : {msg}")
            conn.send("Au revoir !".encode(FORMAT))  # Envoyer un message de confirmation au client
            conn.close()  # Fermer la connexion du client après le message de confirmation
            connected = False
        else:
            # Traiter les commandes envoyées par le client et renvoyer la réponse appropriée
            if msg == "1":
                reponse = GetIP()
                conn.send(reponse.encode(FORMAT))
            elif msg == "2":
                reponse = GetLatency()
                conn.send(reponse.encode(FORMAT))
            elif msg == "3":
                reponse = GetARP()
                conn.send(reponse.encode(FORMAT))
            elif msg == "4":
                reponse = GetEstablishedConnections()
                conn.send(reponse.encode(FORMAT))
            elif msg == "5":
                reponse = GetBandwidth()
                conn.send(reponse.encode(FORMAT))
            elif msg == "6":
                reponse = GetUsageinfo()
                conn.send(reponse.encode(FORMAT))
    conn.close()

# Fonction pour démarrer le serveur
def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)  # Liaison du serveur à l'adresse et au port spécifiés
    print(f"Serveur {socket.gethostname()} : {SERVER}")
    server.listen()  # Mettre en écoute les connexions entrantes
    print(f"[ÉCOUTE] Le serveur écoute sur {SERVER}:{PORT}")
    while True:
        conn, addr = server.accept()  # Accepter une nouvelle connexion entrante
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()  # Démarrer un nouveau thread pour gérer la connexion
        print("Création d'un thread")
        print(f"[CONNEXIONS ACTIVES] {threading.activeCount() - 1}")

# Fonction pour obtenir les informations sur l'adresse IP du serveur
def GetIP():
    # Obtenir le nom d'hôte et les informations sur l'interface réseau 'eth0' si disponible
    hostname = socket.gethostname()
    ip_info = f"Hostname = {hostname}\n"
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        addresse = netifaces.ifaddresses(interface)
        if interface in netifaces.interfaces():
            addresse = netifaces.ifaddresses(interface)
            if netifaces.AF_INET in addresse:
                ipv4_info = addresse[netifaces.AF_INET][0]
                ipv4 = ipv4_info['addr']
                netmask = ipv4_info['netmask']
                gateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
                ip_info += f"Interface = {interface}\n"
                ip_info += f"   IPV4 = {ipv4}\n"
                ip_info += f"   Mask = {netmask}\n"
                ip_info += f"   Gateway = {gateway}\n"
    return ip_info

# Fonction pour obtenir la latence entre le serveur et le client
def GetLatency():
    latency = ping3.ping(SERVER)
    if latency < 1:
        # Convertir la latence en millisecondes
        latency_ms = int(latency * 1000)
        latency = f"{latency_ms}ms"
    else:
        latency = humanfriendly.format_timespan(latency)
    return f"Latence = {latency}\n"

# Fonction pour obtenir la table ARP du serveur
def GetARP():
    iproute = IPRoute()
    arp_table = iproute.get_neighbours(family=2)  # Obtenir la table ARP en utilisant le module pyroute2
    iproute.close()
    formatted_table = []
    for arp in arp_table:
        ip_address = arp.get_attr('NDA_DST')
        mac_address = arp.get_attr('NDA_LLADDR')
        formatted_entry = f"IP = {ip_address} | MAC = {mac_address}\n"
        formatted_table.append(formatted_entry)
    arp_info = "\n".join(formatted_table)
    return arp_info

# Fonction pour obtenir les connexions établies du serveur
def GetEstablishedConnections():
    connections = psutil.net_connections()
    established_connections = [conn for conn in connections if conn.status == 'ESTABLISHED']
    connections_info = ""
    for conn in established_connections:
        source = f"{conn.laddr.ip}:{conn.laddr.port}"
        destination = f"{conn.raddr.ip}:{conn.raddr.port}"
        pid = conn.pid
        connections_info += f"Source = {source}\nDestination = {destination}\nPID = {pid}\n\n"
    return connections_info

# Fonction pour obtenir l'utilisation de la bande passante du serveur
def GetBandwidth():
    network_stats = psutil.net_io_counters()
    sent_bytes = network_stats.bytes_sent
    received_bytes = network_stats.bytes_recv
    return f"Octets envoyés = {humanfriendly.format_size(sent_bytes)}\nOctets reçus = {humanfriendly.format_size(received_bytes)}\n"

# Fonction pour obtenir diverses informations sur l'utilisation des ressources du serveur
def GetUsageinfo():
    usage_info = ""
    usage_info += f"Nombre de processeurs physiques : {psutil.cpu_count(logical=False)}\n"
    usage_info += f"Mémoire Totale : {convert_bytes(psutil.virtual_memory().total)}\n"
    usage_info += f"Mémoire Disponible : {convert_bytes(psutil.virtual_memory().available)}\n"
    usage_info += f"Swap Total : {convert_bytes(psutil.swap_memory().total)}\n"
    usage_info += f"Swap Disponible : {convert_bytes(psutil.swap_memory().free)}\n"
    usage_info += f"Nombre de services en cours d'exécution : {len(psutil.pids())}\n"
    return usage_info

# Fonction pour convertir les octets en Go, Mo, Ko, octets en fonction de la taille
def convert_bytes(num):
    for x in ['octets', 'Ko', 'Mo', 'Go']:
        if num < 1024.0:
            return "{:.2f} {}".format(num, x)
        num /= 1024.0

# Point d'entrée principal du script
if __name__ == '__main__':
    start()  # Démarrer le serveur en appelant la fonction start()