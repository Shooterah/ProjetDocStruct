import os
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
dataf = 0
nb_result = 0
nbdata = 1
tuple = ()


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

 #-------------------Création D'UN XML de formations---------------------#
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

 #-------------------LECTURE D'UN XML---------------------#
def readXML(namefile):
    doc = xml.dom.minidom.parse("Reponses/"+namefile)
    tree = doc.documentElement
    typerep = tree.getAttribute("typeReponse")
    type = 0
    
    if typerep == "RepPersFromForma":

        i = 0;type = 1;tuplepers = ()

        personne = tree.getElementsByTagName("personne")
        for pers in personne:
            nom = pers.getElementsByTagName("nom")
            nom = nom.item(0).firstChild.nodeValue
            prenom = pers.getElementsByTagName("prenom")
            prenom = prenom.item(0).firstChild.nodeValue
            telephone = pers.getElementsByTagName("telephone")
            telephone = telephone.item(0).firstChild.nodeValue
            tuplepers = tuplepers + (nom,prenom,telephone)
            i = i+1
        return i,tuplepers,type
    
    if typerep == "RepCompFromCv":

        j = 0;x=0;y=0;type = 1;tupleCV = ()

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
            tupleCV = tupleCV + (nom,prenom,telephone,mail,github,linkedin)
            competence = cv.getElementsByTagName("competence")
            for comp in competence:
                comp = comp.firstChild.nodeValue
                tupleCV = tupleCV + ("Comp",comp)
            formation = cv.getElementsByTagName("formation")
            for form in formation:
                form = form.firstChild.nodeValue
                tupleCV = tupleCV + ("Form",form)
            j = j+1
        return j,tupleCV,type


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

def suivant(frame_middle,window):
    global dataf
    global nbdata
    global nb_result

    if nbdata == nb_result:
        nbdata = nbdata - nb_result+1
        dataf = (dataf - 3*nb_result)+3
        frame_middle.destroy()
        frame_middle_init(window)
    else:
        nbdata = nbdata + 1 
        dataf = dataf + 3
        frame_middle.destroy()
        frame_middle_init(window)

def precedent(frame_middle,window):
    global dataf
    global nbdata
    global nb_result
    if nbdata == 1:
        nbdata = nbdata + nb_result-1 
        dataf = dataf + (3*nb_result)-3
        frame_middle.destroy()
        frame_middle_init(window)
    else:
        nbdata = nbdata - 1 
        dataf = dataf - 3
        frame_middle.destroy()
        frame_middle_init(window)


def frame_middle_init(window):
    global nb_result
    frame_middle = Frame(window, bg="#528860", bd=1, relief=SUNKEN)
    frame_middle.pack(side=TOP,expand=YES , anchor=N ,ipady=2000)
    label3 = Label(frame_middle, text="Resultats", font=(
        "Times New Roman", 20), padx=2000, pady=0)
    label3.pack()

    if nb_result >= 1:
        action_l3 = partial(precedent,frame_middle,window)
        action_l4 = partial(suivant,frame_middle,window)

        B3 = Button(frame_middle, text="Précedent",width = 10,height=3 , command=action_l3)
        B3.pack(side=LEFT,padx=50, pady=50,anchor=S)
        B4 = Button(frame_middle, text="Suivant", width = 10,height=3, command=action_l4)
        B4.pack(side=RIGHT,padx=50, pady=50,anchor=S)

        texteLabel = Label(frame_middle,bg="#528860", text = ""+str(nbdata)+"/"+str(nb_result) ,font=(
            "Times New Roman", 20))
        texteLabel.pack(side=BOTTOM,padx=0, pady=50,anchor=S)

        if type == 1 :
            #-------------Nom-------------#
            texteLabe2 = Label(frame_middle, bg="#528860" ,text = "Nom :",font=(
            "Times New Roman", 20))
            texteLabe2.place(relx=0.2, rely=0.2, height=30, width=100)
            texteLabe2 = Label(frame_middle, bg="#528860", text = ""+str(tuple[0+dataf]) ,font=(
            "Times New Roman", 20))
            texteLabe2.place(relx=0.6, rely=0.2, height=30, width=100)
            #-----------Prénom------------#
            texteLabe3 = Label(frame_middle, bg="#528860", text = "Prénom:" ,font=(
            "Times New Roman", 20))
            texteLabe3.place(relx=0.2, rely=0.4, height=30, width=100)
            texteLabe3 = Label(frame_middle, bg="#528860", text = ""+str(tuple[1+dataf]) ,font=(
            "Times New Roman", 20))
            texteLabe3.place(relx=0.6, rely=0.4, height=30, width=100)
            #----------Numéro-------------#
            texteLabe4 = Label(frame_middle,width=2006,bg="#528860", text = ""+str(tuple[2+dataf]) ,font=(
            "Times New Roman", 15))
            texteLabe4.place(relx=0.6, rely=0.6, height=30, width=150)
            texteLabe4 = Label(frame_middle,width=2006,bg="#528860", text = "Numéro:",font=(
            "Times New Roman", 20))
            texteLabe4.place(relx=0.2, rely=0.6, height=30, width=100)



#---------------------------------------------------MAIN-----------------------------------------------------#

db, cursor = ressources.ConnectDB()
ressources.ListeCompFromBase(cursor, listcomp)
ressources.ListeFormaFromBase(cursor, listforma)
ressources.DisconnectDB(cursor, db)

fichiers = [f for f in listdir("Reponses") if isfile(join("Reponses", f))]
for file in fichiers:
    nb_result,tuple,type = readXML(file)
    print(tuple)


window = Tk()
window.title('Programme metier')
window.geometry("1080x720")
window.minsize(1080, 720)

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

action_l1 = partial(selected_comp, list1)
action_l2 = partial(selected_form, list2)

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

frame_middle_init(window)

window.mainloop()