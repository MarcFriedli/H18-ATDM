import random
import csv
import Forest_Tree.House as House
import Setup_Scripts.Config as Config


def return_nb_row(path):
    with open(path, "r") as file:
        counter = csv.reader(file)
        nb_row = sum(1 for row in counter)
    return nb_row


def return_field_name_by_index(index):
    """
    :param index: L'index dont on cherche le nom.
    :return: Le nom associé à l'index.
    """
    with open(Config.FIELDS_PATH) as file:
        content = file.read()
        elements = content.split(",")
        return elements[index]


def maisonAleatoire(path_in, path_out, amountHouse):
    # Variables locales
    arrValue = ['C1', 'C2', 'C3', 'M1', 'M2', 'M3', 'M4', 'E1', 'E2', 'E3']

    # Création de 10 vecteurs dans matrice contenant les identifiants donnés au hasard
    matClass = [[0 for x in range(amountHouse)] for y in range(len(arrValue))]
    for index in range(0, len(arrValue)):
        with open(path_in, 'r') as fileOriginal:
            reader = csv.reader(fileOriginal)
            try:
                data = [r for r in reader if r[80] == arrValue[index]]
                random.shuffle(data)
                for id in range(0, amountHouse):
                    matClass[index][id] = data[id][0]
                    id += 1
            except IndexError:
                print(f"error with index {index}")
        index += 1
        fileOriginal.close()

    # Créer un array qui retourne le numéro de colonne pour chacun des id dans matClass
    temp = []
    for index in range(0, len(arrValue)):
        try:
            for id in range(0, amountHouse):
                temp.append(matClass[index][id])
                id += 1
        except IndexError:
            print(f"error with index {int(matClass[index][id])}")
        index += 1
    test = []
    with open(path_in, 'r') as fileOriginal:
        reader = csv.reader(fileOriginal)
        data = [r for r in reader]
        for index in range(0, return_nb_row(path_in)):
            try:
                if data[index][0] in temp:
                    test.append(int(index))
            except IndexError:
                print(f"error with index {index}")
        index += 1
        fileOriginal.close()

    # Construction du nouveau fichier avec les données du fichier original
    with open(path_in, 'r') as fileOriginal:
        reader = csv.reader(fileOriginal)
        data = [r for r in reader]
        with open(path_out, 'w') as fileClass:
            writer = csv.writer(fileClass, lineterminator='\n')
            writer.writerow(data[0])
            for index in range(0, len(arrValue)*amountHouse):
                try:
                    writer.writerow(data[test[index]])
                except IndexError:
                    print(f"error with index {int(matClass[index][id])}")
                index += 1
        fileClass.close()
    fileOriginal.close()


def return_house_by_att(house, attributs):
    # print(attributs)
    try:
        del(attributs[attributs.index(80)])
    except ValueError:
        pass
    att = house.split(',')
    att_names = []
    att_values = []
    for toto in attributs:
        att_names.append(return_field_name_by_index(int(toto)))
        att_values.append(att[int(toto)])
    return House.House(att_names, att_values)
