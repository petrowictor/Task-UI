import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoAlertPresentException

from tools.logger import get_logger

logger = get_logger("ALERT")

class Alert:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def type_of(self)-> str:
        return "Alert"

    def accept(self):
        step = f"Check {self.type_of()} is present"
        with allure.step(step):
            logger.info(step)
            try:
                alert = self.driver.switch_to.alert
                allure.attach(
                    f"Alert is present",
                    name="Alert detected",
                    attachment_type=allure.attachment_type.TEXT
                )
                alert.accept()
            except NoAlertPresentException:
                allure.attach(
                    f"Alert is not present",
                    name="Alert detected",
                    attachment_type=allure.attachment_type.TEXT
                )