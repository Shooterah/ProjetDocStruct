# Function that send data to a database (MySQL)

def sendToDB(prenom, nom, mail, linkedin, github, diplome, tel, competence):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="cv"
        )
        cursor = db.cursor()
        sql = "INSERT INTO cv (prenom, nom, mail, linkedin, github, diplome, tel, competence) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (prenom, nom, mail, linkedin, github, diplome, tel, competence)
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
