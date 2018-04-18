import Setup_Scripts.Config as Config

"""
Script permettant de crée un fichier d'entrainement comprenant uniquement les données comprises dans la liste fields
à partir du fichier PATH
"""

# dictionnaire : clé : l'index du champs; valeurs : une liste contenant les valeurs du champs
values = {}


def return_all_values():
    """
    Ouvre le fichier dont on veut prétraiter les données.
    :return: Une liste contenant toutes les données.
    """
    with open(Config.TRAIN_PATH_RANGED, "r") as file:
        content = file.read()
        return content.split("\n")


def return_field_name_by_index(index):
    """
    :param index: L'index dont on cherche le nom.
    :return: Le nom associé à l'index.
    """
    with open(Config.FIELDS_PATH) as file:
        content = file.read()
        elements = content.split(",")
        return elements[index]


def copy_values(index):
    """
    Copie le contenu du champs dans le dictionnaire
    :param index: l'index du champ qu'on veut copier
    """
    elements = return_all_values()
    for element in elements:
        val = element.split(",")
        for i, v in enumerate(val):
            if i == index:
                values[index].append(v)
    del values[index][0]


def write_new_file(fields, new_file):
    """
    Ecris le contenu du dictionnaire value dans le nouveau fichier.
    """
    with open(new_file, "w") as file:
        nb_values = len(list(values.values())[0])
        for i in fields:
            file.write(return_field_name_by_index(i) + ",")
        file.write("\n")
        for j in range(0, nb_values - 1):
            for k in fields:
                try:
                    file.write(str(values[k][j]) + ",")
                except KeyError:
                    print(f"error with k = {k} and j = {j}")
            file.write("\n")


def create_file_with_field(fields, new_file):
    fields.sort()
    for field in fields:
        values[field] = []
        copy_values(field)
    write_new_file(fields, new_file)
