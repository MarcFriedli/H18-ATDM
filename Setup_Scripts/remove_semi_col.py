def return_all_values(path):
    """
    Ouvre le fichier dont on veut prétraiter les données.
    :return: Une liste contenant toutes les données.
    """
    with open(path, "r") as file:
        content = file.read()
        return content.split("\n")


def write_new_values(path, data):
    with open(path, "w") as file:
        for line in data:
            file.write(line)
            file.write("\n")


def remove_semi_col(path):
    data = return_all_values(path)
    new_data = []
    for line in data:
        if "saleprice" in line.lower():
            toto = len("saleprice") + 1
            line = line[:-toto]
        new_data.append(line[:-1])
    write_new_values(path, new_data)
