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
        
        # ---- à exclure pour 10.2 ----
        if (x == 2) and (y in to_forget_10_2) :                        # si dans la liste to_forget_10_2
            continue                                    # passer

        # ---- .254
        hostname = str("10."+str(x)+"."+str(y)+".254")
        response = os.system("ping -n 1 " + hostname + '| find "TTL=" >nul')
        # ---- réponse positive au ping
        if response == 0:
            etat_254 = 'UP'
        else: # ---- réponse négative au ping
            etat_254 = 'DOWN'

        # ---- Ecrire dans le csv
        if (x == 2) and (y > 99) :
            y_split = str(y)
            y_split = y_split[1:3]
            nom_mag = "Magasin 4"+y_split
        elif x == 2 and (y > 9 ):
            nom_mag = "Magasin 3"+str(y)
        elif x == 2 :
            nom_mag = "Magasin 30"+str(y)
        else : 
            nom_mag = "Magasin "+str(y)

        with open(name_file, 'a') as f:
            f.write("{};{};{}\n".format(nom_mag,hostname,etat_254))

if __name__ == '__main__':

    print ("Merci de ne pas éteindre ce terminal, il se fermera à la fin du programme ... ")
    print ("Le programme met environ 12 min à faire tous les magasins, veuillez attendre ... ")

    time_today = str(datetime.today().strftime("%Y-%m-%d %H-%M"))

    path = os.path.dirname(os.path.realpath(__file__))
    name_file = os.path.join(path, 'resultats_ping'+time_today+'.csv')

    # ---------- Ouvrir le fichier CSV et mettre les en-têtes
    with open(name_file, 'a') as f:
        f.write("{};{};{}\n".format('Nom du magasin','IP' ,'ETAT 254'))

    # ---------- LISTE A EXCLURE :     remarque : range(a,b) -> a inclu, b exclu
    to_forget_10_1 = [6,8,11,14,15,22,23,25,34,35,36,39,40,50,52,53,54,65,117,118,119,121,137,138,140,144,146,148,150,151,152,154,192,197,198,199,201,202,203,204,205,218,219,220,222,223,225,229,231,232,233]
    to_forget_10_1 += list(range(43,48)) + list(range(56,62)) + list(range(68,72)) + list(range(76,80)) + list(range(82,106)) + list(range(107,116)) + list(range(123,127)) + list(range(128,136)) + list(range(156,191)) + list(range(207,215)) + list(range(236,255))
    
    to_forget_10_2 = [1,2,8,10,13,23,25,33,38]+list(range(42,47))+list(range(49,100))                                                            # mag 300
    to_forget_10_2 += [105,107,109,110,111,113,115,119,120,123,125,127]+list(range(131,138))+list(range(139,153))+list(range(154,256))           # mag 400
    # ---------- ping(x,start,stop) 10.1.
    ping (1,1,255)
    
    # ---------- ping(x,start,stop) 10.2.
    ping (2,1,255)
    

    print ("Le programme est fini, bonne journée :D ")
    time.sleep(7)
    exit()