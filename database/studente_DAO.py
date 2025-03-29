# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.studente import Studente


class StudenteDAO:
    def __init__(self):
        pass

    def getStudenti(self):
        cnx = get_connection()
        cursor = cnx.cursor()
        query = """select * from studente"""
        lines = cursor.execute(query)
        studenti = []
        for line in lines:
            studenti.append(Studente(line[0], line[1], line[2], line[3]))
        cnx.close()
        return studenti

    def getStudentiCorso(self, codins):
        studenti = []
        cnx = get_connection()
        cursor = cnx.cursor()
        query = """select s.nome, s.cognome, i.matricola from studente s, iscrizione i where i.matricola = s.matricola and i.codins = %s"""
        cursor.execute(query, (codins,))
        for line in cursor:
            studenti.append(f"{line[0]} {line[1]} ({line[2]})")
        return studenti

    def getStudenteByMatricola(self, matricola):
        cnx = get_connection()
        cursor = cnx.cursor()
        query = """select nome, cognome from studente where matricola = %s"""
        cursor.execute(query, (matricola,))
        return cursor.fetchone()