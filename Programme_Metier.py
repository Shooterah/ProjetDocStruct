import ressources
from tkinter import *
from functools import partial
import xml.dom.minidom
from datetime import datetime
import socket
from os import listdir
from os.path import isfile, join

listcomp = []
listforma = []
listQuestion = []
idfile = 0


def CreationXMLComp(listQuestion, namefile):

    doc = xml.dom.minidom.parseString("<question/>")
    tree = doc.documentElement
    tree.setAttribute("typeQuestion", "CompFromCv")
    #---------------Capsule envoyeur--------------------#
    envoyeur = doc.createElement("envoyeur")
    # ajout ligne id et de son texte 1
    id = doc.createElement("id")
    textid = doc.createTextNode("1")
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


def CreationXMLForm(listQuestion, namefile):
    doc = xml.dom.minidom.parseString("<question/>")
    tree = doc.documentElement
    tree.setAttribute("typeQuestion", "PersFromForma")
    #---------------Capsule envoyeur--------------------#
    envoyeur = doc.createElement("envoyeur")
    # ajout ligne id et de son texte 1
    id = doc.createElement("id")
    textid = doc.createTextNode("1")
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

# fonction qui lit un document xml et qui renvoie son nom son prenom et son telephone


def readXML(namefile):
    doc = xml.dom.minidom.parse("Reponses/"+namefile)
    tree = doc.documentElement
    typerep = tree.getAttribute("typeReponse")

    if typerep == "RepPersFromForma":
        i = 0
        personnes = tree.getElementsByTagName("personnes")
        while i <= len(personnes):
            for personne in personnes:
                nom = personne.getElementsByTagName("nom")[i]
                nom = nom.firstChild.data
                prenom = personne.getElementsByTagName("prenom")[i]
                prenom = prenom.firstChild.data
                telephone = personne.getElementsByTagName("telephone")[i]
                telephone = telephone.firstChild.data
                print(nom, prenom, telephone)
            i = i+1
    elif typerep == "RepCompFromCv":
        j = 0
        CVS = tree.getElementsByTagName("CVS")
        while j <= len(CVS):
            for CV in CVS:
                nom = CV.getElementsByTagName("nom")[j]
                nom = nom.firstChild.data
                prenom = CV.getElementsByTagName("prenom")[j]
                prenom = prenom.firstChild.data
                telephone = CV.getElementsByTagName("telephone")[j]
                telephone = telephone.firstChild.data
                mail = CV.getElementsByTagName("mail")[j]
                mail = mail.firstChild.data
                github = CV.getElementsByTagName("github")[j]
                github = github.firstChild.data
                linkedin = CV.getElementsByTagName("linkedin")[j]
                linkedin = linkedin.firstChild.data
                print(nom, prenom, telephone, mail, github, linkedin)
                competences = CV.getElementsByTagName("competences")[j]
                competence = competences.getElementsByTagName("competence")
                for comp in competence:
                    comp = comp.firstChild.data
                    print(comp)
                formations = CV.getElementsByTagName("formations")[j]
                formation = formations.getElementsByTagName("formation")
                for form in formation:
                    form = form.firstChild.data
                    print(form)
            j = j+1


def selected_comp(list):
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


def selected_form(list):
    global idfile
    SelectList = list.curselection()
    for i in SelectList:
        listQuestion.append(list.get(i))
    idfile += 1
    namelist = str(idfile)+".xml"
    CreationXMLForm(listQuestion, namelist)
    listQuestion.clear()
    list.selection_clear(0, END)


db, cursor = ressources.ConnectDB()
ressources.ListeCompFromBase(cursor, listcomp)
ressources.ListeFormaFromBase(cursor, listforma)
ressources.DisconnectDB(cursor, db)

fichiers = [f for f in listdir("Reponses") if isfile(join("Reponses", f))]
for file in fichiers:
    readXML(file)

window = Tk()
window.title('Programme metier')
window.geometry("1080x720")
window.minsize(1080, 720)
xmax = window.winfo_height()
ymax = window.winfo_width()

frame_left_top = Frame(window, bg="#8BC49A", bd=1, relief=SUNKEN)
frame_left_top.pack(side=LEFT, expand=YES, fill=Y, anchor=NW)

frame_right_top = Frame(window, bg="#8BC49A", bd=1, relief=SUNKEN)
frame_right_top.pack(side=RIGHT, expand=YES, fill=Y, anchor=NE)

frame_left_middle = Frame(window, bg="#528860", bd=1, relief=SUNKEN)
frame_left_middle.pack(side=TOP, ipadx=500, ipady=500, fill=Y)

yscrollbar1 = Scrollbar(frame_left_top)
yscrollbar1.pack(side=RIGHT, fill=Y)
yscrollbar2 = Scrollbar(frame_right_top)
yscrollbar2.pack(side=LEFT, fill=Y)

label1 = Label(frame_left_top, text="Demande des infos CV en fonction des compétences", font=(
    "Times New Roman", 10), padx=10, pady=10)
label2 = Label(frame_right_top, text="Demande des infos personnes en fonction des formations", font=(
    "Times New Roman", 10), padx=10, pady=10)
label3 = Label(frame_left_middle, text="Resultats", font=(
    "Times New Roman", 10), padx=2000, pady=10)
label1.pack()
label2.pack()
label3.pack(side=TOP)

list1 = Listbox(frame_left_top, selectmode=MULTIPLE,
                yscrollcommand=yscrollbar1.set)
list2 = Listbox(frame_right_top, selectmode=MULTIPLE,
                yscrollcommand=yscrollbar2.set)

action_l1 = partial(selected_comp, list1)
action_l2 = partial(selected_form, list2)

B1 = Button(frame_left_top, text="Recherche CV", command=action_l1)
B1.pack(padx=20, pady=20)
B2 = Button(frame_right_top, text="Recherche Personnes", command=action_l2)
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
