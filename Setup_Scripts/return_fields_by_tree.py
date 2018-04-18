import re
import Setup_Scripts.Config as Config


def return_fields_by_tree():
    with open(Config.fields_by_tree, "r") as file:
        fields_by_tree = {}
        content = file.read()
        content = re.sub('[ ]', '', content)
        elements = content.split("\n")
        for line in elements:
            key = line[0]
            fields_by_tree[key] = []
            line = line[line.index('[') + 1:-1]
            fields = line.split(",")
            for field in fields:
                fields_by_tree[key].append(int(field))
    return fields_by_tree
