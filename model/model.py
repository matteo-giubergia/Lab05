from database.corso_DAO import CorsoDAO
from database.studente_DAO import StudenteDAO

class Model:
    def __init__(self):
        self._corsoDAO = CorsoDAO()
        self._studenteDAO = StudenteDAO()


    def corsi(self):
        return self._corsoDAO.getCorsi()    #restituisce la lista di oggetti corso

    def studenti(self):
        return self._studenteDAO.getStudenti() #restituisce la lista di oggetti studente

    def getNumeroIscrittiCorso(self, codins):
        lunghezza = len(self._studenteDAO.getStudentiCorso(codins))
        return lunghezza


    def getStudentiperCorso(self, codins):
        return self._studenteDAO.getStudentiCorso(codins) #lista di tuple

    def getStudenteMatricola(self, matricola):
        return self._studenteDAO.getStudenteByMatricola(matricola)

    def getCorsiStudentePerMatricola(self, matricola):
        return self._corsoDAO.corsiByMatricola(matricola)

    def iscrizione(self, matricola, codins):
        return self._corsoDAO.iscrivi(matricola, codins)


    def nomeCorso(self, codins):
        return self._corsoDAO.getNomeCorso(codins)

    def controlloIscrizione(self):
        return self._corsoDAO.controlloIscrizione()