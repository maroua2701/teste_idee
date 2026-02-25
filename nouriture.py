class nourriture:
    def __init__(self, nom, energie):
        self.nom = nom
        self.energie = energie

    def manger(self, vie):
        vie.aj_val(self.energie)
        return vie.get_val()

    def get_energie(self):
        return self.energie