class Studente:
    def __init__(self, matricola, cognome, nome ,cds):
        self._matricola = matricola
        self._cognome = cognome
        self._nome = nome
        self._cds = cds

    @property
    def matricola(self):
        return self._matricola
    @property
    def cognome(self):
        return self._cognome
    @property
    def nome(self):
        return self._nome
    @property
    def cds(self):
        return self._cds
