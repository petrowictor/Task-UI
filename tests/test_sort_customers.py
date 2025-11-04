import allure
from assertions.assertions import assert_sort_names_descending, assert_sort_names_ascending

@allure.title("Test sort customers")
def test_sort_customers(manager_page):
    manager_page.click_customers(). \
        click_sort_first_name()
    first_names = manager_page.get_list_first_names()
    assert_sort_names_descending(first_names)

    manager_page.click_sort_first_name()
    first_names = manager_page.get_list_first_names()
    assert_sort_names_ascending(first_names)