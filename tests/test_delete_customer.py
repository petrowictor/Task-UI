import allure
from assertions.assertions import assert_delete_customer

@allure.title("Test delete customer")
def test_delete_customer(manager_page):
    manager_page.click_customers()
    deleted_name = manager_page.click_bt_delete_customer()
    first_names = manager_page.get_list_first_names()
    assert_delete_customer(deleted_name, first_names)