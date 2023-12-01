# 23-22-02
# Sous PYTHON : garder les lignes dans un fichier CSV à condition que la colone contionne 

import pandas as pd

# ------- GARDER QUE ... QUAND EGALE A ...
df = pd.read_csv('C:/Users/slin/Desktop/Script/python/manip_csv/no_auth.csv')
  
#garder les données égale à "FALSE" dans la colonne nommé "Double_auth"
df_new = df[df['Double_auth'] == False]

#crée un nouveau fichier 
df_new.to_csv('example_3.csv', index=False)


# ------- GARDER QUE SICONTIENT ... 
# df = pd.read_csv('C:/Users/slin/Desktop/Script/python/manip_csv/devices.csv')
# df_new = df[df['Operating system'].astype(str).str.contains("Windows 7")]
# df_new.to_csv('example.csv', index=False)