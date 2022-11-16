# Connexion a la base de donnee
import requests
import ressources

# Gestion des fichiers 
from os import listdir
from os.path import isfile, join, splitext



def waitFile() :
    while(True) :
        # Recupere la liste des [fichiers] presents dans le dossier "Questions"
        fichiers = [f for f in listdir("Questions") if isfile(join("Questions", f))]
        # Si la liste n'est pas vide : on verifie que l'extension est correcte
        if fichiers :
            # Et si l'extension est "xml" (Exigence de format pour la question) : 
            if (splitext(fichiers[0])[1] == ".xml"):
                # Sortie de la boucle
                break

        # Sinon attente de nouveau fichier

    #Renvoie du fichier à traiter après la boucle
    return fichiers[0]

# Init la bdd et les message de requete
db, req = ressources.ConnectDB()

while(True) :

    # Attente de reception d'une question
    fic = waitFile() 

    print(fic)

    # Lecture du fichier
    fichier = open("Questions/"+fic, "r")
    print(fichier.read())
    fichier.close()

    break

ressources.DisconnectDB(req,db)

exit()