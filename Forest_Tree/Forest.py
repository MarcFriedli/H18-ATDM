import Forest_Tree.Tree as Tree
from Test_Tree import Test_Functions as Setup
import Setup_Scripts.Config as Config


class Forest:

    def __init__(self, liste_tree):
        self.forest = {}
        for tree in liste_tree:
            self.forest[tree] = Tree.Tree(f"../Train_Files/train_tree{tree}.csv")
        self.class_name = Config.class_name

    def config_special_tree(self, liste_tree):
        for tree in liste_tree:
            self.forest[tree].set_special(True)

    def pondere_classe(self, classe, trust):
        guess_class = {}
        try:
            class_index = self.class_name.index(classe)
            if class_index == 0:
                guess_class[self.class_name[class_index]] = trust[0]
                guess_class[self.class_name[class_index + 1]] = trust[1] / 2
            elif class_index == 9:
                guess_class[self.class_name[class_index - 1]] = trust[1] / 2
                guess_class[self.class_name[class_index]] = trust[0]
            else:
                guess_class[self.class_name[class_index - 1]] = trust[1] / 2
                guess_class[self.class_name[class_index]] = trust[0]
                guess_class[self.class_name[class_index + 1]] = trust[1] / 2
        except ValueError:
            """Si un arbre n'a pas pu catégorisé la maison"""
            pass
        return guess_class

    def ponder_trust(self, classe, trust):
        guess_class = {}
        try:
            class_index = self.class_name.index(classe)
            if class_index == 0:
                try:
                    guess_class[self.class_name[class_index]] = trust[classe][0]
                except TypeError:
                    pass
                guess_class[self.class_name[class_index + 1]] = trust[classe][1] / 2
            elif class_index == 9:
                guess_class[self.class_name[class_index - 1]] = trust[classe][1] / 2
                guess_class[self.class_name[class_index]] = trust[classe][0]
            else:
                guess_class[self.class_name[class_index - 1]] = trust[classe][1] / 2
                guess_class[self.class_name[class_index]] = trust[classe][0]
                guess_class[self.class_name[class_index + 1]] = trust[classe][1] / 2
        except ValueError:
            pass
        except IndexError:
            pass
        return guess_class

    def return_value_trust(self, classes, trusts):
        final_guess_dic = {
            "c1": 0,
            "c2": 0,
            "c3": 0,
            "m1": 0,
            "m2": 0,
            "m3": 0,
            "m4": 0,
            "e1": 0,
            "e2": 0,
            "e3": 0,
        }
        for i in range(0, 3):
            toto = self.ponder_trust(classes[i], trusts[i])
            for key, value, in toto.items():
                final_guess_dic[key] += value
        return final_guess_dic


    def return_mode(self, array):
        return max(set(array), key=array.count)


    def return_class_from_avg(self, array):
        indexs = []
        for item in array:
            indexs.append(self.class_name.index(item))
        cpt = 0
        for item in indexs:
            cpt += item
        return int(cpt / len(indexs))

    def determine_classe(self, house, fields_by_tree):
        possibility = []
        pondere_dic = {
            "c1": 0,
            "c2": 0,
            "c3": 0,
            "m1": 0,
            "m2": 0,
            "m3": 0,
            "m4": 0,
            "e1": 0,
            "e2": 0,
            "e3": 0,
        }
        for key, tree in self.forest.items():
            try:
                house_to_test = Setup.return_house_by_att(house, fields_by_tree[key])
                tree.classify(house_to_test)
                guess_classe = house_to_test.classe
                possibility.append(guess_classe)
                ponderation = self.pondere_classe(guess_classe, Config.tree_trust[key])
                for key, value, in ponderation.items():
                    pondere_dic[key] += value
            except IndexError:
                pass

        pondere_guesse = "c1"
        for key in pondere_dic.keys():
            if pondere_dic[key] > pondere_dic[pondere_guesse]:
                pondere_guesse = key
        possibility = [x for x in possibility if x.lower() != "unknown"]
        mode_guess = self.return_mode(possibility)
        avg_guess = self.class_name[self.return_class_from_avg(possibility)]

        final_guess = "c1"
        ponderation = self.return_value_trust([pondere_guesse, avg_guess, mode_guess], [Config.pondere_trust, Config.avg_trust, Config.mode_trust])
        for key in ponderation.keys():
            if ponderation[key] > ponderation[final_guess]:
                final_guess = key

        try:
            return final_guess
        except ValueError:
            """
                Si la forêt n'a pas réussi à trouver l'élément. Il s'agit d'une sécurité, ce n'est pas sencé arriver.
            """
            print("Can't determinate the house")
