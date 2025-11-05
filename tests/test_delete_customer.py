import allure

from assertions.assertions import assert_delete_customer


@allure.title("Test delete customer")
def test_delete_customer(manager_page):
    with allure.step("Click button customers"):
        manager_page.click_customers()
    with allure.step("Get deleted customer"):
        deleted_name = manager_page.click_bt_delete_customer()
    with allure.step("Get list first names"):
        first_names = manager_page.get_list_first_names()
    with allure.step("Assert deleted customer"):
        assert_delete_customer(deleted_name, first_names)