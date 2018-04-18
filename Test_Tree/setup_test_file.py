import Setup_Scripts.Config as Config


def return_range_index():
    with open(Config.RANGE_BY_FIELD_PATH, "r") as file:
        content = file.read()
        line = content.split("\n")
        range_index_dic = {}
        for elements in line:
            element = elements.split(",")
            try:
                range_index_dic[int(element[0])] = element[1]
            except IndexError:
                pass
        return range_index_dic


def return_field_name_by_index(index):
    """
    :param index: L'index dont on cherche le nom.
    :return: Le nom associé à l'index.
    """
    with open(Config.FIELDS_PATH) as file:
        content = file.read()
        elements = content.split(",")
        return elements[index]


def write_new_file(path, new_values):
    """
    Ecris le contenu du dictionnaire values_to_change dans le nouveau fichier.
    """
    nb_fields = len(new_values) - 1
    nb_object = len(return_all_values(Config.TEST_PATH)) - 2
    with open(path, "w") as file:
        for i in range(0, 81):
            file.write(return_field_name_by_index(i) + ",")
        file.write("\n")
        for j in range(0, nb_object - 1):
            for k in range(0, nb_fields + 1):
                file.write(str(new_values[k][j]) + ",")
            file.write("\n")


def return_all_values(path):
    """
    Ouvre le fichier dont on veut prétraiter les données.
    :return: Une liste contenant toutes les données.
    """
    with open(path, "r") as file:
        content = file.read()
        return content.split("\n")


def transform_value_by_range(data, index):
    range_index_dic = return_range_index()
    new_data = []
    for item in data:
        val = int(item)
        if val == 0:
            new_data.append(val)
        else:
            range = int(range_index_dic[index])
            x = int((val - 1) / range) + 1
            max = x * range
            min = (x - 1) * range + 1
            new_data.append(f"[{min}-{max}]")
            #print(f"val : {val} range : {range} x : {x}")
    return new_data


def transform_value_by_year(data):
    """
    :param data: Liste contenant des années .
    :return: La même liste mais avec les années arrondies à la décénie en dessous.
    """
    new_data = []
    for val in data:
        try:
            new_data.append(int(int(val) / 10) * 10)
        except ValueError:
            new_data.append(0)
    return new_data


def preprocess_values(index, values):
    """
       Insère les données modifiées d'un champs dans le dictionnaire values_to_change
       :param index:
       :return:
       """
    data = []
    new_data = []
    range_index = return_range_index().keys()
    year_index = (19, 20, 59)
    for element in values:
        values = element.split(",")
        for i, v in enumerate(values):
            if i == index:
                data.append(v)
    del data[0]
    if index in range_index:
        new_data = transform_value_by_range(data, index)
    elif index in year_index:
        new_data = transform_value_by_year(data)
    else:
        new_data = data
    return new_data


def setup_test_file(path, new_path):
    values = return_all_values(path)
    new_values = {}
    for i in range(0, 81):
        new_values[i] = preprocess_values(i, values)
    write_new_file(new_path, new_values)
