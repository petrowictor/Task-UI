from typing import Self
from pages.base_page import BasePage
from elements.base_element import BaseElement
from tools.helpers import find_deleted_name

from selenium.webdriver.common.by import By

class ManagerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.bt_addCust = BaseElement(driver, "Add-Customer", '[ng-class="btnClass1"]')
        self.post_code = BaseElement(driver, "Post-Code", "[ng-model='postCd']")
        self.first_name = BaseElement(driver, "First-Name", "[ng-model='fName']")
        self.last_name = BaseElement(driver, "Last-Name", "[ng-model='lName']")
        self.bt_add_customer = BaseElement(driver, "Add-Customer", '[class="btn btn-default"]')
        self.alert_message = BaseElement(driver, "Alert-Message", "[ng-model='alertMessage']")
        
        self.bt_open_acct = BaseElement(driver, "Open-Account", '[ng-class="btnClass2"]')

        self.bt_customers = BaseElement(driver, "Customers", '[ng-class="btnClass3"]')
        self.bt_sort_first_name = BaseElement(driver, "Sort-First-Name", '[ng-click="sortType = \'fName\'; sortReverse = !sortReverse"]')
        self.row_customers = BaseElement(driver, "Row-Customers", "tr.ng-scope")

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

    def alert_acept(self):
        self.alert_message.accept()
        return self

    def click_sort_first_name(self):
        self.bt_sort_first_name.click()
        return self

    def get_list_first_names(self):
        self.row_customers.wait_for_all_elements()
        row_customers = self.driver.find_elements(By.CSS_SELECTOR, "tr.ng-scope")
        names = []
        for row in range(len(row_customers)):
            name_element = row_customers[row].find_element(By.CSS_SELECTOR, "td:nth-child(1)").text
            names.append(name_element)
        return names
    
    def click_bt_delete_customer(self):
        self.row_customers.wait_for_all_elements()
        names = self.get_list_first_names()
        name_average_length = find_deleted_name(names)
        for row in range(len(names)):
            if names[row] == name_average_length:
                delete_button = BaseElement(self.driver, "button-delete-customer", "button[ng-click*='deleteCust']")
                delete_button.click(row)
                return names[row]