import MySQLdb


def ConnectDB():
    try:
        db = MySQLdb.connect(host="localhost", user="root",
                             passwd="", database="docstruc")
        cursor = db.cursor()
    except MySQLdb.Error as error:
        print("Failed to connect to Database{}".format(error))
    finally:
        print("Connected to the database")
        return db, cursor


def DisconnectDB(cursor, db):
    try:
        if (db):
            cursor.close()
            db.close()
    except MySQLdb.Error as error:
        print("Database is not Connected{}".format(error))
    finally:
        print("MySQL connection is closed")


def sendToDB(cursor, db, prenom, nom, mail, ListeNuméroTypeTmp, linkedin, github, listeCompétenceTmp, diplome):
    try:
        sql1 = "INSERT INTO candidats(Nom, Prenom, Mail, Tel, Linkedin, Github) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (nom, prenom, mail, str(ListeNuméroTypeTmp[0]), linkedin, github)
        cursor.execute(sql1, val)
        id = db.insert_id()
        db.commit()

        for comp in listeCompétenceTmp:
            sql2 = "SELECT idcomp FROM competences WHERE NomComp LIKE '" + \
                str(comp)+"'"
            cursor.execute(sql2)
            res = cursor.fetchone()
            sql3 = "INSERT INTO candiComp(idcand, idcomp) VALUES (%s, %s)"
            val = (id, res[0])
            cursor.execute(sql3, val)
            db.commit()

        for dipl in diplome:
            sql4 = "SELECT idform FROM formations WHERE NomForm LIKE '" + \
                str(dipl)+"'"
            cursor.execute(sql4)
            res = cursor.fetchone()
            sql5 = "INSERT INTO candiForm(idcand, idform) VALUES (%s, %s)"
            val = (id, res[0])
            cursor.execute(sql5, val)
            db.commit()

    except MySQLdb.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))
    finally:
        print("Insert "+prenom+" Successful")


def ListeCompFromBase(cursor, listcomp):
    sql2 = "SELECT NomComp FROM competences ORDER BY NomComp"
    cursor.execute(sql2)
    res = cursor.fetchall()
    for line in res:
        listcomp.append(line[0])


def ListeFormaFromBase(cursor, listforma):
    sql2 = "SELECT NomForm FROM formations ORDER BY NomForm"
    cursor.execute(sql2)
    res = cursor.fetchall()
    for line in res:
        listforma.append(line[0])


# Envoie une requête a la bdd pour trouver les CV correspondants

# Depuis une liste de competences
def askFromComp(licomp):
    sql = "SELECT Nom, Prenom, Mail, Tel, Linkedin, Github FROM 

    # SELECT * FROM `candidats`,`candicomp`,`competences` WHERE candidats.idCand = candicomp.idCand AND candicomp.idComp = competences.idComp AND competences.NomComp = "CSS"
     
