import os
import shutil
import ressources
from tkinter import *
from functools import partial
import xml.dom.minidom
from datetime import datetime
import socket
from os import listdir
import time
from os.path import isfile, join

listcomp = []
listforma = []
listQuestion = []
idfile = 0
dataf = 0
nbcomp = [0 for i in range(100)]
nbforma = [0 for i in range(100)]
nb_result = 0
type = 0
nbdata = 1
tuple = []


def CreationXMLComp(listQuestion, namefile):

    doc = xml.dom.minidom.parseString("<question/>")
    tree = doc.documentElement
    tree.setAttribute("typeQuestion", "CompFromCv")
    #---------------Capsule envoyeur--------------------#
    envoyeur = doc.createElement("envoyeur")
    # ajout ligne id et de son texte 1
    id = doc.createElement("id")
    textid = doc.createTextNode(str(idfile))
    id.appendChild(textid)
    envoyeur.appendChild(id)
    # ajout ligne auteur et de son texte
    auteur = doc.createElement("auteur")
    textauteur = doc.createTextNode(socket.gethostname())
    auteur.appendChild(textauteur)
    envoyeur.appendChild(auteur)
    # ajout ligne date et de son texte
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d")
    date = doc.createElement("date")
    textdate = doc.createTextNode(current_time)
    date.appendChild(textdate)
    envoyeur.appendChild(date)
    tree.appendChild(envoyeur)
    #-------------------Competences---------------------#
    competences = doc.createElement("competences")
    for comp in listQuestion:
        competence = doc.createElement("competence")
        textcompetence = doc.createTextNode(comp)
        competence.appendChild(textcompetence)
        competences.appendChild(competence)
    tree.appendChild(competences)

    # crée un fichier de nom namefile
    myFile = open("Questions/"+namefile, "w+")
    myFile.write(doc.toprettyxml())

    # print(doc.toprettyxml())

 #-------------------Création D'UN XML de formations---------------------#


def CreationXMLForm(listQuestion, namefile):
    doc = xml.dom.minidom.parseString("<question/>")
    tree = doc.documentElement
    tree.setAttribute("typeQuestion", "PersFromForma")
    #---------------Capsule envoyeur--------------------#
    envoyeur = doc.createElement("envoyeur")
    # ajout ligne id et de son texte 1
    id = doc.createElement("id")
    textid = doc.createTextNode(str(idfile))
    id.appendChild(textid)
    envoyeur.appendChild(id)
    # ajout ligne auteur et de son texte
    auteur = doc.createElement("auteur")
    textauteur = doc.createTextNode(socket.gethostname())
    auteur.appendChild(textauteur)
    envoyeur.appendChild(auteur)
    # ajout ligne date et de son texte
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d")
    date = doc.createElement("date")
    textdate = doc.createTextNode(current_time)
    date.appendChild(textdate)
    envoyeur.appendChild(date)
    tree.appendChild(envoyeur)
    #-------------------Formations---------------------#
    formations = doc.createElement("formations")
    for form in listQuestion:
        formation = doc.createElement("formation")
        textformation = doc.createTextNode(form)
        formation.appendChild(textformation)
        formations.appendChild(formation)
    tree.appendChild(formations)
    # crée un fichier de nom namefile
    myFile = open("Questions/"+namefile, "w+")
    myFile.write(doc.toprettyxml())

 #-------------------LECTURE D'UN XML---------------------#


def readXML(namefile):
    global nbcomp
    global nbforma
    doc = xml.dom.minidom.parse(namefile)
    tree = doc.documentElement
    typerep = tree.getAttribute("typeReponse")
    type = 0

    if typerep == "RepPersFromForma":

        i = 0
        type = 1
        tuplepers = []

        personne = tree.getElementsByTagName("personne")
        for pers in personne:
            nom = pers.getElementsByTagName("nom")
            nom = nom.item(0).firstChild.nodeValue
            prenom = pers.getElementsByTagName("prenom")
            prenom = prenom.item(0).firstChild.nodeValue
            telephone = pers.getElementsByTagName("telephone")
            telephone = telephone.item(0).firstChild.nodeValue
            # ajout des données dans la liste
            tuplepers.append(nom)
            tuplepers.append(prenom)
            tuplepers.append(telephone)
            i = i+1
        return i, tuplepers, type

    if typerep == "RepCompFromCv":

        j = 0
        type = 2
        tupleCV = []

        CV = tree.getElementsByTagName("CV")
        for cv in CV:
            nom = cv.getElementsByTagName("nom")
            nom = nom.item(0).firstChild.nodeValue
            prenom = cv.getElementsByTagName("prenom")
            prenom = prenom.item(0).firstChild.nodeValue
            telephone = cv.getElementsByTagName("telephone")
            telephone = telephone.item(0).firstChild.nodeValue
            mail = cv.getElementsByTagName("mail")
            mail = mail.item(0).firstChild.nodeValue
            github = cv.getElementsByTagName("github")
            github = github.item(0).firstChild.nodeValue
            linkedin = cv.getElementsByTagName("linkedin")
            linkedin = linkedin.item(0).firstChild.nodeValue
            # ajout des données dans la liste
            tupleCV.append(nom)
            tupleCV.append(prenom)
            tupleCV.append(telephone)
            tupleCV.append(mail)
            tupleCV.append(github)
            tupleCV.append(linkedin)
            competence = cv.getElementsByTagName("competence")
            for comp in competence:
                comp = comp.firstChild.nodeValue
                tupleCV.append(comp)
                nbcomp[j] = nbcomp[j]+1

            formation = cv.getElementsByTagName("formation")
            for form in formation:
                form = form.firstChild.nodeValue
                tupleCV.append(form)
                nbforma[j] = nbforma[j]+1
            j = j+1
        return j, tupleCV, type


def selected_comp(frame_middle, list):
    global idfile
    SelectList = list.curselection()
    for i in SelectList:
        listQuestion.append(list.get(i))
    # crée un fichier avec en nom idfile.xml
    idfile += 1
    namelist = str(idfile) + '.xml'
    CreationXMLComp(listQuestion, namelist)
    listQuestion.clear()
    # cancel selection of the list
    list.selection_clear(0, END)
    listen()
    frame_middle.destroy()
    frame_middle_init(window)


def selected_form(frame_middle, list):
    global idfile
    SelectList = list.curselection()
    for i in SelectList:
        listQuestion.append(list.get(i))
    idfile += 1
    namelist = str(idfile)+".xml"
    CreationXMLForm(listQuestion, namelist)
    listQuestion.clear()
    list.selection_clear(0, END)
    listen()
    # refresh the frame
    frame_middle.destroy()
    frame_middle_init(window)


def suivant(frame_middle, window):
    global dataf
    global nbdata
    global nbcomp
    global nbforma

    if type == 1:
        if nbdata < nb_result:
            nbdata = nbdata + 1
            dataf = dataf + 3
            frame_middle.destroy()
            frame_middle_init(window)
    if type == 2:
        if nbdata < nb_result:
            dataf = dataf + 6+nbcomp[nbdata-1]+nbforma[nbdata-1]
            nbdata = nbdata + 1
            frame_middle.destroy()
            frame_middle_init(window)


def precedent(frame_middle, window):
    global dataf
    global nbdata
    global nbcomp
    global nbforma
    if type == 1:
        if nbdata > 1:
            nbdata = nbdata - 1
            dataf = dataf - 3
            frame_middle.destroy()
            frame_middle_init(window)
    if type == 2:
        if nbdata > 1:
            nbdata = nbdata - 1
            dataf = dataf - (6+nbcomp[nbdata-1]+nbforma[nbdata-1])
            frame_middle.destroy()
            frame_middle_init(window)


def refresh(frame_middle, window):
    frame_middle.destroy()
    frame_middle_init(window)


def frame_middle_init(window):

    global nb_result
    global nbcomp
    global nbforma
    global nb_result

    frame_middle = Frame(window, bg="#528860", bd=1, relief=SUNKEN)
    frame_middle.pack(side=TOP, expand=YES, anchor=N, ipady=2000)
    label3 = Label(frame_middle, text="Resultats", font=(
        "Times New Roman", 20), padx=2000, pady=0)
    label3.pack()

    # fonction pour rafraichir depuis un bouton
    refresh_action = partial(refresh, frame_middle, window)

    B5 = Button(frame_middle, text="Actualiser",
                width=10, height=3, command=refresh_action)
    B5.pack(side=BOTTOM, padx=0, pady=25, anchor=S)

    if nb_result >= 1:
        action_l3 = partial(precedent, frame_middle, window)
        action_l4 = partial(suivant, frame_middle, window)

        B3 = Button(frame_middle, text="Précedent",
                    width=10, height=3, command=action_l3)
        B3.pack(side=LEFT, padx=50, pady=10, anchor=S)
        B4 = Button(frame_middle, text="Suivant",
                    width=10, height=3, command=action_l4)
        B4.pack(side=RIGHT, padx=50, pady=10, anchor=S)

        texteLabel = Label(frame_middle, bg="#528860", text=""+str(nbdata)+"/"+str(nb_result), font=(
            "Times New Roman", 20))
        texteLabel.pack(side=BOTTOM, padx=0, pady=10, anchor=S)

        if type == 1:
            #-------------Nom-------------#
            texteLabe2 = Label(frame_middle, bg="#528860", text="Prénom :", font=(
                "Times New Roman", 20))
            texteLabe2.place(relx=0.01, rely=0.1, height=30, width=100)
            texteLabe2 = Label(frame_middle, bg="#528860", text=""+str(tuple[0+dataf]), font=(
                "Times New Roman", 20))
            texteLabe2.place(relx=0.55, rely=0.1, height=30, width=100)
            #-----------Prénom------------#
            texteLabe3 = Label(frame_middle, bg="#528860", text="Nom:", font=(
                "Times New Roman", 20))
            texteLabe3.place(relx=0.01, rely=0.15, height=30, width=100)
            texteLabe3 = Label(frame_middle, bg="#528860", text=""+str(tuple[1+dataf]), font=(
                "Times New Roman", 20))
            texteLabe3.place(relx=0.55, rely=0.15, height=30, width=100)
            #----------Numéro-------------#
            texteLabe4 = Label(frame_middle, width=2006, bg="#528860", text=""+str(tuple[2+dataf]), font=(
                "Times New Roman", 20))
            texteLabe4.place(relx=0.55, rely=0.2, height=30, width=150)
            texteLabe4 = Label(frame_middle, width=2006, bg="#528860", text="Numéro:", font=(
                "Times New Roman", 20))
            texteLabe4.place(relx=0.01, rely=0.2, height=30, width=100)

        if type == 2:
            #-------------Nom-------------#
            texteLabe2 = Label(frame_middle, bg="#528860", text="Prénom :", font=(
                "Times New Roman", 20))
            texteLabe2.place(relx=0.01, rely=0.1, height=30, width=100)
            texteLabe2 = Label(frame_middle, bg="#528860", text=""+str(tuple[0+dataf]), font=(
                "Times New Roman", 20))
            texteLabe2.place(relx=0.55, rely=0.1, height=30, width=100)
            #-----------Prénom------------#
            texteLabe3 = Label(frame_middle, bg="#528860", text="Nom:", font=(
                "Times New Roman", 20))
            texteLabe3.place(relx=0.01, rely=0.15, height=30, width=100)
            texteLabe3 = Label(frame_middle, bg="#528860", text=""+str(tuple[1+dataf]), font=(
                "Times New Roman", 20))
            texteLabe3.place(relx=0.55, rely=0.15, height=30, width=100)
            #----------Numéro-------------#
            texteLabe4 = Label(frame_middle, width=2006, bg="#528860", text=""+str(tuple[2+dataf]), font=(
                "Times New Roman", 20))
            texteLabe4.place(relx=0.35, rely=0.2, height=30, width=250)
            texteLabe4 = Label(frame_middle, width=2006, bg="#528860", text="Numéro:", font=(
                "Times New Roman", 20))
            texteLabe4.place(relx=0.01, rely=0.2, height=30, width=100)
            #----------Adresse-------------#
            texteLabe5 = Label(frame_middle, width=2006, bg="#528860", text=""+str(tuple[3+dataf]), font=(
                "Times New Roman", 15))
            texteLabe5.place(relx=0.35, rely=0.25, height=30, width=250)
            texteLabe5 = Label(frame_middle, width=2006, bg="#528860", text="Adresse:", font=(
                "Times New Roman", 20))
            texteLabe5.place(relx=0.01, rely=0.25, height=30, width=100)
            #----------github-------------#
            texteLabe6 = Label(frame_middle, width=2006, bg="#528860", text=""+str(tuple[4+dataf]), font=(
                "Times New Roman", 15))
            texteLabe6.place(relx=0.35, rely=0.3, height=30, width=250)
            texteLabe6 = Label(frame_middle, width=2006, bg="#528860", text="Github:", font=(
                "Times New Roman", 20))
            texteLabe6.place(relx=0.01, rely=0.3, height=30, width=100)
            #----------linkedin-------------#
            texteLabe7 = Label(frame_middle, width=2006, bg="#528860", text=""+str(tuple[5+dataf]), font=(
                "Times New Roman", 15))
            texteLabe7.place(relx=0.35, rely=0.35, height=30, width=250)
            texteLabe7 = Label(frame_middle, width=2006, bg="#528860", text="Linkedin:", font=(
                "Times New Roman", 20))
            texteLabe7.place(relx=0.01, rely=0.35, height=30, width=100)

            yscrollbar1 = Scrollbar(frame_middle)
            yscrollbar1.place(relx=0.01, rely=0.45, height=200, width=20)
            yscrollbar2 = Scrollbar(frame_middle)
            yscrollbar2.place(relx=0.94, rely=0.45, height=200, width=20)

            liste_comp = Listbox(frame_middle, font=(
                "Times New Roman", 15))
            liste_comp.place(relx=0.08, rely=0.45, height=200,
                             width=140)
            i = 6
            while i < 6 + nbcomp[nbdata-1]:
                liste_comp.insert(END, tuple[i+dataf])
                i += 1

            liste_form = Listbox(frame_middle, font=(
                "Times New Roman", 15))
            liste_form.place(relx=0.50, rely=0.45, height=200,
                             width=170)

            i = 6 + nbcomp[nbdata-1]
            while i < 6 + nbcomp[nbdata-1] + nbforma[nbdata-1]:
                liste_form.insert(END, tuple[i+dataf])
                i += 1
            liste_comp.config(yscrollcommand=yscrollbar1.set)
            liste_form.config(yscrollcommand=yscrollbar2.set)
    return frame_middle


# Fpnction qui ecoute si un nouveau fichier est présent dans le dossier Reponses
def listen():
    global nb_result
    global tuple
    global type
    global nbcomp
    global nbforma
    global dataf
    global nbdata

    time.sleep(1)
    for file in os.listdir("Reponses"):
        if file.endswith(".xml"):
            with open("Reponses/"+file, "r") as f:
                # reset des variables
                dataf = 0
                nbcomp = [0 for i in range(100)]
                nbforma = [0 for i in range(100)]
                nb_result = 0
                type = 0
                nbdata = 1
                tuple = []
                nb_result, tuple, type = readXML(f)
            f.close()
            # déplacer le fichier dans le dossier Histo_Rep
            shutil.move("Reponses/"+file, "HistoReponses/"+file)
            break


#---------------------------------------------------MAIN-----------------------------------------------------#
db, cursor = ressources.ConnectDB()
ressources.ListeCompFromBase(cursor, listcomp)
ressources.ListeFormaFromBase(cursor, listforma)
ressources.DisconnectDB(cursor, db)

window = Tk()
window.title('Programme metier')
window.geometry("720x480")
window.minsize(200, 100)
window.maxsize(1080, 720)

frame_left = Frame(window, bg="#8BC49A", bd=1, relief=SUNKEN)
frame_left.pack(side=LEFT, expand=YES, fill=Y, anchor=NW)

frame_right = Frame(window, bg="#8BC49A", bd=1, relief=SUNKEN)
frame_right.pack(side=RIGHT, expand=YES, fill=Y, anchor=NE)

yscrollbar1 = Scrollbar(frame_left)
yscrollbar1.pack(side=RIGHT, fill=Y)
yscrollbar2 = Scrollbar(frame_right)
yscrollbar2.pack(side=LEFT, fill=Y)

label1 = Label(frame_left, text="Demande des infos CV en fonction des compétences", font=(
    "Times New Roman", 10), padx=10, pady=10)
label2 = Label(frame_right, text="Demande des infos personnes en fonction des formations", font=(
    "Times New Roman", 10), padx=10, pady=10)

label1.pack()
label2.pack()

list1 = Listbox(frame_left, selectmode=MULTIPLE,
                yscrollcommand=yscrollbar1.set)
list2 = Listbox(frame_right, selectmode=MULTIPLE,
                yscrollcommand=yscrollbar2.set)

frame_middle = frame_middle_init(window)


action_l1 = partial(selected_comp, frame_middle, list1)
action_l2 = partial(selected_form, frame_middle, list2)

B1 = Button(frame_left, text="Recherche CV", command=action_l1)
B1.pack(padx=20, pady=20)

B2 = Button(frame_right, text="Recherche Personnes", command=action_l2)
B2.pack(padx=20, pady=20)

list1.pack(padx=10, pady=10, expand=YES, fill="both")
list2.pack(padx=10, pady=10, expand=YES, fill="both")

for comp_item in range(len(listcomp)):
    list1.insert(END, listcomp[comp_item])
    list1.itemconfig(comp_item, bg="gray")

for form_item in range(len(listforma)):
    list2.insert(END, listforma[form_item])
    list2.itemconfig(form_item, bg="gray")

yscrollbar1.config(command=list1.yview)
yscrollbar2.config(command=list2.yview)

window.mainloop()
