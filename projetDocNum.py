from multiprocessing.connection import wait
from time import sleep
import pdfplumber
import json
import requests

with pdfplumber.open("C:/M1_DSC/UEP/CV.pdf") as pdf:
    page = pdf.pages[0]
    text = page.extract_text()

with pdfplumber.open("C:/Users/flori/Downloads/CV_Jeoffrey_PEREIRA.pdf") as pdf:
    page2 = pdf.pages[0]
    text2 = page2.extract_text()

listeCompétence = ["Java", "C", "SQL", "Vue.js", "C++", "C#", "JavaScript", "Python", ".NET", "Spring",
                   "SpringBoot", "JS", "Anglais", "Espagnol", "Arabe", "Chinois", "Allemand", "Italien", "PHP", "CSS", "HTML", "Web"]
listeCompétenceTmp = []

ListeNuméroType = ["06", "07", "09"]
ListeNuméroTypeTmp = []

print()
print()


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


getDataCompetence(text)
getDataTelNumber(text)
mail = getDataMail(text)
prenom, nom = getPrenomNom(text)

print(listeCompétenceTmp)
print(ListeNuméroTypeTmp)
print(mail)
print(prenom + " " + nom)

listeCompétenceTmp = []
ListeNuméroTypeTmp = []
print('---------------------------------------------------------')

getDataCompetence(text2)
getDataTelNumber(text2)
mail = getDataMail(text2)
prenom, nom = getPrenomNom(text2)

print(listeCompétenceTmp)
print(ListeNuméroTypeTmp)
print(mail)
print(prenom + " " + nom)
