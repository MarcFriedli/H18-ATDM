from math import log
from Forest_Tree import House


class TrainData:

    def __init__(self, path=""):
        if path == "":
            self.list_att = list()
            self.list_houses = list()
        else:
            with open(path, 'r') as file:
                self.list_att = \
                    file.readline().lower().strip().split(',')
                self.list_houses = self.setup_list_house(
                    file.read().strip().lower().split('\n'),
                    self.list_att
                )

    def __len__(self):
        return len(self.list_houses)

    @staticmethod
    def setup_list_house(houses, att_names):
        house_list = []
        for house in houses:
            attributs = house.lower().strip().split(',')
            classe = attributs[-1] if len(attributs) != len(att_names) else ""
            house_list.append(House.House(att_names, attributs[:len(att_names)], classe))
        return house_list

    def return_classe_name(self):
        list_houses = []
        for house in self.list_houses:
            if not house.classe in list_houses:
                list_houses.append(house.classe)
        return list_houses

    def return_houses_with_same_classe(self, classe):
        houses = TrainData()
        houses.list_att = self.list_att[:]
        for house in self.list_houses:
            if house.classe == classe:
                houses.list_houses.append(house)
        return houses

    def return_houses_with_same_att_value(self, attribut, value):
        houses = TrainData()
        houses.list_att = self.list_att[:]
        houses.list_att.remove(attribut)
        for house in self.list_houses:
            if house.house_att[attribut] == value:
                houses.list_houses.append(house)
        return houses

    def return_entropie(self):
        entropie = 0
        for classe in self.return_classe_name():
            houses = self.return_houses_with_same_classe(classe)
            entropie += len(houses) * log(len(houses), 2)
        return log(len(self), 2) - entropie / len(self)

    def return_best_att(self):
        max, best_att = float("-inf"), ""
        for attribut in self.list_att:
            gain = self.benefit_entropie(attribut)
            if gain >= max:
                max, best_att = gain, attribut
        return best_att

    def return_all_value_from_att(self, attribut):
        values = []
        for house in self.list_houses:
            if not house.house_att[attribut] in values:
                values.append(house.house_att[attribut])
        return values

    def benefit_entropie(self, attribut):
        sum = 0
        for value in self.return_all_value_from_att(attribut):
            houses = self.return_houses_with_same_att_value(attribut, value)
            sum += len(houses) * houses.return_entropie()
        return self.return_entropie() - sum / len(self)

    def ratio_gain(self, attribut):
        split = self.split_entropie(attribut)
        benefit = self.benefit_entropie(attribut)
        return benefit / split if split != 0 else float("inf")

    def split_entropie(self, attribut):
        tot = 0
        for value in self.return_all_value_from_att(attribut):
            houses = self.return_houses_with_same_att_value(attribut, value)
            tot += len(houses) * log(len(houses), 2)
        return log(len(self), 2) - tot / len(self)
