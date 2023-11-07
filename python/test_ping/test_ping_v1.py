import os
import datetime
import datetime as dt

# ---------- FONCTION vérifier l'existance du fichier et le créer si n'existe pas 
if os.path.exists("PingResults.txt") :
    with open("PingResults.txt", 'r+') as f:
        f.truncate()
    time_today = str(dt.datetime.now())
    date = "******************************************************\n   PingTest executed on : "+time_today+"\n******************************************************\n"
    with open("PingResults.txt","a") as fichier : 
        fichier.write(date)
else :
    # créer le fichier
    time_today = str(dt.datetime.now())
    date = "******************************************************\n   PingTest executed on : "+time_today+"\n******************************************************\n"
    with open("PingResults.txt","a") as fichier : 
        fichier.write(date)

# ---------- LISTE A EXCLURE :
to_forget_10_1 = [6,8,11,14,15,22,23,25,34,35,36,39,40,50,52,54,65,113,114,117,118,121,125,126,137,140,144,146,148,150,152,154,192,197,198,199,202,203,204,207,208,210,213,214,216,218,219,222,223,
                  225,229,232] + list(range(43,48)) + list(range(56,62)) + list(range(68,72)) + list(range(76,80)) + list(range(82,106))+ list(range(128,136)) + list(range(156,191)) + list(range(236,255))

# ---------- fonction pour créer les adresse IP : 10.x.y.Z
x = 1
for y in range (1,254) :

    # ---- à exclure pour 10.1 ----
    if y in to_forget_10_1 :                        # si dans la liste to_forget_10_1
        continue                                    # passer                       
    else :                                          # si n'est pas dans la liste, écrire le nom du magasin
        nom_mag = "-------- Magasin "+str(y)+"\n"
        fichier = open("PingResults.txt", "a")
        fichier.write(nom_mag)

    # ---- .50 / .51 /.70 /.90
    for z in (50,51,70,90) :
        hostname = str("10."+str(x)+"."+str(y)+"."+str(z))
        response = os.system("ping -n 1 " + hostname + '| find "TTL=" >nul')
        if response == 0:
            information = "{} is up!\n".format(hostname)
            fichier = open("PingResults.txt", "a")
            fichier.write(information)
        else:
            information = "{} is down!\n".format(hostname)
            fichier = open("PingResults.txt", "a")
            fichier.write(information)

ip_400 = [401,412,421]

x = 2
for y in ip_400 :
    y_split = str(y)                    
    y_split = y_split[1:3]    
    nom_mag = "-------- Magasin 4"+y_split+"\n"     # 4 + y (0 à 99)        
    fichier = open("PingResults.txt", "a")
    fichier.write(nom_mag)

    # ---- .50 / .51 /.70 /.90
    for z in (50,51,70,90) :
        hostname = str("10."+str(x)+"."+str(y)+"."+str(z))
        response = os.system("ping -n 1 " + hostname + '| find "TTL=" >nul')
        if response == 0:
            information = "{} is up!\n".format(hostname)
            fichier = open("PingResults.txt", "a")
            fichier.write(information)
        else:
            information = "{} is down!\n".format(hostname)
            fichier = open("PingResults.txt", "a")
            fichier.write(information)