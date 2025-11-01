from tools.rand_post_code import random_post_code
from tools.postcode_to_name import postcode_to_name
from tools.find_name_closest_to_average_length import find_name_closest_to_average_length

class TestCases:
    def test_add_customer(self, manager_page):
        post_code = random_post_code()
        first_name = postcode_to_name(post_code)     
        
        manager_page.click_add_cust(). \
            fill_first_name(first_name). \
            fill_last_name('Testov'). \
            fill_post_code(post_code). \
            click_bt_add_customer(). \
            alert_acept(). \
            click_customers(). \
            check_first_name_in_table(first_name)

    def test_sort_customers(self, manager_page):
        manager_page.click_customers(). \
            click_sort_first_name(). \
            check_sort_names_descending(). \
            click_sort_first_name(). \
            check_sort_names_ascending()

    def test_delete_customer(self, manager_page):
        manager_page.click_customers()
        deleted_name = manager_page.click_bt_delete_customer()
        manager_page.check_delete_customer(deleted_name)
            