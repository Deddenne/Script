# 23-22-02
# Sous PYTHON : garder les lignes dans un fichier CSV à condition que la colone contionne 

import pandas as pd
  
df = pd.read_csv('C:/Users/slin/Desktop/Script/python/manip_csv/users.csv')
  
#garder les données égale à "FALSE" dans la colonne nommé "Double_auth"
df_new = df[df['Double_auth'] == False]

df_new.to_csv('example_3.csv', index=False)