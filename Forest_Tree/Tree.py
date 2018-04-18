from Forest_Tree import TrainData, Node, Leaf


class Tree:

    def __init__(self, path=""):
        self.houses_for_train = TrainData.TrainData(path)
        self.tree = None
        self.build()
        self.special = False

    def build(self):
        self.tree = self._build_tree(self.houses_for_train)

    def _build_tree(self, houses_for_train):
        if houses_for_train.return_entropie() == 0:
            return Leaf.Leaf(houses_for_train.list_houses[0].classe)
        if len(houses_for_train.list_att) == 0:
            max, final_classe = 0, ""
            for classe in houses_for_train.return_classe_name():
                houses = houses_for_train.return_houses_with_same_classe(classe)
                if len(houses) > max:
                    max, final_classe = len(houses), classe
            return Leaf.Leaf(final_classe)

        att_to_test = houses_for_train.return_best_att()
        node = Node.Node(att_to_test)
        for value in houses_for_train.return_all_value_from_att(att_to_test):
            houses = houses_for_train.return_houses_with_same_att_value(att_to_test, value)
            node.childs[value] = self._build_tree(houses)
        return node

    def classify(self, house):
        current_node = self.tree
        if self.special:
            unknown = True
            for att in house.house_att.values():
                if unknown and str(att) != '0' and att.lower() != "na":
                    unknown = False
            if unknown:
                house.classe = "Unknown"
                return
        try:
            while not isinstance(current_node, Leaf.Leaf):
                value = house.house_att[current_node.att_to_test]
                current_node = current_node.childs[value]
            house.classe = current_node.classe
        except KeyError:
            house.classe = "unknown"

    def set_special(self, bool):
        self.special = bool

    def is_alive(self):
        return "Tree is alive"
