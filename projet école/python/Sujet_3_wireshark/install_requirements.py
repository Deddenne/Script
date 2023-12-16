import subprocess

def install_requirements():
    try:
        with open('requirements.txt', 'r') as file:
            file.read().splitlines()
            subprocess.check_call(['pip3', 'install', '-r', 'requirements.txt'])
            subprocess.check_call(['sudo', 'apt-get', 'install', 'python3-tk'])
        print("Les dépendances ont été installées avec succès.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

    if __name__ == "__main__":
        install_requirements()