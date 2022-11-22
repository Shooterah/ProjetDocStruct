
# ---------+
# | Import |
# +--------+

# Connexion a la base de donnee
import requests
import ressources

# Librairie pour les arbres dom
import xml.dom.minidom

# Recuperer la date actuelle
from datetime import datetime



# Gestion des fichiers 
from os import listdir
from os.path import isfile, join, splitext

# +------------+
# | Constantes |
# +------------+

# Dans le cas ou une liste de compétence est renvoyee (cf. readXML())
LICOMP = 1
# Dans le cas ou une liste de formations est renvoyee (Cf. readXml())
LIFORMA = 2


# Structure des reponses sql (position i de l'element):
IDCAND   = 0
NOM      = 1
PRENOM   = 2
EMAIL    = 3
TEL      = 4
LINKEDIN = 5
GITHUB   = 6

# +---------+
# | Classes |
# +---------+

# Classe personne
class personne: 

    def __init__(self, n, p, t):
        self.nom = n   
        self.prenom = p
        self.telephone = t
        
# Classe envoyeur/ auteur
class envoyeur:
    def __init__(self, id, nom, date):
        self.id = id  
        self.nom = nom
        self.date = date

    def afficher(self):
        print(f"""
        Id     : {self.id}
        Prenom : {self.nom}
        Date   : {self.date}
        """)


# +-----------+
# | Fonctions |
# +-----------+

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

    # Recupere les infos de l'envoyeur de la question    
    id = tree.getElementsByTagName("id")[0].childNodes[0].nodeValue
    auteur = tree.getElementsByTagName("auteur")[0].childNodes[0].nodeValue
    date = tree.getElementsByTagName("date")[0].childNodes[0].nodeValue

    
    # Recupere le type de requete (Premier element de l'arbre)
    typereq = elt.getAttribute("typeQuestion")

    # Analyse de la requete en fonction de son type #
      
    # Cv depuis les competences
    if typereq == "CompFromCv":

        # Init itérateur
        i = 0
        # Init la liste des compétences
        liComp = []

        # Récupere la valeur des elements "competence" (liste) dans l'arbre dom (forme une liste/NodeList)
        competences = tree.getElementsByTagName("competence")

        # Creation de la liste de competences (variable)
        for comp in competences:
            # childNodes = ce qui est contenu entre les balises <competence>,
            # nodeValue = la valeur de ce contenu
            liComp.append(comp.childNodes[0].nodeValue)
    
        return LICOMP,liComp, envoyeur(id,auteur,date)


    # Cv depuis les formations
    if typereq == "PersFromForma":

        # Init itérateur
        i = 0
        # Init la liste des compétences
        liForma = []

        # Récupere la valeur des elements "competence" (liste) dans l'arbre dom (forme une liste/NodeList)
        formations = tree.getElementsByTagName("formation")

        # Creation de la liste de competences (variable)
        for forma in formations:
            # childNodes = ce qui est contenu entre les balises <competence>,
            # nodeValue = la valeur de ce contenu
            liForma.append(forma.childNodes[0].nodeValue)
    
        return LIFORMA, liForma, envoyeur(id,auteur,date)



# Ajout d'un envoyeur dans un xml de reponse
def addEnv(doc, auteur):
    env = doc.createElement("envoyeur")
    # Ajoute un ID dans la partie envoyeur
    id = doc.createElement("id")
    textid = doc.createTextNode(str(auteur.id))
    id.appendChild(textid)
    env.appendChild(id)

    # Ajoute un auteur dans la partie envoyeur
    auteur = doc.createElement("auteur")
    textAuteur = doc.createTextNode("SERVEUR")
    auteur.appendChild(textAuteur)
    env.appendChild(auteur)
    
    # ajout ligne date et de son texte
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d")
    date = doc.createElement("date")
    textdate = doc.createTextNode(current_time)
    date.appendChild(textdate)
    env.appendChild(date)
   
    return env


# Ajout d'un destinataire dans un xml de reponse
def addDest(doc, auteur):

    dest = doc.createElement("destinataire")
    txtDest = doc.createTextNode(str(auteur.nom))
    dest.appendChild(txtDest)

    return dest


# Ajoute les Cvs dans une reponse de type Competence
def addCvsComp(doc, liCVs):

    # Ajoute le nombre de cv trouvé
    CVs = doc.createElement("CVS")
    CVs.setAttribute("nb",str(len(liCVs)))

    # Analyse de la liste de résultats
    for cv in liCVs:

        # Ajoute la liste des Cvs de personnes
        CV = doc.createElement("CV")

        # Stockage des infomations
        p = personne(cv[PRENOM],cv[NOM],cv[TEL])
        # Si la requete est competence, on souhaite avoir le mail et le linkedin et le github
        mailCand = cv[EMAIL]
        linkedinCand = cv[LINKEDIN]
        githubCand = cv[GITHUB]

        pers = doc.createElement("personne")

        # Ajout du nom candidat
        nom = doc.createElement("nom")
        txtNom = doc.createTextNode(str(p.nom))
        nom.appendChild(txtNom)
        # Ajout du prenom du candidat
        prenom = doc.createElement("prenom")
        txtPrenom = doc.createTextNode(str(p.prenom))
        prenom.appendChild(txtPrenom)
        # Ajout du telephone du candidat
        tel = doc.createElement("telephone")
        txtTel = doc.createTextNode(str(p.telephone))
        tel.appendChild(txtTel)

        # Ajout des infos du candidat dans le noeud personne
        pers.appendChild(nom)
        pers.appendChild(prenom)
        pers.appendChild(tel)

        # Ajout de la personne au CV
        CV.appendChild(pers)

        # Ajout du mail du candidat
        mail = doc.createElement("mail")
        txtMail = doc.createTextNode(str(mailCand))
        mail.appendChild(txtMail)
        # Ajout du mail au CV
        CV.appendChild(mail)

        # Ajout du linkedin du candidat
        linkedin = doc.createElement("linkedin")
        txtLinkedin = doc.createTextNode(str(linkedinCand))
        linkedin.appendChild(txtLinkedin)
        # Ajout du linkedin au CV
        CV.appendChild(linkedin)

       # Ajout du github du candidat
        github = doc.createElement("github")
        txtGithub = doc.createTextNode(str(githubCand))
        github.appendChild(txtGithub)
        # Ajout du linkedin au CV
        CV.appendChild(github)



        CVs.appendChild(CV)




    return CVs



# Ajoute les Cvs dans une reponse de type Formations
def addCvsForma(doc, liCVs):
    # Ajoute le nombre de cv trouvé
    personnes = doc.createElement("personnes")
    personnes.setAttribute("nb",str(len(liCVs)))

    # Analyse de la liste de résultats
    for cv in liCVs:

        # Stockage des infomations
        p = personne(cv[PRENOM],cv[NOM],cv[TEL])

        pers = doc.createElement("personne")

        # Ajout du nom candidat
        nom = doc.createElement("nom")
        txtNom = doc.createTextNode(str(p.nom))
        nom.appendChild(txtNom)
        # Ajout du prenom du candidat
        prenom = doc.createElement("prenom")
        txtPrenom = doc.createTextNode(str(p.prenom))
        prenom.appendChild(txtPrenom)
        # Ajout du telephone du candidat
        tel = doc.createElement("telephone")
        txtTel = doc.createTextNode(str(p.telephone))
        tel.appendChild(txtTel)

        # Ajout des infos du candidat dans le noeud personne
        pers.appendChild(nom)
        pers.appendChild(prenom)
        pers.appendChild(tel)

        
        # Ajout de la personne au tableau personnes
        personnes.appendChild(pers)


    return personnes




# Création d'un document xml de reponse
def repXML(typeRep, auteur, liCVs):
    # Creation du doc
    doc = xml.dom.minidom.parseString("<reponse/>")
    # Init de l'abre dom
    tree = doc.documentElement
    if typeRep == LICOMP:
        tree.setAttribute("typeReponse", "RepCompFromCv")
    elif typeRep == LIFORMA:
        tree.setAttribute("typeReponse", "RepPersFromForma")
    else :
        print("Problème de type de réponse dans la fonction repXML(typeRep)")
        exit()

    # Ajout de l'auteur
    tree.appendChild(addEnv(doc,auteur))

    # Ajout du destinataire
    tree.appendChild(addDest(doc,auteur))

    # Ajout de la liste de CVs

    if typeRep == LICOMP:    
        tree.appendChild(addCvsComp(doc,liCVs))
    elif typeRep == LIFORMA:
        tree.appendChild(addCvsForma(doc,liCVs))
    else :
        print("Problème de type de réponse dans la fonction repXML(typeRep)")
        exit()

    return doc
    


# Creation d'un fichier de nom namefile depuis un arbre xml
def creaFic(doc, nomFic):
    myFile = open("Reponses/" + nomFic, "w+")
    myFile.write(doc.toprettyxml())
    





######################################
#                                    #
#             ___MAIN___             #
#                                    #
######################################


# Init la bdd et les message de requete
db, req = ressources.ConnectDB()

while(True) :

    # Attente de reception d'une question
    fic = waitFile() 

    print(f"Nom du fichier : {fic}")

    # Lecture du fichier
    #fichier = open("Questions/"+fic, "r")
    #print(fichier.read())
    #fichier.close()

    typeReq, liReq, auteur = readXML(fic)

    # Le type de requete implique le meme type de reponse
    typeRep = typeReq

    # Requete de type competence
    if(typeReq == LICOMP):
        sql = ressources.reqLicomp(liReq)
    # Requete de type fromation
    elif(typeReq == LIFORMA):
        sql = ressources.reqLiForma(liReq)

    # Sinon erreur
    else:
        print("Problème rencontré :")
        print("Le type de requête est invalide")
        exit()
    
    # Execution de la requete sql
    req.execute(sql)
    liCVs = req.fetchall()

    # Le nombre de CVs correspondant
    nbCVs = len(liCVs)

    auteur.afficher()
    
    doc = repXML(typeRep,auteur,liCVs)

    creaFic(doc,fic)

    #for cv in liCVs:
        # #print(cv)
        # # Stockage des infomations
        # p = personne(cv[PRENOM],cv[NOM],cv[TEL])
        # # Si la requete est competence, on souhaite avoir le mail et le tel
        # if (typeReq == LICOMP):
        #     mail = cv[EMAIL]
        #     tel = cv[TEL]


            
    
    break

# Deconnexion de la bdd
ressources.DisconnectDB(req,db)

exit()