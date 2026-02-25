class Sport:
    def __init__(self, name, energie_perdue):
        self.name = name
        self.energie_perdue = energie_perdue
    
    def faire_sport(self, vie):
        vie.aj_val(-self.energie_perdue)
        return vie.get_val()
    
    def get_energie_perdue(self):
        return self.energie_perdue