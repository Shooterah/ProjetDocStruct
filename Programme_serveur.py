# Connexion a la base de donnee
import requests
import ressources

# Librairie pour les arbres dom
import xml.dom.minidom


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


# Fonction qui permet de lire un fichier
def readXML(fic):
    # Creation de l'arbre dom depuis le xml
    tree = xml.dom.minidom.parse("Questions/"+ fic)
    # Premier element de l'arbre
    elt = tree.documentElement

    # Recupere le type de requete (Premier element de l'arbre)
    typereq = elt.getAttribute("typeQuestion")

    #-----------------------------------------------#
    # Analyse de la requete en fonction de son type #
    #-----------------------------------------------#

    # Cv depuis les compétences
    if typereq == "CompFromCv":

        # Init itérateur
        i = 0
        # Init la liste des compétences
        liComp = []

        # Récupere la valeur des elements "competence" (liste) dans l'arbre dom (forme une liste/NodeList)
        competences = tree.getElementsByTagName("competence")

        # Creation de la liste de competences en variable
        for comp in competences:
            liComp.append(comp.childNodes[0].nodeValue)
    
    print(liComp)


# Init la bdd et les message de requete
db, req = ressources.ConnectDB()

while(True) :

    # Attente de reception d'une question
    fic = waitFile() 

    print(fic)

    # Lecture du fichier
    #fichier = open("Questions/"+fic, "r")
    #print(fichier.read())
    #fichier.close()

    readXML(fic)

    break

ressources.DisconnectDB(req,db)

exit()