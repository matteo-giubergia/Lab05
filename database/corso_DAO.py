# Add whatever it is needed to interface with the DB Table corso
from model.corso import Corso
from database.DB_connect import get_connection

class CorsoDAO:
    def __init__(self):
        pass

    def getCorsi(self):
        cnx = get_connection()
        cursor = cnx.cursor()
        query = """select * from corso"""
        cursor.execute(query)
        corsi = []
        for line in cursor:
            corsi.append(Corso(line[0], line[1], line[2], line[3]))
            print(line)
        cnx.close()
        return corsi

    def corsiByMatricola(self, matricola):
        cnx = get_connection()
        cursor = cnx.cursor()
        query = """select c.nome from corso c, iscrizione i where c.codins = i.codins and matricola = %s"""
        cursor.execute(query, (matricola,))
        corsi = []
        for c in cursor.fetchall():
            corsi.append(c)
        cnx.close()
        return corsi

    def iscrivi(self, matricola, codins):
        cnx = get_connection()
        cursor = cnx.cursor()
        query = """INSERT INTO iscrizione (matricola, codins) VALUES(%s, %s)"""
        cursor.execute(query, (matricola, codins))
        cnx.commit()
        cnx.close()

    def getNomeCorso(self, codins):
        cnx = get_connection()
        cursor = cnx.cursor()
        query = """select nome from corso where codins = %s"""
        cursor.execute(query, (codins,))
        nomeCorso = cursor.fetchone()[0]
        cnx.close()
        return nomeCorso

    def controlloIscrizione(self):
        iscrizioni = []
        cnx = get_connection()
        cursor = cnx.cursor()
        query= """select codins, matricola from iscrizione"""
        cursor.execute(query)
        for codins, matricola in cursor.fetchall():
            iscrizioni.append((codins,matricola))
        cnx.close()
        return iscrizioni