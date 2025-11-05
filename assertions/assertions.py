def assert_first_name_in_table(name, first_names):
    assert name in first_names, f"{name} not in list"

def assert_sort_names_ascending(first_names):
    assert first_names == sorted(first_names), "Names not sorted in ascending order"

def assert_sort_names_descending(first_names):
    assert first_names == sorted(first_names, reverse=True), "Names not sorted in descending order"

def assert_delete_customer(name, first_names):
    assert name not in first_names, f"{name} still in list"