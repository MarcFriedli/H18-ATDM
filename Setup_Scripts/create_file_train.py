from Setup_Scripts import return_fields_by_tree as Fields, crate_file_with_field as Create, remove_semi_col as Remove


def start():
    fields_by_tree = Fields.return_fields_by_tree()
    for key, value in fields_by_tree.items():
        path = f"../Train_Files/train_tree{key}.csv"
        Create.create_file_with_field(value, path)
        Remove.remove_semi_col(path)


# start()