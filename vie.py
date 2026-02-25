class Vie :
    def __init__(self, val = 50, val_max = 250):
        self.val = val
        self.val_max = val_max

    def aj_val(self, ajout):
        self.val += ajout
        if self.val > self.val_max:
            self.val = self.val_max
            return self.val
        elif self.val < 0:
            self.val = 0
            return self.val
        else:
            return self.val


    def get_val(self):
        return self.val