##################### CHANGER LES NOMS DES FICHIERS #####################
import glob
import os

# Fichier EndpointInventory (extraction XDR)
path_EndpointInventory = os.path.isfile("EndpointInventory*.csv")
if path_EndpointInventory == False :
    pattern_EndpointInventory = "EndpointInventory*.csv"
    maching_file_EndpointInventory = glob.glob(pattern_EndpointInventory)

    src_EndpointInventory = maching_file_EndpointInventory[0]
    dst_EndpointInventory = "EndpointInventory.csv"

    for file_name_EndpointInventory in maching_file_EndpointInventory :
        os.rename(src_EndpointInventory, dst_EndpointInventory)

# Fichier Device List (extraction tous les postes de Trend Vision)
path_Device_List = os.path.isfile("All_Device_Trend.csv")
if path_Device_List == False : 
    pattern_Device_List = "Device_List*.csv"
    maching_file_Device_List = glob.glob(pattern_Device_List)

    src_Device_List = maching_file_Device_List[0]
    dst_Device_List = "All_Device_Trend.csv"

    for file_name in maching_file_Device_List :
        os.rename(src_Device_List, dst_Device_List)


# Fichier Device List (extraction tous les postes de Trend Vision)
path_Umbrella = os.path.isfile("Umbrella.csv")
if path_Umbrella == False :
    pattern_Umbrella = "export*.csv"
    maching_file_Umbrella = glob.glob(pattern_Umbrella)

    src_Umbrella = maching_file_Umbrella[0]
    dst_Umbrella = "Umbrella.csv"

    for file_name in maching_file_Umbrella :
        os.rename(src_Umbrella, dst_Umbrella)

# Fichier GLPI
path_GLPI = os.path.isfile("glpi*.csv")
if path_GLPI == False :
    pattern_GLPI = "glpi*.csv"
    maching_file_GLPI = glob.glob(pattern_GLPI)

    src_GLPI = maching_file_GLPI[0]
    dst_GLPI = "GLPI.csv"

    for file_name in maching_file_GLPI :
        os.rename(src_GLPI, dst_GLPI)



##################### COMPARERE LES FICHIERS #####################

# affectation des fichiers
file1 = "EndpointInventory.csv"
file2 = "All_Device_Trend.csv"
file3 = "Umbrella.csv"
file4 = "GLPI.csv"

# importing module
from pandas import *
import csv
import pandas as pd

# ---------------- Modifier le fichier Umbrella , car sépatateur ";" ----------------
# Lire le fichier CSV avec ; comme séparateur
df = pd.read_csv(file4, sep=';')

# Sélectionner les quatre premières colonnes
df_reduit = df.iloc[:, :4]

# Sauvegarder le nouveau fichier CSV avec , comme séparateur
df_reduit.to_csv(file4,index=False, sep=',')


# reading CSV file
data_Endpoint_name = read_csv(file1)
daya_All_Device_Trend = read_csv(file2)
data_umbrella = read_csv(file3)
data_glpi = read_csv(file4)

# Convertir les données des colones en liste 
Endpoint = data_Endpoint_name['Endpoint name'].tolist()
All_Device_Trend = daya_All_Device_Trend['Device name'].tolist()
glpi = data_glpi['Nom'].tolist()
Umbrella = data_umbrella['label'].tolist()

# Calcul de l'union de toutes les listes pour obtenir tous les éléments uniques
union_all = set(All_Device_Trend).union(Endpoint,glpi,Umbrella)

# Création d'une foonction pour vérifier la version d'Umbrella (No : new  version ; Yes : Old version)
def version_umbrella(device_name):
    file3 = "Umbrella.csv"
    with open(file3, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['label'] == device_name:
                if str(row['osVersion']).startswith("Microsoft Windows NT 10") : 
                    return "No" 
                else :
                    return "Yes"

# Préparation des données pour le fichier CSV
rows = [['Devince name','All_Device_Trend','Trend Vison Endpoint','GLPI','Umbrella','Old version Umbrella']]

# Vérifications des postes
for element in union_all:
    osVersion_umbrella = version_umbrella(element)
    row = [
        element,
        'Yes' if element in All_Device_Trend else 'No',
        'Yes' if element in Endpoint else 'No',
        'Yes' if element in glpi else 'No',
        'Yes' if element in Umbrella else 'No',
        osVersion_umbrella
    ]
    rows.append(row)

# Écriture dans le fichier CSV
with open('list_comparison.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
