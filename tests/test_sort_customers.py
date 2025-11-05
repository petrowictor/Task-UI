import allure

from assertions.assertions import (
    assert_sort_names_ascending,
    assert_sort_names_descending,
)


@allure.title("Test sort customers")
def test_sort_customers(manager_page):
    with allure.step("Click button customers"):
        manager_page.click_customers()

    with allure.step("Click button sort first name"):
        manager_page.click_sort_first_name()
    with allure.step("Get list first names and assert sort in descending order"):
        first_names = manager_page.get_list_first_names()
        assert_sort_names_descending(first_names)

    with allure.step("Click button sort first name"):
        manager_page.click_sort_first_name()
    with allure.step("Get list first names and assert sort in ascending order"):
        first_names = manager_page.get_list_first_names()
        assert_sort_names_ascending(first_names)