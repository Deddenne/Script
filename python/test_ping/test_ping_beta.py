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
                  225,229,232] + list(range(43,47)) + list(range(56,61)) + list(range(68,71)) + list(range(76,79)) + list(range(82,105))+ list(range(128,135)) + list(range(156,190))

to_forget_10_2 = [0,1,8,10,13,25,33,38,42,43,44,107,109,110,111,113,115,119,120] + list(range(131,254))

# ---------- fonction pour créer les adresse IP : 10.x.y.Z
for x in range (1,2) :
    for y in range (1,254) :
        # ---- si l'ip commence par 10.1  ... ----
        if x == 1 :
            # ---- à exclure pour 10.1 ----
            if y in to_forget_10_1 :                        # si dans la liste to_forget_10_1
                continue                                    # passer                       
            else :                                          # si n'est pas dans la liste, écrire le nom du magasin
                nom_mag = "-------- Magasin "+str(y)+"\n"
                fichier = open("PingResults.txt", "a")
                fichier.write(nom_mag)

        # ---- si l'ip commence par 10.2  ... ----
        if x == 2 :
            # ---- à exclure pour 10.1 ----
            if y in to_forget_10_2 :                                # si dans la liste to_forget_10_2
                continue                                            # passer
            else :                                                  # si n'est pas dans la liste, écrire le nom du magasin
                if y < 10:                                          # inférieur à 10 
                    nom_mag = "-------- Magasin 30"+str(y)+"\n"     # 30 + y (1 à 9)
                    fichier = open("PingResults.txt", "a")
                    fichier.write(nom_mag)
                elif y < 100:                                       # inférieur à 100
                    nom_mag = "-------- Magasin 3"+str(y)+"\n"      # 3 + y (11 à 99)
                    fichier = open("PingResults.txt", "a")
                    fichier.write(nom_mag)
                else :                                              # supérieur à 100
                    y_split = str(y)                    
                    y_split = y_split[1:3]    
                    nom_mag = "-------- Magasin 4"+y_split+"\n"     # 4 + y (0 à 99)        
                    fichier = open("PingResults.txt", "a")
                    fichier.write(nom_mag)

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
