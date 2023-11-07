import os
import datetime
from datetime import datetime
import csv


# Créer le fichier CSV
time_today = str(datetime.today().strftime("%Y-%m-%d %H-%M"))
name_file = "PingResults"+time_today+".csv"

with open(name_file, 'w') as csvfile:
    fieldnames = ['Nom du magasin', 'ETAT 50','ETAT 51','ETAT 70','ETAT 90']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # ---------- LISTE A EXCLURE :
    to_forget_10_1 = [6,8,11,14,15,22,23,25,34,35,36,39,40,50,52,54,65,113,114,117,118,121,125,126,137,140,144,146,148,150,152,154,192,197,198,199,202,203,204,207,208,210,213,214,216,218,219,222,223,
                  225,229,232] + list(range(43,48)) + list(range(56,62)) + list(range(68,72)) + list(range(76,80)) + list(range(82,106))+ list(range(128,136)) + list(range(156,191)) + list(range(236,255))

    # ---------- fonction pour créer les adresse IP : 10.x.y.Z
    x = 1
    for y in range (1,254) :

        # ---- à exclure pour 10.1 ----
        if y in to_forget_10_1 :                        # si dans la liste to_forget_10_1
            continue                                    # passer                       

        # ---- .50 / .51 /.70 /.90
        for z in (50,51,70,90) :
            hostname = str("10."+str(x)+"."+str(y)+"."+str(z))
            response = os.system("ping -n 1 " + hostname + '| find "TTL=" >nul')
            if response == 0:
                if z == 50 : 
                    etat_50 = 'UP'
                if z == 51 :
                    etat_51 = 'UP'
                if z == 70 : 
                    etat_70 = 'UP'
                if z == 90 :
                    etat_90 = 'UP'
            else:
                if z == 50 : 
                    etat_50 = 'DOWN'
                if z == 51 :
                    etat_51 = 'DOWN'
                if z == 70 : 
                    etat_70 = 'DOWN'
                if z == 90 :
                    etat_90 = 'DOWN'
        
        nom_mag = "Magasin "+str(y)
        writer.writerow({'Nom du magasin': nom_mag , 'ETAT 50' : etat_50 ,'ETAT 51' : etat_51,'ETAT 70' : etat_70,'ETAT 90' : etat_90})

    ip_400 = [401,412,421]
    x = 2
    
    for y in ip_400 :
        # ---- .50 / .51 /.70 /.90
        for z in (50,51,70,90) :
            hostname = str("10."+str(x)+"."+str(y)+"."+str(z))
            response = os.system("ping -n 1 " + hostname + '| find "TTL=" >nul')
            if response == 0:
                if z == 50 : 
                    etat_50 = 'UP'
                if z == 51 :
                    etat_51 = 'UP'
                if z == 70 : 
                    etat_70 = 'UP'
                if z == 90 :
                    etat_90 = 'UP'
            else:
                if z == 50 : 
                    etat_50 = 'DOWN'
                if z == 51 :
                    etat_51 = 'DOWN'
                if z == 70 : 
                    etat_70 = 'DOWN'
                if z == 90 :
                    etat_90 = 'DOWN'
        
        y_split = str(y)                    
        y_split = y_split[1:3]    
        nom_mag = "Magasin 4"+y_split
        writer.writerow({'Nom du magasin': nom_mag , 'ETAT 50' : etat_50 ,'ETAT 51' : etat_51,'ETAT 70' : etat_70,'ETAT 90' : etat_90})