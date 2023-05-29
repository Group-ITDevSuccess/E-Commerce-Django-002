import subprocess
import os

# Chemin vers le virtualenv à la racine du projet
venv_path = "./env/votre/virtualenv"

# Commande pour activer le virtualenv
activate_command = os.path.join(venv_path, "Scripts", "activate")

# Chemin vers le dossier du projet "ecommerce"
projet_path = "./ecommerce"

# Commande pour exécuter le serveur Django
runserver_command = "py manage.py runserver"

# Activation du virtualenv
subprocess.run(activate_command, shell=True, check=True)

# Changement de répertoire vers le dossier du projet
os.chdir(projet_path)

# Exécution de la commande "py manage.py runserver"
subprocess.run(runserver_command, shell=True)
