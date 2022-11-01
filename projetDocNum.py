from multiprocessing.connection import wait
from time import sleep
from turtle import clear
import MySQLdb
import pdfplumber
import json
import requests

# Fonction qui affiche le nom de tout les fichiers contenue dans un dossier


def getCV():
    import os
    listeCV = []
    for file in os.listdir("CV/PDF"):
        if file.endswith(".pdf"):
            listeCV.append(file)
    return listeCV


listeCompétence = ["Java", "C", "SQL", "Vue.js", "C++", "C#", "JavaScript", "Python", ".NET", "Spring",
                   "SpringBoot", "JS", "Anglais", "Espagnol", "Arabe", "Chinois", "Allemand", "Italien", "PHP", "CSS", "HTML", "Web"]
listeCompétenceTmp = []

ListeNuméroType = ["06", "07", "09"]
ListeNuméroTypeTmp = []


def getDataCompetence(text):
    for row in text.split("\n"):
        for row2 in row.split(" "):
            for comp in listeCompétence:
                if row2.__contains__(comp):
                    if comp not in listeCompétenceTmp:
                        listeCompétenceTmp.append(comp)


def getDataTelNumber(text):
    chercheToutNum = 0
    nbNum = 0
    numero = ""
    num14 = 0
    for row in text.split("\n"):
        for row2 in row.split(" "):
            if chercheToutNum == 1 and nbNum < 4:
                numero = numero + row2
                nbNum = nbNum + 1
            for num in ListeNuméroType:
                if row2.startswith(num):
                    if len(row2) == 10:
                        ListeNuméroTypeTmp.append(row2)
                    elif len(row2) == 2:
                        chercheToutNum = 1
                        numero = numero + row2
                    elif len(row2) == 14:
                        numero = numero + row2[0] + row2[1] + row2[3] + row2[4] + \
                            row2[6] + row2[7] + row2[9] + \
                            row[10] + row[12] + row[13]
                        num14 = 1
    if chercheToutNum == 1 or num14 == 1:
        ListeNuméroTypeTmp.append(numero)

# fonction qui permet de récupérer l'adresse mail du CV


def getDataMail(text):
    mail = ""
    for row in text.split("\n"):
        for row2 in row.split(" "):
            if row2.__contains__("@"):
                mail = row2
    return mail

# Fonction qui charge tous les prénom éxistant dans une liste


def charge_liste_prenom():
    maListe = []
    url = "https://raw.githubusercontent.com/ori-bibas/list-of-names/main/src/first-names.json"
    r = requests.get(url)
    res = json.loads(r.text)
    res = res["firstNames"]
    for prenom in res:
        maListe.append(prenom)
    return maListe

# Fonction qui renvois le prénom et nom d'un texte sur une ligne a l'aide d'une liste de prénom


def getPrenomNom(text):
    monPrenom = ""
    envoisNom = 0
    for row in text.split("\n"):
        for row2 in row.split(" "):
            if (envoisNom) and (row2 != ""):
                return monPrenom, row2
            for prenom in charge_liste_prenom():
                if prenom.upper() == row2.upper():
                    monPrenom = prenom
                    envoisNom = 1

# Function that get the linkedin url from the text if it exist


def getLinkedin(text):
    for row in text.split("\n"):
        for row2 in row.split(" "):
            if row2.__contains__("linkedin"):
                return row2

# Function that get the github url from the text if it exist


def getGithub(text):
    for row in text.split("\n"):
        for row2 in row.split(" "):
            if row2.__contains__("github"):
                return row2

# Function that create a list that contain the values Licence, Master, Doctorat, DUT, DU, BTS, BAC, Brevet, CAP, BEP


def getDiplome(text):
    diplome = ["Licence", "Master", "Doctorat",
               "DUT", "BTS", "BAC", "Brevet", "CAP", "BEP"]
    diplomeTmp = []
    for row in text.split("\n"):
        for dipl in diplome:
            if row.__contains__(dipl):
                if dipl not in diplomeTmp:
                    diplomeTmp.append(dipl)
    return diplomeTmp


def afficheCV():
    for cv in getCV():
        with pdfplumber.open("CV/PDF/" + cv) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                getDataCompetence(text)
                getDataTelNumber(text)
                mail = getDataMail(text)
                prenom, nom = getPrenomNom(text)
                linkedin = getLinkedin(text)
                github = getGithub(text)
                diplome = getDiplome(text)
                if prenom != "":
                    print("Prénom : " + prenom)
                else:
                    print("Prénom : Inconnu")
                if nom != None:
                    print("Nom : " + nom)
                else:
                    print("Nom : Inconnu")
                if mail != "":
                    print("Mail : " + mail)
                else:
                    print("Mail : Inconnu")
                if linkedin != None:
                    print("Linkedin : " + linkedin)
                else:
                    print("Linkedin : Inconnu")
                if github != None:
                    print("Github : " + github)
                else:
                    print("Github : Inconnu")
                if len(diplome) > 0:
                    print("Diplome : " + str(diplome))
                else:
                    print("Diplome : Inconnu")
                if len(listeCompétenceTmp) > 0:
                    print("Compétence : " + str(listeCompétenceTmp))
                else:
                    print("Compétence : Inconnu")
                if len(ListeNuméroTypeTmp) > 0:
                    print("Numéro : " + str(ListeNuméroTypeTmp))
                else:
                    print("Numéro : Inconnu")
                print(
                    "---------------------------------------------------------------------")
                listeCompétenceTmp.clear()
                ListeNuméroTypeTmp.clear()

def CvtoDB(cursor,db):
     for cv in getCV():
        with pdfplumber.open("CV/PDF/" + cv) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                getDataTelNumber(text)
                mail = getDataMail(text)
                prenom, nom = getPrenomNom(text)
                linkedin = getLinkedin(text)
                github = getGithub(text)
                getDataCompetence(text)
                sendToDB(cursor,db,prenom, nom, mail,ListeNuméroTypeTmp, linkedin, github,listeCompétenceTmp)
                listeCompétenceTmp.clear()
                ListeNuméroTypeTmp.clear()

def ConnectDB():
    try:
        db = MySQLdb.connect(host="localhost", user="root",passwd="",database="docstruc")
        cursor = db.cursor()
    except MySQLdb.Error as error:
        print("Failed to connect to Database{}".format(error))
    finally:
        print("Connected to the database")
        return db,cursor

def DisconnectDB(cursor,db):
    try: 
        if (db):
            cursor.close()
            db.close()
    except MySQLdb.Error as error:
        print("Database is not Connected{}".format(error))
    finally:
        print("MySQL connection is closed")


def sendToDB(cursor,db,prenom, nom, mail,ListeNuméroTypeTmp, linkedin, github,listeCompétenceTmp):
    try:
        sql1 = "INSERT INTO candidats(Nom, Prenom, Mail, Tel, Linkedin, Github) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (nom, prenom, mail,str(ListeNuméroTypeTmp[0]), linkedin, github)
        cursor.execute(sql1, val)
        id = db.insert_id()
        db.commit()

        for comp in listeCompétenceTmp:
            sql2 = "SELECT idcomp FROM competences WHERE NomComp LIKE '"+str(comp)+"'"
            cursor.execute(sql2)
            res = cursor.fetchone()
            sql3 = "INSERT INTO candiComp(idcand, idcomp) VALUES (%s, %s)"
            val = (id,res[0])
            cursor.execute(sql3, val)
            db.commit()

    except MySQLdb.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))
    finally:
        print("Insert "+prenom+" Successful")


db,cursor = ConnectDB()
CvtoDB(cursor,db)
DisconnectDB(cursor,db)
