
class Corso:
    def __init__(self, codins, crediti, nome, pd):
        self.codins= codins
        self.crediti = crediti
        self.nome = nome
        self.pd = pd

    def __str__(self):
        return f"{self.nome} {self.codins}"

    def getCodins(self):
        return self.codins

# if __name__ == '__main__':
#     c = Corso("abc", 6, "matte", "<NAME>" )
#     print(c.codins)
#     print(c.crediti)
#     print(c)
