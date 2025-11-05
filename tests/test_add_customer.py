import allure

from assertions.assertions import assert_first_name_in_table
from tools.helpers import get_first_name, get_post_code


@allure.title("Test add customer")
def test_add_customer(manager_page):
    with allure.step("Get post code and first name"):
        post_code = get_post_code()
        first_name = get_first_name(post_code)

    with allure.step("Fill customer data and click add customer button"):
        manager_page.click_add_cust(). \
            fill_first_name(first_name). \
            fill_last_name('Testov'). \
            fill_post_code(post_code). \
            click_bt_add_customer(). \
            alert_accept(). \
            click_customers()
    with allure.step("Get list first names and assert customer added"):
        first_names = manager_page.get_list_first_names()
        assert_first_name_in_table(first_name, first_names)