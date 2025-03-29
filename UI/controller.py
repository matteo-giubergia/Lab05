import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_show_iscritti(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        # name = self._view.txt_name.value
        # if name is None or name == "":
        #     self._view.create_alert("Inserire il nome")
        #     return
        # self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        # self._view.update_page()
        self._view._lv.clean()
        coidns = self._view._ddCorso.value
        if coidns is None :
            self._view.create_alert("seleziona il corso!")
            return
        lunghezza = self._model.getNumeroIscrittiCorso(coidns)
        self._view._lv.controls.append(ft.Text(f"ci sono {lunghezza} iscritti: "))
        for line in self._model.getStudentiperCorso(coidns):
            self._view._lv.controls.append(ft.Text(line))
        self._view.update_page()

    def handle_cercaStudente(self, e):
        matricola = self._view.inserisciMatricola.value
        if matricola is None or matricola == "":
            self._view.create_alert("inserisci la matricola!")
            return

        nome, cognome = self._model.getStudenteMatricola(matricola)
        self._view.nome.value = nome
        self._view.cognome.value = cognome
        self._view.update_page()

    def handle_cercaCorsi(self, e):
        self._view._lv.clean()
        self._view._ddCorso.clean()
        matricola = self._view.inserisciMatricola.value
        if matricola is None or matricola == "":
            self._view.create_alert("inserisci la matricola!")
            return
        # nome, cognome = self._model.getStudenteMatricola(matricola)
        if self._model.getStudenteMatricola(matricola) is None:
            self._view.create_alert("matricola inesistente! ")
            return
        self._view._lv.controls.append(ft.Text(f"risultano {len(self._model.getCorsiStudentePerMatricola(matricola))} corsi: "))
        for c in self._model.getCorsiStudentePerMatricola(matricola):
            self._view._lv.controls.append(ft.Text(c[0]))
        self._view.update_page()


    def handle_iscriviti(self, e):
        self._view._lv.clean()
        self.handle_cercaStudente(e)
        matricola = self._view.inserisciMatricola.value

        codins = self._view._ddCorso.value #
        if codins is None :
            self._view.create_alert("scegli il corso cui  iscriverti")
            return
        # AGGIUNGERE CONTROLLO SE STUDENTE GIA ISCRITTO AL CORSO SELEZIONATO
        flag = self.checkIscrizione(codins, matricola)
        if flag == True:
            corso = self._model.nomeCorso(codins)
            self._model.iscrizione(matricola, codins)
            self._view._lv.controls.append(ft.Text(f"iscrizione della matricola {matricola} al corso {corso} effettuata"))
            self._view.update_page() # cnx.commit() per aggiornare i dati nel database
        else:
            self._view._lv.controls.append(ft.Text(f"la matricola {matricola} è già iscritta al corso!"))
            self._view.update_page()
            return

    def checkIscrizione(self, codins, matricola):
        iscrizioni = self._model.controlloIscrizione()
        for cod, matr in iscrizioni:
            if cod == codins and matr == matricola:
                return True


    def fill_ddCorso(self):
        corsi = self._model.corsi()
        for c in corsi:
            self._view._ddCorso.options.append(ft.dropdown.Option(key = c.getCodins(), text = c.__str__()))