from selenium.webdriver.common.by import By

BTN_ADD_CUSTOMER_TAB = (By.CSS_SELECTOR, '[ng-class="btnClass1"]')
BTN_OPEN_ACCOUNT_TAB = (By.CSS_SELECTOR, '[ng-class="btnClass2"]')
BTN_CUSTOMERS_TAB = (By.CSS_SELECTOR, '[ng-class="btnClass3"]')
FIELD_FIRST_NAME = (By.CSS_SELECTOR, "[ng-model='fName']")
FIELD_LAST_NAME = (By.CSS_SELECTOR, "[ng-model='lName']")
FIELD_POST_CODE = (By.CSS_SELECTOR, "[ng-model='postCd']")
BTN_ADD_CUSTOMER_SUBMIT = (By.CSS_SELECTOR, '[class="btn btn-default"]')
BTN_SORT_FIRST_NAME = (By.CSS_SELECTOR, '[ng-click="sortType = \'fName\'; sortReverse = !sortReverse"]')
ROW_CUSTOMER = (By.CSS_SELECTOR, "tr.ng-scope")
ALERT_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-danger")
FIRST_CHILD = (By.CSS_SELECTOR, "td:nth-child(1)")
BTN_DELETE_SUBMIT = (By.CSS_SELECTOR, "button[ng-click*='deleteCust']")