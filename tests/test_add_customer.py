import allure
from tools.helpers import get_post_code, get_first_name
from assertions.assertions import assert_first_name_in_table

@allure.title("Test add customer")
def test_add_customer(manager_page):
    post_code = get_post_code()
    first_name = get_first_name(post_code)

    manager_page.click_add_cust(). \
        fill_first_name(first_name). \
        fill_last_name('Testov'). \
        fill_post_code(post_code). \
        click_bt_add_customer(). \
        alert_acept(). \
        click_customers()
    first_names = manager_page.get_list_first_names()
    assert_first_name_in_table(first_name, first_names)