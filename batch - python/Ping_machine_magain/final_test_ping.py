# // ---------------------------------------- \\ 
# // ----------    TEST DE PING    ---------- \\ 
# // ----------   BY John Allard   ---------- \\ 
# // ----------   & Sandrine Lin   ---------- \\ 
# // ----------     10/11/2023     ---------- \\ 
# // ---------------------------------------- \\ 

import os
import datetime
from datetime import datetime
import time

# ---------- fonction pour créer les adresse IP : 10.x.y.Z
def ping(x,start,stop):
    
    for y in range (start,stop) :

        # ---- à exclure pour 10.1 ----
        if (x == 1) and (y in to_forget_10_1) :                        # si dans la liste to_forget_10_1
            continue                                    # passer                       

        # ---- .50 / .51 /.70 /.90
        for z in (50,51,70,90) :
            hostname = str("10."+str(x)+"."+str(y)+"."+str(z))
            response = os.system("ping -n 1 " + hostname + '| find "TTL=" >nul')
            # ---- réponse positive au ping
            if response == 0:
                if z == 50 : 
                    etat_50 = 'UP'
                if z == 51 :
                    etat_51 = 'UP'
                if z == 70 : 
                    etat_70 = 'UP'
                if z == 90 :
                    etat_90 = 'UP'
            else: # ---- réponse négative au ping
                if z == 50 : 
                    etat_50 = 'DOWN'
                if z == 51 :
                    etat_51 = 'DOWN'
                if z == 70 : 
                    etat_70 = 'DOWN'
                if z == 90 :
                    etat_90 = 'DOWN'
        
        # ---- Ecrire dans le csv
        if x == 2 :
            y_split = str(y)                    
            y_split = y_split[1:3]    
            nom_mag = "Magasin 4"+y_split
        else : 
            nom_mag = "Magasin "+str(y)
        with open(name_file, 'a') as f:
            f.write("{};{};{};{};{}\n".format(nom_mag , etat_50 , etat_51, etat_70, etat_90))
    
if __name__ == '__main__':   
    
    print ("Merci de ne pas éteindre ce terminal, il se fermera à la fin du programme ... ")
    print ("Le programme met environ 12 min à faire tous les magasins, veuillez attendre ... ")

    time_today = str(datetime.today().strftime("%Y-%m-%d %H-%M"))
    
    path = os.path.dirname(os.path.realpath(__file__)) 
    name_file = os.path.join(path, 'resultats_ping'+time_today+'.csv')
    
    # ---------- Ouvrir le fichier CSV et mettre les en-têtes
    with open(name_file, 'a') as f:
        f.write("{};{};{};{};{}\n".format('Nom du magasin', 'ETAT 50','ETAT 51','ETAT 70','ETAT 90'))

    # ---------- LISTE A EXCLURE :
    to_forget_10_1 = [6,8,11,14,15,22,23,25,34,35,36,39,40,50,52,53,54,65,117,118,119,121,137,138,140,144,146,148,150,151,152,154,192,197,198,199,201,202,203,204,205,218,219,220,222,223,225,229,231,232,233] 
    to_forget_10_1 += list(range(43,48)) + list(range(56,62)) + list(range(68,72)) + list(range(76,80)) + list(range(82,106)) + list(range(107,116)) + list(range(123,127)) + list(range(128,136)) + list(range(156,191)) + list(range(207,215)) + list(range(236,255))
    
    # ---------- ping(x,start,stop)
    ping (1,1,255)
    # ---------- ping Magasin 412
    ping (2,112,113)

    print ("Le programme est fini, bonne journée :D ")
    time.sleep(7)
    exit()