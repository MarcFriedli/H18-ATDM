class House:
    def __init__(self, att_names, att_values, classe=""):
        self.classe = classe
        self.house_att = {}
        for i in range(len(att_names)):
            try:
                self.house_att[att_names[i].lower()] = att_values[i].lower()
            except AttributeError:
                self.house_att[str(att_names[i])] = att_values[i].lower()
