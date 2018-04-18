TEST_PATH = "../Ressources/sample_test_with_class.csv"
TEST_PATH_RANGED = "../Ressources/sample_test_with_class_with_range.csv"
TEST_FILE = "test_house.csv"

TRAIN_PATH = "../Ressources/sample_train_with_class.csv"
TRAIN_PATH_RANGED = "../Ressources/sample_train_with_class_with_range.csv"
TRAIN_PATH_PRICE = "../Ressources/sample_train_with_class_and_price.csv"
TRAIN_PATH_PRICE_RANGE = "../Ressources/sample_train_with_class_range_and_price.csv"

FIELDS_PATH = "../Ressources/fields.txt"
fields_by_tree = "../Ressources/fields_by_tree.txt"
RANGE_BY_FIELD_PATH = "../Ressources/range_by_field.txt"

FINAL_PATH = "../Ressources/final_result.csv"

forest_trust = {
    "c1": [0.57, 0.34],
    "c2": [0.41, 0.13],
    "c3": [0.08, 0.37],
    "m1": [0.18, 0.49],
    "m2": [0.21, 0.44],
    "m3": [0.19, 0.41],
    "m4": [0.19, 0.44],
    "e1": [0.28, 0.37],
    "e2": [0.26, 0.30],
    "e3": [0.74, 0.08],
}

tree_trust = {
    "1": [0.36, 0.39],
    "2": [0.2, 0.35],
    "3": [0.23, 0.36],
    "4": [0.23, 0.37],
    "5": [0.27, 0.29],
    "6": [0.24, 0.38],
    "7": [0.27, 0.33],
    "8": [0.22, 0.34],
    "9": [0.25, 0.35],
}

mode_trust = {
    "c1": [0.33, 0.22],
    "c2": [0.25, 0.39],
    "c3": [0.19, 0.46],
    "m1": [0.24, 0.27],
    "m2": [0.27, 0.44],
    "m3": [0.27, 0.42],
    "m4": [0.26, 0.46],
    "e1": [0.36, 0.55],
    "e2": [0.37, 0.43],
    "e3": [0.68, 0.15],
}

avg_trust = {
    "c1": [0.69, 0.12],
    "c2": [0.35, 0.47],
    "c3": [0.26, 0.37],
    "m1": [0.24, 0.36],
    "m2": [0.18, 0.37],
    "m3": [0.34, 0.28],
    "m4": [0.30, 0.32],
    "e1": [0.30, 0.58],
    "e2": [0.19, 0.8],
    "e3": [1.00, 0.00],
}

pondere_trust = {
    "c1": [0.47, 0.24],
    "c2": [0.27, 0.41],
    "c3": [0.24, 0.36],
    "m1": [0.37, 0.29],
    "m2": [0.35, 0.42],
    "m3": [0.25, 0.43],
    "m4": [0.32, 0.52],
    "e1": [0.41, 0.55],
    "e2": [0.38, 0.49],
    "e3": [0.78, 0.15],
}

class_name = ["c1", "c2", "c3", "m1", "m2", "m3", "m4", "e1", "e2", "e3"]