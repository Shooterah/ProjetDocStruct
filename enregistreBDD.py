# Function that send data to a database (MySQL)

def sendToDB(prenom, nom, mail,tel, linkedin, github):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="docstruc"
        )
        cursor = db.cursor()
        sql = "INSERT INTO candidats(Nom, Prenom, Mail, Tel, Linkedin, Github) VALUES (%s, %s, %s, %s, %s, %s,)"
        val = (nom, prenom, mail, tel, linkedin, github)
        cursor.execute(sql, val)
        db.commit()
        print(cursor.rowcount, "record inserted.")
    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))
    finally:
        if (db.is_connected()):
            cursor.close()
            db.close()
            print("MySQL connection is closed")

# fonction qui lit le fichier xml qui contient les données d'un cv


def readXML():
    tree = ET.parse('cv.xml')
    root = tree.getroot()
    for child in root:
        prenom = child.find('prenom').text
        nom = child.find('nom').text
        mail = child.find('mail').text
        linkedin = child.find('linkedin').text
        github = child.find('github').text
        diplome = child.find('diplome').text
        tel = child.find('tel').text
        for competance in child.findall('competances'):
            competence = competance.text
