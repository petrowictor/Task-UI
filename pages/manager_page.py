from typing import Self

import locators.manager_locators as Locators
from elements.base_element import BaseElement
from pages.base_page import BasePage
from tools.helpers import find_deleted_name


class ManagerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.bt_addCust = BaseElement(driver, "Add-Customer", Locators.BTN_ADD_CUSTOMER_TAB)
        self.post_code = BaseElement(driver, "Post-Code", Locators.FIELD_POST_CODE)
        self.first_name = BaseElement(driver, "First-Name", Locators.FIELD_FIRST_NAME)
        self.last_name = BaseElement(driver, "Last-Name", Locators.FIELD_LAST_NAME)
        self.bt_add_customer = BaseElement(driver, "Add-Customer", Locators.BTN_ADD_CUSTOMER_SUBMIT)
        self.alert_message = BaseElement(driver, "Alert-Message", Locators.ALERT_MESSAGE)
        
        self.bt_open_acct = BaseElement(driver, "Open-Account", Locators.BTN_OPEN_ACCOUNT_TAB)

        self.bt_customers = BaseElement(driver, "Customers", Locators.BTN_CUSTOMERS_TAB)
        self.bt_sort_first_name = BaseElement(driver, "Sort-First-Name", Locators.BTN_SORT_FIRST_NAME)
        self.row_customers = BaseElement(driver, "Row-Customers", Locators.ROW_CUSTOMER)

    def click_add_cust(self):
        self.bt_addCust.click()
        return self

    def click_open_acct(self):
        self.bt_open_acct.click()
        return self

    def click_customers(self):
        self.bt_customers.click()
        return self

    def click_bt_add_customer(self):
        self.bt_add_customer.click()
        return self
        
    def fill_first_name(self, value):
        self.first_name.fill(value)
        return self
    
    def fill_post_code(self, value):
        self.post_code.fill(value)
        return self

    def fill_last_name(self, value) -> Self:
        self.last_name.fill(value)
        return self

    def alert_accept(self):
        self.alert_message.accept()
        return self

    def click_sort_first_name(self):
        self.bt_sort_first_name.click()
        return self

    def get_list_first_names(self):
        self.row_customers.wait_for_all_elements()
        row_customers = self.driver.find_elements(*Locators.ROW_CUSTOMER)
        names = []
        for row in range(len(row_customers)):
            name_element = row_customers[row].find_element(*Locators.FIRST_CHILD).text
            names.append(name_element)
        return names
    
    def click_bt_delete_customer(self):
        self.row_customers.wait_for_all_elements()
        names = self.get_list_first_names()
        name_average_length = find_deleted_name(names)
        for row in range(len(names)):
            if names[row] == name_average_length:
                delete_button = BaseElement(self.driver, "button-delete-customer", Locators.BTN_DELETE_SUBMIT)
                delete_button.click(row)
                return names[row]