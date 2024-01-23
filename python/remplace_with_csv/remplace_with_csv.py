import csv

def generer_phrases(fichier_csv):
    phrases = []
    
    with open(fichier_csv, newline='', encoding='utf-8') as csvfile:
        lecteur_csv = csv.reader(csvfile)
        en_tetes = next(lecteur_csv)  # Ignorer la première ligne si elle contient les en-têtes
        
        for ligne in lecteur_csv:
            pc, ip = ligne
            phrase = f'echo {pc} - {ip}\nmd "\\{ip}\\c$\\Program Files (x86)\\Cegid\\Cegid Retail\\CPOS Drivers\\Neptin"\nxcopy "\\srv-data\\Informatique\\13-Distrib\\Nepting" "\\{ip}\\c$\\Program Files (x86)\\Cegid\\Cegid Retail\\CPOS Drivers\\Neptin"\n'
            phrases.append(phrase)
    
    return phrases

def main():
    fichier_csv = 'pc_ip.csv'  # Remplacez par le chemin réel de votre fichier CSV
    phrases = generer_phrases(fichier_csv)
    
    phrases = generer_phrases(fichier_csv)
    
    with open('output.txt', 'w', encoding='utf-8') as fichier_texte:
        for phrase in phrases:
            print(phrase, file=fichier_texte)

if __name__== "_main_":
    main()