import flet as ft

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txtIn = None
        self.btn_cercaiscritti = None
        self._lv = None
        self._ddCorso = None
        self.inserisciMatricola = None
        self.nome = None
        self.cognome=None
        self.cercaStudente = None
        self.cercaCorsi = None
        self.iscrivi = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self._ddCorso = ft.Dropdown(label="Seleziona corso", width=self._page.window_width*0.5)#inserire il nome dei corsi dal database
        self._controller.fill_ddCorso()

        # button for the "hello" reply
        self.btn_cercaiscritti = ft.ElevatedButton(text="Cerca iscritti", on_click=self._controller.handle_show_iscritti)
        self.inserisciMatricola = ft.TextField(label="matricola", expand=1)
        self.nome = ft.TextField(label="nome", expand=1, read_only=True)
        self.cognome = ft.TextField(label="cognome", expand=1, read_only=True)
        self._lv = ft.ListView(expand=1)
        self.cercaStudente = ft.ElevatedButton(text="cerca studente", on_click = self._controller.handle_cercaStudente, expand=1)
        self.cercaCorsi = ft.ElevatedButton(text="cerca corsi", on_click=self._controller.handle_cercaCorsi, expand=1)
        self.iscrivi = ft.ElevatedButton(text="iscriviti", on_click=self._controller.handle_iscriviti, expand=1)




        row1 = ft.Row([self._ddCorso, self.btn_cercaiscritti],
                      alignment=ft.MainAxisAlignment.CENTER)
        row2 = ft.Row([self.inserisciMatricola, self.nome, self.cognome])
        row4 = ft.Row([self.cercaStudente, self.cercaCorsi, self.iscrivi])
        row3 = ft.Container(self._lv)

        self._page.add(row1, row2, row4, row3)

        # List View where the reply is printed
        # self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        # self._page.controls.append(self.txt_result)
        # self._page.update()



    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
