from Test_Tree import Test_Functions as Setup, setup_test_file as Test_Setup, maisonPrice as Price
import Forest_Tree.Forest as Forest
from Setup_Scripts import Config as Config, return_fields_by_tree as Fields, create_file_train as Create
import os


class UnknownElement(Exception):
    """If a element is unknowed"""


def clean_rep(path):
    for file in os.listdir(path):
        os.remove(f"{path}/{file}")


def return_result_path_from_id(id):
    return f"Results/result{id}.txt"


def write_result(path, result):
    # print(result)
    with open(path, "w") as file:
        file.write(result)


def read_file(path):
    with open(path, "r") as file:
        content = file.read()
        houses = content.split("\n")
        return houses


def return_price(forest, fields_by_tree):
    print("START")
    houses = read_file(Config.TEST_FILE)
    del houses[0]
    final_result = "id,SalePrice"
    for house in houses:
        att = house.split(",")
        try:
            id = att[0]
            if id == "":
                raise IndexError
            guess = forest.determine_classe(house, fields_by_tree)
            price = Price.pricing(id, guess.upper())
            final_result += f"\n{id},{price}"
        except IndexError:
            """
            Si jamais le fichier de test possède une ligne blanche ou avec des noms d'attributs erronés
            """
            pass
    print("DONE")
    # write_result(Config.FINAL_PATH, final_result)


def execute_forest():
    Create.start()
    Test_Setup.setup_test_file(Config.TEST_PATH, Config.TEST_PATH_RANGED)

    Setup.maisonAleatoire(Config.TEST_PATH_RANGED, Config.TEST_FILE, 30)
    fields_by_tree = Fields.return_fields_by_tree()
    forest = Forest.Forest(fields_by_tree.keys())
    forest.config_special_tree(["8", "9"])

    return_price(forest, fields_by_tree)


def start():
    execute_forest()

